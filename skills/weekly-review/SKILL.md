---
name: weekly-review
description: Weekly review of the business and the second brain. Says what moved, what is stuck, what is drifting, sets next week's priorities, then offers a hygiene pass (inbox, memory, missing links, sources of truth). Use on the review day set in the brain, or when the user says "weekly review", "revue de la semaine", "bilan de la semaine", "endweek", "plan next week".
---

# Weekly review

Step back on the week, leader to leader, then keep the brain clean. Talk in the user's language; content in the language `AGENTS.md` sets.

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states (review day, folders, confidentiality).

- Paths from its `## Brain map`: Cockpit, Journal, Memory, Context, Decisions, Inbox. For a role missing from the map only: `00_COCKPIT/`, `00_COCKPIT/Journal.md`, `_System/MEMORY.md`, `_System/Context.md`, `00_COCKPIT/Decisions/`, `00_IMPORT/`.
- Reviews go to `<Cockpit>/Reviews/` unless `AGENTS.md` names another place. If the Templates folder holds `Weekly_Review.md`, use it.
- No review day set in `AGENTS.md`: after the first review, ask which day suits the user and offer to write it in `AGENTS.md`.

## Part 1: the business review

1. Read Context (priorities) and Memory (where things stand).
2. Read the journal entries of the last 7 days, the decisions log of the week, and the notes modified in the last 7 days. Read the notes, not only their titles.
3. If a calendar is connected and listed as a source of truth: the week's meetings, and next week's big ones.
4. Find: what really moved, what is stuck and why, what drifts without anyone looking.

Write `<Reviews>/YYYY-Www.md` (add to it if it exists):

```markdown
---
type: review
created: YYYY-MM-DD
---

# Week Www review · YYYY-MM-DD

## What moved
- <facts, not impressions>

## What is stuck
- <the block, and what it takes to unblock it>

## Blind spot
- <what drifts or is being avoided>

## Next week's priorities
1. <the one thing that matters most, and why now>
2.
3.
```

Then three lines in the chat: the verdict of the week and priority number one. Sober and honest: if something is wrong, say it.

## Part 2: hygiene pass (ask first)

Ask: "Shall I do the hygiene pass?" If yes:

1. Inbox not empty: process it with the `inbox` method (plan, yes, file).
2. Memory: refresh `Where things stand`, `Next steps`, `Recent decisions`; prune what is stale.
3. Links: find 3 to 5 recent notes with no `[[link]]` and connect them.
4. Sources: a tool used this week that is not in the sources-of-truth table: suggest `connect`.
5. Folder instructions: a folder that changed a lot gets a proposed update to its `AGENTS.md` or `README.md`.
6. Context: something structural changed (offer, big project, pivot): propose the change, wait for a yes.

Add a line at the end of the review: `Hygiene: <n> notes filed, <n> links, memory updated`.

## Rules

- No flattery, no invented facts. A week with little progress is reported as such.
