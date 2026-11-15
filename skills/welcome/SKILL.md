---
name: welcome
description: Start-of-session briefing for the second brain. Reads the journal, memory and inbox, then says where things stand, what is waiting and what to do first. Use at the start of a work session or when the user says "welcome", "briefing", "on reprend", "où on en est", "start the session", "what's on my plate".
---

# Welcome: start of session

Give the user a short briefing so the session starts from where the last one stopped. Answer in the user's language. Read only; write nothing.

## Find the folders

Read the `## Brain map` table in the root `AGENTS.md` (or `CLAUDE.md`). If there is none, use the first that exists: Inbox `00_IMPORT/` or `Inbox/`; Journal `00_COCKPIT/Journal.md`; Memory `_System/MEMORY.md`; Context `_System/Contexte_Global.md` or `_System/Context.md`. If none of these exist, say so in one line and suggest `brain-setup`.

## Read

1. Context: skim it for the user's first name, business and current priorities.
2. Memory: `Where things stand` and `Next steps`.
3. Journal: the two most recent entries, and any unchecked `- [ ]` in them.
4. Inbox: count the files (ignore hidden files and `README`).
5. Recent activity: notes modified in the last 7 days (count, and the 3 most recent titles).

## Briefing

```
Hi <first name>, <weekday, date>.

Last time
- <what the last journal entry says was done, in 1-2 lines>

Waiting for you
- <unchecked next steps from the journal or memory, at most 3>

State
- Inbox: <n> items
- Last 7 days: <n> notes touched

Suggestion
- <one concrete first move>
```

## Suggestion, pick one

- Inbox above 5 items: process it with `inbox`.
- Friday, or no weekly review in the last 7 days: `weekly-review`.
- An unchecked next step exists: start with the oldest one.
- Inbox empty and nothing pending: ask what the session is about.

## Style

Short lines, no filler, no flattery. If a file is missing, say what is missing instead of guessing.
