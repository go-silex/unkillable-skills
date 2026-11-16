#!/usr/bin/env python3
"""embed.py: make a slides deck standalone, or lint it.

    python3 embed.py deck.html            # writes deck-standalone.html next to it
    python3 embed.py deck.html -o out.html
    python3 embed.py --check deck.html    # lint only, writes nothing

Embed mode inlines every local <img src> and CSS url() as a base64 data URI.
Remote URLs (http, https, //) and data URIs are left alone, so an optional
Google Fonts <link> stays a link (the chassis falls back to system fonts offline).
Exits 2 if a local file is missing (nothing is written).

Check mode reports, with line numbers:
  errors (exit 1): leftover {{PLACEHOLDERS}} outside HTML comments, em dashes,
    titles in full uppercase, more than one accent per slide, more than five
    bullets, local images that do not exist, no slide at all.
  warnings (exit 0): titles over 90 characters, steps outside 3 to 5,
    weak contrast between brand tokens (hex or rgb values only).

Standard library only, Python 3.8+.
"""
import argparse
import base64
import html
import mimetypes
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

EM_DASH = "\u2014"  # escaped so this file stays free of the character itself
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
TITLE_TAGS = {"h1", "h2", "h3"}
TITLE_CLASSES = {"title", "statement"}

IMG_SRC = re.compile(r"(<img\b[^>]*?\bsrc\s*=\s*)([\"'])(.*?)\2", re.I | re.S)
CSS_URL = re.compile(r"url\(\s*(&quot;|[\"']?)(.*?)\1\s*\)", re.I | re.S)


# ---------------------------------------------------------------- helpers

def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def local_path(ref, base):
    """Return the local Path a reference points to, or None if it is remote, inline or empty."""
    ref = html.unescape(ref.strip())
    if not ref or "{{" in ref or ref.startswith("#"):
        return None
    low = ref.lower()
    if low.startswith(("data:", "http:", "https:", "//", "mailto:", "blob:", "about:", "javascript:")):
        return None
    if low.startswith("file:"):
        p = Path(unquote(urlsplit(ref).path))
    else:
        p = Path(unquote(urlsplit(ref).path))
        if not p.is_absolute():
            p = base / p
    return p


def data_uri(path):
    mime = mimetypes.guess_type(path.name)[0]
    if path.suffix.lower() == ".svg":
        mime = "image/svg+xml"
    elif path.suffix.lower() == ".webp":
        mime = "image/webp"
    elif path.suffix.lower() in (".woff2", ".woff", ".ttf", ".otf"):
        mime = "font/" + path.suffix.lower()[1:]
    return f"data:{mime or 'application/octet-stream'};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def find_local_refs(text, base):
    """Yield (kind, start, end, ref, path) for every local reference in the document."""
    for m in IMG_SRC.finditer(text):
        p = local_path(m.group(3), base)
        if p is not None:
            yield ("img", m.start(3), m.end(3), m.group(3), p)
    for m in CSS_URL.finditer(text):
        p = local_path(m.group(2), base)
        if p is not None:
            yield ("url", m.start(2), m.end(2), m.group(2), p)


# ---------------------------------------------------------------- embed

def embed(src, out):
    text = src.read_text(encoding="utf-8")
    base = src.parent
    refs = sorted(find_local_refs(text, base), key=lambda r: r[1])
    missing = [(r, line_of(text, s)) for (_, s, _, r, p) in refs if not p.is_file()]
    for ref, ln in missing:
        print(f"WARNING line {ln}: file not found: {ref}", file=sys.stderr)
    if missing:
        print(f"FAILED: {len(missing)} missing file(s), nothing written.", file=sys.stderr)
        return 2
    cache, parts, last = {}, [], 0
    for _, s, e, ref, p in refs:
        key = p.resolve()
        if key not in cache:
            cache[key] = data_uri(p)
        parts.append(text[last:s])
        parts.append(cache[key])
        last = e
    parts.append(text[last:])
    result = "".join(parts)
    if re.search(r"\{\{[^{}]*\}\}", re.sub(r"<!--.*?-->", "", result, flags=re.S)):
        print("Note: placeholders {{...}} are still in the deck. Run --check.", file=sys.stderr)
    out.write_text(result, encoding="utf-8")
    size = out.stat().st_size / 1048576
    print(f"OK: {out} ({len(cache)} file(s) embedded, {len(refs)} reference(s), {size:.2f} MB)")
    return 0


# ---------------------------------------------------------------- check

