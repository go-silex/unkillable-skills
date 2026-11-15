---
name: save-context
description: Turns the current conversation into a self-contained context document saved in the second brain, so a new conversation, another AI tool or a colleague can pick up the work with zero prior context. Use when the user says "save context", "sauvegarde le contexte", "passation", "résume pour reprendre plus tard", "handover", "I'll continue in another chat".
---

# Save context

Write a handover document that stands on its own. Answer and write in the user's language.

## Where it goes

`## Brain map` in the root `AGENTS.md` (or `CLAUDE.md`), role Cockpit. If there is none: `00_COCKPIT/`. File: `<Cockpit>/Context/YYYY-MM-DD-<short-title>.md` (create `Context/` if needed).

## 1. Compact the conversation

Keep what lasts, drop the chatter:

- Goal: what we are trying to achieve, and for whom.
- What was built or decided, and why.
- Exact references: files as `[[wikilinks]]`, URLs, tools, commands.
- Where secrets live (for example "API key in the password manager, item X"). **Never the values.**
- Open questions, next steps, traps met on the way.
- Preferences and conventions that matter for this topic.

Then check: what would someone starting from zero miss? Fill that gap.

## 2. Write it

```markdown
---
type: reference
created: YYYY-MM-DD
tags: [context]
---

# <short, explicit title>

**TL;DR**: <2-3 lines>

## Goal
## Where things stand
## Decisions and why
## References
## Next steps
- [ ] ...
## Traps
```

Omit an empty section. No "as said above": every line reads on its own.

## 3. Close

- Add a line to `## Where things stand` in the Memory pointing to the new note.
- Reply with the path and one sentence the user can paste into a new conversation: "Read `<path>` and continue from there."

## Rules

- Never copy a password, token or key into the note.
- Facts from this conversation only. Mark anything uncertain as such.
