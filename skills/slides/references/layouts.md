# Slide layouts

Twelve copyable blocks for `assets/chassis.html`. A deck is the chassis (brand tokens filled once, in the client's template) with blocks pasted in place of `<!-- SLIDES -->`. Copy a block as is, keep its classes, replace only the `{{PLACEHOLDERS}}`, then delete the lines you do not need (an extra bullet, a fourth step).

## Global rules

- **One idea per slide.** If it does not fit, make two slides. Never shrink the type to make it fit.
- **Titles:** sentence case, never full uppercase, three lines at most (about 90 characters). A title says the point, not the topic: "Costs fall by a third", not "Costs".
- **One accent per slide.** The accent is the element with the class `accent` (a card, a row, a step, a marked phrase), or the whole slide when it carries `on-accent`. Never two. Blocks that ship with an accent already have it: move it, do not add a second.
- **No em dash anywhere.** Use a colon, a comma, parentheses or a new sentence.
- **Short text.** Bullets: one line each, two at most, five bullets max. Card and step text: two short sentences at most.
- **Colors come from the tokens only.** No hex value, no inline `style` color in a slide. If a block looks wrong in a palette, fix the tokens, not the slide.
- **Images are local files** next to the deck (`img/photo.jpg`), then `scripts/embed.py` turns them into a single standalone file. An image with no source yet: leave `src=""`, the grey placeholder shows.
- **Logos** use `{{LOGO}}` everywhere (the chassis and the cover and closing blocks). An empty `src` hides the logo cleanly. The small mark in the footer is hidden on accent slides and on the closing slide.
- Before delivering: `python3 scripts/embed.py --check deck.html` must pass, then look at every slide (`deck.html#4` opens slide 4; `?debug` outlines slides whose content leaves the safe area).

## Shared pieces

| Piece | Markup | Note |
|---|---|---|
| Kicker | `<p class="kicker">Context</p>` | Small label above a title, one to three words. Optional everywhere. |
| Title | `<h2 class="title">...</h2>` | `h1` on the cover only. |
| Lead | `<p class="lead">...</p>` | One or two sentences under a title. Optional. |
| Head | `<header class="head">` | Wraps kicker, title and lead at the top of content slides. |
| Label | `<p class="label">...</p>` | Small uppercase metadata inside a card, column, step, table header. |
| Footer | injected by the chassis | Logo mark, footer text (`data-footer` on `.deck-stage`) and `03 / 12`. Not on the cover. Add `data-nofoot` to a slide to remove it. |
| Accent slide | add `on-accent` to the section class | Background becomes `--accent`, text `--accent-ink`. Section dividers ship with it. |

## 1. Cover

**Class:** `s-cover`
**Use for:** the first slide: deck title, one-line promise, date and presenter.
**Rules:** one cover per deck. Title on two lines at most. The accent is the short bar above the title.

```html
<section class="slide s-cover">
  <img class="brand-logo" src="{{LOGO}}" alt="{{COMPANY}}">
  <div class="cover-main">
    <div class="cover-bar accent"></div>
    <h1 class="title">{{DECK_TITLE}}</h1>
    <p class="lead">{{SUBTITLE}}</p>
  </div>
  <div class="cover-meta"><span>{{DATE}}</span><span>{{PRESENTER}}</span><span>{{AUDIENCE}}</span></div>
</section>
```

## 2. Section divider

**Class:** `s-section` (with `on-accent`)
**Use for:** opening a part of the deck, three to five per deck at most.
**Rules:** the big number is the part number (`01`, `02`). Title of two to five words. Remove `on-accent` for a calmer divider on the background color; never put another accent on this slide.

```html
<section class="slide s-section on-accent">
  <div class="section-num">{{NN}}</div>
  <p class="kicker">{{PART_LABEL}}</p>
  <h2 class="title">{{SECTION_TITLE}}</h2>
  <p class="lead">{{SECTION_INTRO}}</p>
</section>
```

## 3. Statement

**Class:** `s-statement`
**Use for:** one big sentence: a belief, a finding, the key message before or after a dense part.
**Rules:** 20 words max. The marked phrase (`span.accent`) is two to four words, or remove the span. The source line is optional.

```html
<section class="slide s-statement">
  <p class="kicker">{{KICKER}}</p>
  <p class="statement">{{STATEMENT_START}} <span class="accent">{{KEY_PHRASE}}</span> {{STATEMENT_END}}</p>
  <p class="source">{{SOURCE}}</p>
</section>
```

## 4. Bullets

**Class:** `s-bullets`
**Use for:** a short list of parallel points: reasons, findings, requirements.
**Rules:** five bullets max, one line each (two at most). Start each with the strong word in `<b>`, the rest in `<span>`. Optional: `class="accent"` on the one bullet that matters most.

```html
<section class="slide s-bullets">
  <header class="head">
    <p class="kicker">{{KICKER}}</p>
    <h2 class="title">{{TITLE}}</h2>
  </header>
  <ul class="bullets">
    <li><b>{{POINT_1}}</b> <span>{{DETAIL_1}}</span></li>
    <li><b>{{POINT_2}}</b> <span>{{DETAIL_2}}</span></li>
    <li><b>{{POINT_3}}</b> <span>{{DETAIL_3}}</span></li>
    <li><b>{{POINT_4}}</b> <span>{{DETAIL_4}}</span></li>
  </ul>
</section>
```

## 5. Two columns

**Class:** `s-two-col`
**Use for:** a comparison (before and after, option A and B, today and tomorrow) or two halves of one answer.
**Rules:** both columns have the same structure. Three list items max per column. The accent (`col accent`) goes on the recommended or future side.

```html
<section class="slide s-two-col">
  <header class="head">
    <p class="kicker">{{KICKER}}</p>
    <h2 class="title">{{TITLE}}</h2>
  </header>
  <div class="cols">
    <div class="col">
      <p class="label">{{LEFT_LABEL}}</p>
      <h3>{{LEFT_TITLE}}</h3>
      <p>{{LEFT_TEXT}}</p>
      <ul><li>{{LEFT_ITEM_1}}</li><li>{{LEFT_ITEM_2}}</li><li>{{LEFT_ITEM_3}}</li></ul>
    </div>
    <div class="col accent">
      <p class="label">{{RIGHT_LABEL}}</p>
      <h3>{{RIGHT_TITLE}}</h3>
      <p>{{RIGHT_TEXT}}</p>
      <ul><li>{{RIGHT_ITEM_1}}</li><li>{{RIGHT_ITEM_2}}</li><li>{{RIGHT_ITEM_3}}</li></ul>
    </div>
  </div>
</section>
```

## 6. Three cards

**Class:** `s-cards`
**Use for:** three options, pillars, offers or principles of equal weight.
**Rules:** exactly three cards (two or four also fit, never more). Card title of one to four words, text of two short sentences. The accent card is the one you recommend; move `accent` or remove it.

```html
<section class="slide s-cards">
  <header class="head">
    <p class="kicker">{{KICKER}}</p>
    <h2 class="title">{{TITLE}}</h2>
  </header>
  <div class="cards">
    <div class="card">
      <p class="label">{{CARD_1_LABEL}}</p>
      <h3>{{CARD_1_TITLE}}</h3>
      <p>{{CARD_1_TEXT}}</p>
    </div>
    <div class="card accent">
      <p class="label">{{CARD_2_LABEL}}</p>
      <h3>{{CARD_2_TITLE}}</h3>
      <p>{{CARD_2_TEXT}}</p>
    </div>
    <div class="card">
      <p class="label">{{CARD_3_LABEL}}</p>
      <h3>{{CARD_3_TITLE}}</h3>
      <p>{{CARD_3_TEXT}}</p>
    </div>
  </div>
</section>
```

## 7. Big numbers

**Class:** `s-numbers`
**Use for:** one to three figures that prove the point.
**Rules:** five characters max per number (`87%`, `3.2x`, `12k`, `48h`). Each label says what the number measures and over what period. Every figure needs a real source: never invent one. The accent bar goes on the number that matters most.

```html
<section class="slide s-numbers">
  <header class="head">
    <p class="kicker">{{KICKER}}</p>
    <h2 class="title">{{TITLE}}</h2>
  </header>
  <div class="stats">
    <div class="stat accent"><span class="num">{{NUMBER_1}}</span><p>{{LABEL_1}}</p></div>
    <div class="stat"><span class="num">{{NUMBER_2}}</span><p>{{LABEL_2}}</p></div>
    <div class="stat"><span class="num">{{NUMBER_3}}</span><p>{{LABEL_3}}</p></div>
  </div>
</section>
```

## 8. Quote

**Class:** `s-quote`
**Use for:** a customer, employee or expert voice that says it better than you.
**Rules:** 35 words max, real words from a real person, with name and role. The quotation mark is the accent.

```html
<section class="slide s-quote">
  <figure class="quote">
    <span class="qmark accent" aria-hidden="true">&ldquo;</span>
    <blockquote>{{QUOTE}}</blockquote>
    <figcaption><b>{{NAME}}</b>{{ROLE_AND_COMPANY}}</figcaption>
  </figure>
</section>
```

## 9. Image and text

**Class:** `s-image`
**Use for:** a product screen, a place, a team, a photo that carries the message, next to a short text.
**Rules:** one image per slide, a local file (`img/name.jpg`) or `src=""` for the placeholder. The image is cropped to fill its half: keep the subject centred. Add `reverse` to `split` to put the image on the left.

```html
<section class="slide s-image">
  <div class="split">
    <div class="text">
      <p class="kicker">{{KICKER}}</p>
      <h2 class="title">{{TITLE}}</h2>
      <p class="lead">{{TEXT}}</p>
    </div>
    <figure class="media"><img src="{{IMAGE}}" alt="{{IMAGE_ALT}}"></figure>
  </div>
</section>
```

## 10. Steps

**Class:** `s-steps`
**Use for:** a process, a timeline, a roadmap, a method: three to five steps in order.
**Rules:** three to five steps, all with the same structure. Label = when or which step (`Week 1`, `Step 2`). The accent dot marks where we are now, or the step that matters most.

```html
<section class="slide s-steps">
  <header class="head">
    <p class="kicker">{{KICKER}}</p>
    <h2 class="title">{{TITLE}}</h2>
  </header>
  <ol class="steps">
    <li class="step"><p class="label">{{STEP_1_LABEL}}</p><h3>{{STEP_1_TITLE}}</h3><p>{{STEP_1_TEXT}}</p></li>
    <li class="step accent"><p class="label">{{STEP_2_LABEL}}</p><h3>{{STEP_2_TITLE}}</h3><p>{{STEP_2_TEXT}}</p></li>
    <li class="step"><p class="label">{{STEP_3_LABEL}}</p><h3>{{STEP_3_TITLE}}</h3><p>{{STEP_3_TEXT}}</p></li>
    <li class="step"><p class="label">{{STEP_4_LABEL}}</p><h3>{{STEP_4_TITLE}}</h3><p>{{STEP_4_TEXT}}</p></li>
  </ol>
</section>
```

## 11. Table

**Class:** `s-table`
**Use for:** a small comparison grid: options against criteria, plan against budget.
**Rules:** five columns and six rows max, short cells (a word, a number, a short phrase). Numbers get `class="n"` (right aligned). The accent row is the recommended option; move it or remove it.

```html
<section class="slide s-table">
  <header class="head">
    <p class="kicker">{{KICKER}}</p>
    <h2 class="title">{{TITLE}}</h2>
  </header>
  <table class="table">
    <thead><tr><th>{{COL_1}}</th><th>{{COL_2}}</th><th>{{COL_3}}</th><th class="n">{{COL_4}}</th></tr></thead>
    <tbody>
      <tr><td>{{ROW_1}}</td><td>{{CELL}}</td><td>{{CELL}}</td><td class="n">{{VALUE}}</td></tr>
      <tr class="accent"><td>{{ROW_2}}</td><td>{{CELL}}</td><td>{{CELL}}</td><td class="n">{{VALUE}}</td></tr>
      <tr><td>{{ROW_3}}</td><td>{{CELL}}</td><td>{{CELL}}</td><td class="n">{{VALUE}}</td></tr>
    </tbody>
  </table>
</section>
```

## 12. Closing

**Class:** `s-closing`
**Use for:** the last slide: the next step and how to reach you.
**Rules:** the title is the next step or a thank you, never "Questions?" alone. One call to action (the accent button). Two or three contact entries; remove the ones you do not have.

```html
<section class="slide s-closing">
  <img class="brand-logo" src="{{LOGO}}" alt="{{COMPANY}}">
  <h2 class="title">{{CLOSING_TITLE}}</h2>
  <p class="lead">{{CLOSING_TEXT}}</p>
  <a class="cta accent" href="{{CTA_URL}}">{{CTA_LABEL}}</a>
  <div class="contact">
    <div><span class="label">{{CONTACT_1_LABEL}}</span>{{CONTACT_1}}</div>
    <div><span class="label">{{CONTACT_2_LABEL}}</span>{{CONTACT_2}}</div>
    <div><span class="label">{{CONTACT_3_LABEL}}</span>{{CONTACT_3}}</div>
  </div>
</section>
```

## Choosing a layout

| The slide says... | Layout |
|---|---|
| "Here is who we are and what this is about" | Cover |
| "Now, part two" | Section divider |
| "Remember this one thing" | Statement |
| "There are four reasons" | Bullets |
| "Before, after" / "Option A, option B" | Two columns |
| "Three ways to do it" | Three cards |
| "The numbers prove it" | Big numbers |
| "Here is what a customer said" | Quote |
| "Look at this" | Image and text |
| "This is how it unfolds" | Steps |
| "Here is how the options compare" | Table |
| "Here is what happens next" | Closing |

If no layout fits, split the content into two slides that do fit before inventing a new one. A new layout goes in the deck's own `<style>` block, after the chassis CSS, uses only the tokens, and follows the global rules above.
