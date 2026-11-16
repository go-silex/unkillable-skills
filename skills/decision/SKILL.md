---
name: decision
description: Logs an important decision in the second brain, one note per subject (for example "Price of offer X"), with the current decision on top and a dated history below, so a decision that changes several times stays in one place. Adds one line to the decisions log and the memory. Use when the user says "decision", "on a décidé", "log cette décision", "consigne ce choix", "we decided", "record this decision".
---

# Decision

Keep the memory of important choices, simply. Talk in the user's language; content in the language `AGENTS.md` sets.

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states.

- Paths from its `## Brain map`: Decisions, Memory. For a role missing from the map only: `00_COCKPIT/Decisions/`, `_System/MEMORY.md`.
- The Decisions folder's `README.md` or `AGENTS.md`, and a `Decision.md` in the Templates folder, win over the format below.

## Is it a decision?

Log it only if it changes direction, money, people, a commitment to someone outside, or would be costly to undo. "Send the email to Michel" is a task: say so and offer `capture`. Something only said or still open is not decided: write "said on <date>" where it belongs.

## One note per subject

A decision is filed under its **subject**, not its date: `Price_Offer_X.md`, `Felix_Role.md`, `Weekly_Review_Day.md`. When the subject comes back, the same note is updated:

- `## Current` is rewritten: what holds today, and why in one or two lines.
- `## History` gets one dated line on top. History is never rewritten.

So one note shows the decision in force and every change before it. A new note only for a new subject.

```markdown
---
type: decision
status: active
area: <a company, a stream, a project>
updated: YYYY-MM-DD
---

# <Subject>

## Current
<what is decided>. Why: <one or two lines>. (<source, date>)

## History
- YYYY-MM-DD · <what was decided> · <why, source>
```

`status: replaced` when the subject itself is closed or merged into another note (link it).

## Steps

1. Find the decision: the user's words after the command, or what was decided in this conversation. Unclear: ask "Which decision do you want to log?".
2. Find the subject: search the Decisions folder and `Decisions_Log.md` for an existing note on it (same subject, other wording).
3. Missing reason: ask only "Why?", once. No answer: write "not stated".
4. Update the existing note (rewrite `Current`, add a `History` line, set `updated`), or create it.
5. Add a line at the top of the current year in `<Decisions>/Decisions_Log.md` (create it with `# Decisions log` and a `## YYYY` heading if missing): `- YYYY-MM-DD · <area> · <decision> ([[note]])`. The log gets a line at every change: it is the chronological view.
6. Add a line to `## Recent decisions` in the Memory (keep the 10 most recent).
7. Link related notes (project, person) with `[[links]]`. Confirm in one line.

## Rules

- Never invent a reason. A decision the user did not confirm is never logged.
- File names follow the brain's convention, without a date: the subject is the name.
