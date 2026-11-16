---
name: slides
description: Makes a 16:9 HTML slide deck in the user's own brand. On first use it sets up the brand kit (brand book, logos, colors, fonts) in the brain and derives the user's deck template from it; afterwards it writes decks from a brief or notes, using the brain's context, and checks every slide before delivering. Works in any browser and prints to PDF. Use when the user says "slides", "deck", "présentation", "fais-moi un deck", "make a presentation", "set up my brand", "configure ma charte".
---

# Slides

A deck in the user's brand, built from a fixed chassis so it always works: 1920 × 1080 stage scaled to the window, arrow keys, slide counter, print to PDF. Talk in the user's language; the deck is in the language of its audience.

## What ships with this skill

| File | Role |
|---|---|
| `assets/chassis.html` | CSS and JS of every deck, driven by tokens (`--bg`, `--surface`, `--ink`, `--ink-soft`, `--accent`, `--accent-ink`, `--line`, `--font-display`, `--font-body`, `--radius`; optional `--display-weight`, `--display-tracking`, `--logo-filter`) and placeholders `{{LANG}}`, `{{DECK_TITLE}}`, `{{FONTS_URL}}`, `{{LOGO}}`, `{{FOOTER}}`. `#N` or `?slide=N` opens slide N; `?debug` outlines overflowing slides in red. Never rewritten. |
| `references/layouts.md` | The catalog: copyable blocks with "use for" and rules. |
| `assets/sample_deck.html` | Every layout once, neutral palette. |
| `scripts/embed.py` | `--check` lints a deck (placeholders left, em dashes, uppercase titles, two accents on a slide). Without `--check`, writes a `-standalone.html` copy with images inlined, for sending. |

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states.

- Brand path: `## Brain map`, role Brand (default `_System/Brand/` only if the map has none).
- Several brands (a company, a second company, a personal brand): `AGENTS.md` may say which brand serves which deck and where the deliverable goes. Follow it. If it does not, ask which brand.
- An entity's brand that lives elsewhere (a shared drive): read it there, never copy it into the brain.
- Deliverables: where `AGENTS.md` routes them. Otherwise next to the project note, or `<Cockpit>/Decks/`.

## Phase 0: brand setup (first use, or a brand without a kit)

A brand is ready when its folder holds `Brand_Kit.md` and `Deck_Template.html`. If not:

1. Ask in one message:
   - Do you have a brand book, brand guide or charter (PDF, link, Figma)? Please drop it in `<Brand>/source/`.
   - Your logos (SVG or PNG, light and dark versions if any), in `<Brand>/assets/`.
   - Your fonts (names; files if they are not Google Fonts).
   - A deck you like (yours or one you admire), optional.
   - Nothing at all? Give me your website: I will draft a kit from it for you to correct.
2. Read what they gave. Extract: colors (background, text, accent, lines), fonts, logo files, rules (spacing, what is forbidden, tone of titles).
3. Write `<Brand>/Brand_Kit.md`:

```markdown
---
type: reference
created: YYYY-MM-DD
source: <brand book file, website, or "drafted, to confirm">
---

# Brand kit · <brand>

## Tokens
| Token | Value | From |
|---|---|---|
| --bg | #... | brand book p. 4 |
| --surface | | |
| --ink | | |
| --ink-soft | | |
| --accent | | |
| --accent-ink | | |
| --line | | |
| --font-display | | |
| --font-body | | |
| --radius | | |

## Logos
- Light background: `assets/<file>`
- Dark background: `assets/<file>`

## Rules
- <what the brand book imposes or forbids, one line each>
```

   Check contrast: `--ink` on `--bg` and `--accent-ink` on `--accent` must be readable (aim for a WCAG ratio of 4.5 or more). Propose a fix if not.
4. Build `<Brand>/Deck_Template.html`: copy `assets/chassis.html`, set the tokens, fill `{{FONTS_URL}}` (or delete that line for system fonts), `{{LANG}}`, `{{FOOTER}}`, and point `{{LOGO}}` to the logo (relative path from the template). On a dark background use the light logo; if there is none and the logo is one color, set `--logo-filter: brightness(0) invert(1)`. Leave `<!-- SLIDES -->` and `{{DECK_TITLE}}` in place.
5. Show a 3-slide sample (cover, bullets, big number) made from the template, open it if a browser is available, and ask: "Does this look like your brand?" Adjust tokens until yes. Never touch the chassis CSS to fix a brand: only tokens, or a commented `/* Brand adjustments */` block in the template's own `<style>`, after the chassis CSS.

## Phase 1: brief

One grouped question, skipped for what the request already says:

1. Goal and audience (pitch, board, team, talk, client proposal).
2. Length: short (6 to 10), medium (12 to 20).
3. Content: provided, raw notes, or just the subject (then draw from the brain: Context, project notes, decisions, person notes of the audience).
4. Brand, if several.

Never ask about style: it comes from the kit.

## Phase 2: build

1. Read `references/layouts.md` fully and the brand's `Brand_Kit.md` rules.
2. Write the plan: one line per slide, `layout → idea`. One slide, one idea. Show it and wait for a yes when the deck has more than 8 slides.
3. Copy `Deck_Template.html` to the deliverable folder as `YYYY-MM-DD_Deck_<Subject>.html`. Set `{{DECK_TITLE}}`. Paste the catalog blocks at `<!-- SLIDES -->`, replacing only texts, images and numbers. The cover and closing blocks hold their own `{{LOGO}}`: fill it there too.
   - Titles: a name or a short phrase, never a full sentence, never all caps, three lines at most.
   - One accent per slide at most.
   - Facts, numbers and names come from the brain or the user. A missing figure is a visible `[to fill]`, never invented. Prices only from the brain's source of truth for offers.
   - Text is written then checked with the `de-ai-ify` rules. No em dash.
4. Run `python3 <skill>/scripts/embed.py --check <deck>` and fix every warning.

## Phase 3: check before saying done

Open the deck in a browser if you have one (a local file is enough; `#N` in the URL opens slide N). Look at every slide:

- Nothing overflows the stage, nothing overlaps.
- Readable contrast everywhere; the logo shows on the cover.
- Counter coherent; the first slide shows without a click.

No browser available: say so plainly, and tell the user which slides to check by eye.

## Phase 4: deliver

- Path of the deck, one line per slide of the plan.
- To send it: `python3 <skill>/scripts/embed.py <deck>` writes a `-standalone.html` with images inlined. For a PDF: open in Chrome, Print, "Save as PDF", landscape, no margins.
- If a new layout was needed and the user liked it, offer to save it in `<Brand>/Layouts_Local.md` for next time.

## Rules

- The chassis is never rewritten, simplified or replaced by another engine.
- A brand's kit is the user's: never mix two brands in one deck.
- Never send or publish the deck anywhere without an explicit yes.
