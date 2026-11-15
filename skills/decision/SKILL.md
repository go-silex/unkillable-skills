---
name: decision
description: Logs a decision in the second brain with its context, the options on the table, the choice, the reason and what would make it worth revisiting. Use when the user says "decision", "on a décidé", "log cette décision", "consigne ce choix", "we decided", "record this decision".
---

# Decision

Keep the memory of choices, so nobody has to rebuild the reasoning later. Answer in the user's language.

## Find the folders

`## Brain map` in the root `AGENTS.md` (or `CLAUDE.md`). If there is none: Decisions `00_COCKPIT/Decisions/` (create it if missing), Memory `_System/MEMORY.md`, Context `_System/Contexte_Global.md` or `_System/Context.md`. If the brain has a decision template (for example `_System/Templates/Decision.md`), follow it.

## Steps

1. The decision is what the user wrote after the command, or what was decided in this conversation. If unclear, ask "Which decision do you want to log?" and wait.
2. Ask only for what is missing, in one message: the other options considered, why this one, what would make you revisit it.
3. Write `<Decisions>/YYYY-MM-DD-<short-title>.md`:

```markdown
---
type: decision
created: YYYY-MM-DD
status: active
---

# Decision: <title>

## Context
<the situation that forced the choice>

## Options considered
- <option A>: <for / against>
- <option B>: <for / against>

## Choice
<what was decided>

## Why
<the reasoning and the assumptions>

## Revisit if
<what would make us reconsider>
```

4. Link it to related notes (project, client, person) with `[[links]]`.
5. Add one line to `## Recent decisions` in the Memory: `- YYYY-MM-DD: <decision> ([[note]])`.
6. Confirm in one line.

## Rules

- Never invent an option or a reason the user did not give. Leave a section with "not stated" rather than filling it.
- A decision that replaces an older one: set the old note's `status: superseded` and link both.
