#!/usr/bin/env python3
"""Checks the plugin before a release: manifests agree, every skill is valid.
Usage: python3 scripts/check.py"""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
errors = []

manifests = {
    "plugin.json": root / "plugin.json",
    ".claude-plugin/plugin.json": root / ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json": root / ".codex-plugin/plugin.json",
}
data = {}
for label, path in list(manifests.items()) + [
    (".claude-plugin/marketplace.json", root / ".claude-plugin/marketplace.json"),
    (".agents/plugins/marketplace.json", root / ".agents/plugins/marketplace.json"),
]:
    try:
        data[label] = json.loads(path.read_text())
    except Exception as e:
        errors.append(f"{label}: {e}")

names = {data[m].get("name") for m in manifests if m in data}
versions = {data[m].get("version") for m in manifests if m in data}
cm = data.get(".claude-plugin/marketplace.json", {}).get("plugins", [{}])[0]
names.add(cm.get("name")); versions.add(cm.get("version"))
names.add(data.get(".agents/plugins/marketplace.json", {}).get("plugins", [{}])[0].get("name"))
if len(names) != 1: errors.append(f"plugin names differ: {names}")
if len(versions) != 1: errors.append(f"versions differ: {versions}")

skills = sorted(p for p in (root / "skills").iterdir() if p.is_dir())
for d in skills:
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: SKILL.md missing"); continue
    text = f.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{d.name}: no frontmatter"); continue
    fm = dict(re.findall(r"^(\w[\w-]*):\s*(.*)$", m.group(1), re.M))
    if fm.get("name") != d.name: errors.append(f"{d.name}: name '{fm.get('name')}' != folder")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", d.name) or len(d.name) > 64:
        errors.append(f"{d.name}: name must be kebab-case, <= 64 chars")
    desc = fm.get("description", "")
    if not desc: errors.append(f"{d.name}: description missing")
    if len(desc) > 1024: errors.append(f"{d.name}: description {len(desc)} chars > 1024")
    if "—" in text: errors.append(f"{d.name}: em dash found")
    for ref in re.findall(r"`(\w[\w-]*)` skill|the `(\w[\w-]*)` skill", text):
        pass

if errors:
    print("FAIL"); [print(" -", e) for e in errors]; sys.exit(1)
print(f"OK: plugin '{names.pop()}' v{versions.pop()}, {len(skills)} skills: " + ", ".join(d.name for d in skills))