class SlideScanner(HTMLParser):
    """Collects per-slide facts: accents, titles, bullets, steps."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides = []      # dicts
        self.stack = []       # open tags: (tag, classes)
        self.slide = None
        self.slide_depth = None
        self.capture = None   # [depth, line, chunks]

    def _classes(self, attrs):
        return set((dict(attrs).get("class") or "").split())

    def handle_starttag(self, tag, attrs):
        cls = self._classes(attrs)
        line = self.getpos()[0]
        if self.slide is None and tag == "section" and "slide" in cls:
            self.slide = {"line": line, "classes": cls, "accents": [], "titles": [], "bullets": 0, "steps": 0}
            if "on-accent" in cls:
                self.slide["accents"].append(line)
            self.slides.append(self.slide)
            self.slide_depth = len(self.stack)
        elif self.slide is not None:
            if "accent" in cls:
                self.slide["accents"].append(line)
            if tag == "li":
                parent = self.stack[-1][1] if self.stack else set()
                if "bullets" in parent:
                    self.slide["bullets"] += 1
                if "step" in cls:
                    self.slide["steps"] += 1
            if self.capture is None and (tag in TITLE_TAGS or cls & TITLE_CLASSES):
                self.capture = [len(self.stack), line, []]
        if tag not in VOID:
            self.stack.append((tag, cls))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            t, _ = self.stack.pop()
            depth = len(self.stack)
            if self.capture is not None and depth == self.capture[0]:
                txt = " ".join("".join(self.capture[2]).split())
                self.slide["titles"].append((self.capture[1], txt))
                self.capture = None
            if self.slide is not None and depth == self.slide_depth:
                self.slide = None
                self.slide_depth = None
            if t == tag:
                break

    def handle_data(self, data):
        if self.capture is not None:
            self.capture[2].append(data)


def parse_color(v):
    v = v.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h[:3])
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"rgba?\(\s*(\d+)[\s,]+(\d+)[\s,]+(\d+).*\)", v)
    if m:
        return tuple(int(x) for x in m.groups())
    return None


def contrast(a, b):
    def lum(c):
        ch = [x / 255 for x in c]
        ch = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in ch]
        return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def check(src):
    text = src.read_text(encoding="utf-8")
    errors, warnings = [], []
    no_comments = re.sub(r"<!--.*?-->", lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)

    for m in re.finditer(r"\{\{[^{}]*\}\}", no_comments):
        errors.append((line_of(text, m.start()), f"placeholder left: {m.group(0)}"))
    for m in re.finditer(EM_DASH, text):
        ctx = text[max(0, m.start() - 30):m.end() + 30].replace("\n", " ").strip()
        errors.append((line_of(text, m.start()), f"em dash: ...{ctx}..."))

    for _, s, _, ref, p in find_local_refs(no_comments, src.parent):
        if not p.is_file():
            errors.append((line_of(text, s), f"local file not found: {ref}"))

    scanner = SlideScanner()
    scanner.feed(text)
    scanner.close()
    if not scanner.slides:
        errors.append((1, 'no <section class="slide ..."> found'))
    for i, sl in enumerate(scanner.slides, 1):
        tag = f"slide {i}"
        if len(sl["accents"]) > 1:
            errors.append((sl["line"], f"{tag}: {len(sl['accents'])} accents (lines {', '.join(map(str, sl['accents']))}), one per slide"))
        if sl["bullets"] > 5:
            errors.append((sl["line"], f"{tag}: {sl['bullets']} bullets, five max"))
        if sl["steps"] and not 3 <= sl["steps"] <= 5:
            warnings.append((sl["line"], f"{tag}: {sl['steps']} steps, use 3 to 5"))
        for ln, t in sl["titles"]:
            letters = [c for c in t if c.isalpha()]
            if len(letters) >= 5 and t == t.upper():
                errors.append((ln, f"{tag}: title in full uppercase: {t[:60]}"))
            if len(t) > 90:
                warnings.append((ln, f"{tag}: title of {len(t)} characters, may exceed three lines"))

    root = re.search(r":root\s*\{(.*?)\}", no_comments, re.S)
    if root:
        body = re.sub(r"/\*.*?\*/", "", root.group(1), flags=re.S)
        tok = {k: parse_color(v) for k, v in re.findall(r"--([\w-]+)\s*:\s*([^;]+);", body)}
        pairs = [("ink", "bg", 4.5), ("ink-soft", "bg", 4.5), ("ink", "surface", 4.5), ("accent-ink", "accent", 4.5)]
        for fg, bg, need in pairs:
            a, b = tok.get(fg), tok.get(bg)
            if a and b:
                r = contrast(a, b)
                if r < need:
                    warnings.append((line_of(text, root.start()), f"contrast --{fg} on --{bg} is {r:.1f}:1, aim for {need}:1 or more"))

    for ln, msg in sorted(errors):
        print(f"ERROR   line {ln}: {msg}")
    for ln, msg in sorted(warnings):
        print(f"WARNING line {ln}: {msg}")
    n = len(scanner.slides)
    status = "FAILED" if errors else "PASSED"
    print(f"{status}: {src.name}, {n} slide(s), {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck", help="deck HTML file")
    ap.add_argument("-o", "--out", help="output file (default: <name>-standalone.html next to the deck)")
    ap.add_argument("--check", action="store_true", help="lint only, write nothing")
    a = ap.parse_args()
    src = Path(a.deck).expanduser()
    if not src.is_file():
        print(f"not found: {src}", file=sys.stderr)
        return 2
    if a.check:
        return check(src)
    out = Path(a.out).expanduser() if a.out else src.with_name(src.stem + "-standalone.html")
    return embed(src, out)


if __name__ == "__main__":
    sys.exit(main())
