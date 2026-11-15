---
name: weekly-review
description: Weekly review of the business and the second brain. Says what moved, what is stuck, what is drifting, sets next week's priorities, then offers a hygiene pass (inbox, memory, missing links). Use on Fridays or when the user says "weekly review", "revue de la semaine", "bilan de la semaine", "endweek", "plan next week".
---

# Weekly review

Step back on the week, leader to leader, then keep the brain clean. Answer in the user's language.

## Find the folders

`## Brain map` in the root `AGENTS.md` (or `CLAUDE.md`). If there is none: Cockpit `00_COCKPIT/`, Journal `00_COCKPIT/Journal.md`, Memory `_System/MEMORY.md`, Context `_System/Contexte_Global.md` or `_System/Context.md`, Inbox `00_IMPORT/`.

## Part 1: the business review

1. Read Context (goals, priorities) and Memory (where things stand).
2. Read the journal entries of the last 7 days, the decisions of the week, and the notes modified in the last 7 days. Read the notes, not only their titles.
3. Find: what really moved, what is stuck and why, what drifts without anyone looking.

Write `<Cockpit>/Reviews/YYYY-Www.md` (create `Reviews/` if needed; if the file exists, add to it):

```markdown
# Week Www review - YYYY-MM-DD

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

1. Inbox not empty: process it (same method as the `inbox` skill).
2. Memory: refresh `Where things stand`, `Next steps`, `Recent decisions`; prune what is stale.
3. Links: find 3 to 5 recent notes with no `[[link]]` and connect them.
4. Folder instructions: if a folder changed a lot, propose an update to its `AGENTS.md`/`CLAUDE.md`.
5. Context: if something structural changed (offer, big project, pivot), propose the change and wait for a yes before editing it.

Add a line at the end of the review file: `Hygiene: <n> notes filed, <n> links, memory updated`.

## Rules

- No flattery, no invented facts. A week with little progress is reported as such.
