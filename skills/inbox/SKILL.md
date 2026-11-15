---
name: inbox
description: Processes the second brain's inbox. Reads every captured note, files it in the right folder with a clean title, frontmatter and links, merges duplicates, and leaves the inbox empty. Use when the user says "inbox", "inbox processor", "triage", "vide l'inbox", "range l'inbox", "process my inbox", "clean up captures".
---

# Inbox: empty the inbox

File every captured item in the right place, linked, so the brain does not rot. Answer in the user's language.

## Find the folders

`## Brain map` in the root `AGENTS.md` (or `CLAUDE.md`). If there is none, the inbox is `00_IMPORT/` or `Inbox/`. To learn where things go, read the root `AGENTS.md`/`CLAUDE.md` and the `AGENTS.md`/`CLAUDE.md` inside each main folder. Do not guess a destination.

## Steps

1. List everything in the inbox (ignore hidden files and the inbox's own `README`).
2. For each item, read it fully, then decide:
   - **Destination folder**: the folder whose instructions describe this kind of note.
   - **Title**: improve it if vague. File names: no accents, no spaces.
   - **Frontmatter**: set `type` to what the note has become (see below); set `created: YYYY-MM-DD` (rename an existing `date:` to `created:`); never fill a field you do not know.
   - **Links**: add `[[links]]` to existing related notes (people, projects, clients). Search titles for real.
   - **Duplicate** of an existing note: merge into it instead of creating a second one.
   - **Pure task**: add it as `- [ ]` to the project note or the cockpit, and drop the capture.
   - **Information about a person**: also update that person's note (see the `person` skill), or create it.
3. Too thin or unclassifiable, or no folder fits: leave it in the inbox untouched (it keeps `type: capture`), say why, and suggest where it could go.

## Type after filing

`type: capture` is temporary. A note leaving the inbox never keeps it.

| The note is | `type` |
|---|---|
| A meeting or call summary | `meeting` |
| An idea or a piece of work to carry | `project` |
| A choice that was made | `decision` |
| A reusable way of doing things | `process` |
| An article, PDF or reading (add `source:` with the URL or origin) | `source` |
| A lasting reference or template | `reference` |
| A person | `person` |

If the brain has its own conventions file (for example `_System/Conventions_Frontmatter.md`), it wins over this table.

## Before acting

- More than 5 items with a doubtful destination: show the plan (title, destination, type) and ask for a yes.
- Otherwise act, then report.

## End check

No note outside the inbox should still have `type: capture`. Fix any you meet and say so.

## Report

- <n> filed: title, destination, type (one line each)
- <n> links created
- <n> left in the inbox, and why

## Rules

- Never delete anything without an explicit yes. A merged capture goes to the brain's archive or trash folder if there is one; otherwise ask.
- Never change the content's meaning while cleaning it.
