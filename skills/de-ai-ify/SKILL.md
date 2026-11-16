---
name: de-ai-ify
description: Removes the patterns that make a text sound AI-written and restores a human voice, without changing what it says. Runs after writing, on a post, newsletter, email, script, web page, chat message or meeting summary. Use when the user says "de-ai-ify", "humanize", "ça sent l'IA", "rends ça humain", "enlève le slop", "passe ce texte au filtre", "make it sound human".
---

# De-AI-ify

The text is already written. Remove what gives the machine away, keep the substance. Work in the text's language. Do not use this skill to write a text: it runs after, on a text pasted, given as an argument, or pointed to by a path.

## Input

- Pasted text: return the corrected version in the chat, in the same format (a post stays a post, an email an email, a chat message keeps its bullets if they help reading).
- A file path: read it fully, write the corrected version next to it with the suffix `-HUMAN` (`Note.md` becomes `Note-HUMAN.md`). Never overwrite the original.
- If the brain has a **Voice** file (role Voice in the `## Brain map` of the root `AGENTS.md`), read it: the result must sound like that person, not like a generic human.

## What to remove

- **Stock transitions**: "Moreover", "Furthermore", "In addition", "However" at every turn; « De plus », « Par ailleurs », « En outre », « Néanmoins », and the overuse of « Cependant », « Toutefois ». "Although X, Y" as a systematic opener.
- **Clichés**: "In today's fast-paced world", "unlock the potential", "game-changer"; « Dans un monde en constante évolution », « Force est de constater », « Exploiter le potentiel de », « Tirer parti de ».
- **Filler**: "It is important to note that", « Il convient de souligner », « En effet » as a crutch, quantifiers that count nothing ("various", "numerous", « divers », « nombreux », « multiples »).
- **Corporate jargon**: optimize → improve, implement → set up, leverage → use, synergy → the actual link, scalable → can grow. In French: optimiser → améliorer, implémenter → mettre en place, capitaliser sur → utiliser.
- **Robot patterns**: a rhetorical question answered right away; obsessive parallel structures; lists that always have three items; announcing what you are about to say; a conclusion that repeats the paragraph.
- **Typography**: the em dash used as a stylish comma (replace with a comma, a colon or a full stop), "Not only X but also Y", bold on whole sentences, exclamation marks on empty sentences.

## What to bring back

Varied sentence length: four words after a long sentence carry more than a regular paragraph. A spoken tone. Direct statements, no "it seems that". Precise examples instead of general formulas. Natural transitions, or none. When a story, a number or a real case is buried under an abstract sentence, bring it forward.

## Method

1. Read the whole text and find **the main tell** first: often one thing (uniform bullets, three symmetrical subheads, an announcement paragraph) carries most of the AI effect. Fix that first.
2. Go pattern by pattern, without softening the substance.
3. Read it as if aloud. What nobody would say out loud does not stay.

## Output, always in this order

1. **The corrected text.**
2. **Changes**: one line per change, naming the pattern ("seven bullets of equal length turned into one paragraph"), not the feeling.
3. **What is missing**: places where a concrete example, number or name would make the text better, that you cannot invent.

## Rules

- **Never change the substance.** A missing fact is flagged, never filled. Numbers, dates, names, prices and commitments stay exactly as they are.
- **A text that already sounds human stays as it is.** Say "nothing to change" rather than rewriting to justify the skill.
- **Same format out as in.** No post turned into a note, no chat message turned into a document.
- **The author's voice, not yours.**
- **No em dash**, even while rewriting.

## Examples

**Before:** « Dans un monde où l'intelligence artificielle ne cesse de se développer, il est crucial de comprendre que tirer parti de l'IA de manière efficace ne se résume pas à utiliser la technologie la plus avancée. »
**After:** « L'IA marche mieux quand tu l'utilises pour des tâches précises : écrire du code, analyser des données, répondre à des questions. »

**Before:** "It is important to note that, moreover, numerous companies have implemented innovative solutions in order to optimize their processes."
**After:** "Plenty of companies have done it already. Most simplified their processes before adding anything."

**Before:** « Une facture est rattachée à la période de la prestation, et non à sa date d'émission. »
**After:** « Une facture va dans le mois de la prestation : le travail de mars va dans mars, même si la facture part en avril. »
