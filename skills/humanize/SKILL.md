---
name: humanize
description: Removes the patterns that make a text sound AI-written and restores a human voice, without changing what it says. For a post, newsletter, email, script, web page or meeting summary written or co-written with AI. Use when the user says "humanize", "de-ai-ify", "ça sent l'IA", "rends ça humain", "enlève le slop", "make it sound human".
---

# Humanize

The text is already written. Remove what gives the machine away, keep the substance. Work in the text's language.

## Input

- Pasted text: return the corrected version in the chat, in the same format (a post stays a post, an email stays an email).
- A file path: read it fully, write the corrected version next to it with the suffix `-human` (`Note.md` becomes `Note-human.md`). Never overwrite the original.

## What to remove

- **Stock transitions**: "Moreover", "Furthermore", "In addition", "However" at every turn; in French "De plus", "Par ailleurs", "En outre", "Néanmoins".
- **Clichés**: "In today's fast-paced world", "unlock the potential", "leverage", "game-changer"; "Dans un monde en constante évolution", "Force est de constater", "Tirer parti de".
- **Filler**: "It is important to note that", "Il convient de souligner", vague quantifiers ("various", "numerous", "divers", "nombreux").
- **Corporate jargon**: optimize, implement, synergy, scalable, when a plain word exists.
- **Robot patterns**: a rhetorical question answered right away; lists that always have three items; announcing what you are about to say; a conclusion that repeats the paragraph; parallel structures in every sentence.
- **Typography**: em dashes used as stylish commas (replace with a comma, a colon or a full stop), "Not only X but also Y", bold on whole sentences, exclamation marks on empty sentences.

## What to bring back

Sentences of varied length. A spoken tone. Direct statements, no "it seems that". Precise examples instead of general formulas. Natural transitions, or none. If a concrete story, number or case is buried under an abstract sentence, bring it forward.

## Method

1. Read the whole text and find **the main tell** first: often one thing (uniform bullets, three symmetrical subheads, an announcement paragraph) carries most of the AI effect. Fix that first.
2. Go through the patterns one by one, without softening the substance.
3. Read it as if aloud. What nobody would say out loud does not stay.

## Output, always in this order

1. **The corrected text.**
2. **Changes**: one line per change, naming the pattern ("seven bullets of equal length turned into one paragraph").
3. **What is missing**: places where a concrete example, number or name would make the text better, that you cannot invent.

## Rules

- **Never change the substance.** A missing fact is flagged, never filled. Numbers, dates, names, prices and commitments stay exactly as they are.
- **A text that already sounds human stays as it is.** Say "nothing to change" rather than rewriting to justify yourself.
- Keep the author's voice, not yours.
