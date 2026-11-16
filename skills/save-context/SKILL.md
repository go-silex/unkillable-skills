---
name: save-context
description: Turns the current conversation into a self-contained context document saved in the second brain, so a new conversation, another AI tool or a colleague can pick up the work with zero prior context. Use when the user says "save context", "sauvegarde le contexte", "passation", "résume pour reprendre plus tard", "handover", "I'll continue in another chat".
---

# Save context

Write a handover document that stands on its own. Talk in the user's language; content in the language `AGENTS.md` sets.

## Find your way

- Path: `## Brain map` of the root `AGENTS.md`, role Cockpit (default `00_COCKPIT/` only if the map has none). File: `<Cockpit>/Context/YYYY-MM-DD_Short_Title.md`, or the brain's naming convention. Create `Context/` if needed.
- If the Templates folder holds `Context.md` or `Handover.md`, use it instead of the format below.
- If the work belongs to a project or client folder that has its own `AGENTS.md`, ask whether the document should live there instead.

## 1. Compact the conversation

Keep what lasts, drop the chatter:

- Goal: what we are trying to achieve, and for whom.
- What was built or decided, and why.
- Exact references: files as `[[wikilinks]]`, URLs, tools, commands.
- Where secrets live ("API key in the password manager, item X"). **Never the values.**
- Open questions, next steps, traps met on the way.
- Preferences and conventions that matter for this topic.

Then check: what would someone starting from zero miss? Fill that gap.

## 2. Write it

```markdown
---
type: reference
created: YYYY-MM-DD
source: session YYYY-MM-DD
related: []
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
