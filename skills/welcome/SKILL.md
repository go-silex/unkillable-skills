---
name: welcome
description: Start-of-session briefing for the second brain. Reads the journal, memory and inbox, plus the connected tools listed as sources of truth (calendar, mail, chat, CRM), then says where things stand, what is waiting and what to do first. Use at the start of a work session or when the user says "welcome", "briefing", "on reprend", "où on en est", "start the session", "what's on my plate".
---

# Welcome: start of session

A short briefing so the session starts where the last one stopped. Read only: write nothing, send nothing. Talk in the user's language.

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states (paths, ritual days, confidentiality).

- Paths come from its `## Brain map`. For a role missing from the map only: Inbox `00_IMPORT/`, Journal `00_COCKPIT/Journal.md`, Memory `_System/MEMORY.md`, Context `_System/Context.md`. If nothing is found, say so in one line and suggest `brain-check`.
- External sources come from its sources-of-truth table (heading containing "truth" or "Sources").

## Read the brain

1. Context: the user's first name, business, current priorities.
2. Memory: `Where things stand` and `Next steps`.
3. Journal: the two most recent entries, and any unchecked `- [ ]` in them. Note the date of the last entry: it is "since last time".
4. Inbox: count the items (ignore hidden files and `README`).
5. Cockpit: an interview in progress (`Interview_Progress.md` with days not done).

## Read the connected sources

For each tool in the sources table that has a connector available in this session, read what is time-sensitive since last time. At most 3 items per source, most important first.

| Kind of tool | What to read |
|---|---|
| Calendar | today's meetings (and tomorrow's first one), with the person notes that exist for the attendees |
| Mail | threads waiting for the user's reply, from people or companies the brain knows |
| Chat | direct messages and mentions not answered |
| CRM, task tool | items due today or overdue, assigned to the user |

- Respect the confidentiality rules of `AGENTS.md` (an account the brain must not read stays unread).
- A source that fails or has no connector: one line, "Gmail (second account): not connected here". Never guess its content.
- A connected tool missing from the sources table: one line suggesting `connect`.

## Briefing

```
Hi <first name>, <weekday, date>.

Last time
- <what the last journal entry says was done, 1-2 lines>

Today
- <meetings, with a person note link when one exists>

Waiting for you
- <next steps from journal or memory, replies owed, due items: at most 5>

State
- Inbox: <n> items · last 7 days: <n> notes touched

Suggestion
- <one concrete first move>
```

Omit a block with nothing in it. Keep it readable on a phone.

## Suggestion, pick one

- A meeting within 2 hours with someone whose person note is thin or older than 30 days: refresh it with `person`.
- Interview in progress and today's theme not done: `interview`.
- Inbox above 5 items: `inbox`.
- Review day set in `AGENTS.md` is today, or no review in the last 7 days: `weekly-review`.
- An unchecked next step exists: start with the oldest one.
- Otherwise: ask what the session is about.

## Style

Short lines, no filler, no flattery. A missing file is named, never guessed.
