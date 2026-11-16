---
name: capture
description: Drops an idea, a note, a task, a contact or a link into the second brain's inbox in seconds, without deciding where it goes, with the useful metadata (kind, source, people, due date) so the inbox can file it later. Use when the user says "capture", "note ça", "garde ça", "jette ça dans l'inbox", "remind me", "save this idea", or dictates a raw thought to keep.
---

# Capture

The user throws a raw thought, often dictated. Drop it cleanly into the inbox, with enough metadata that `inbox` can file it without asking again. Speed first: no questions unless the input is empty.

## Find your way

- Inbox path: `## Brain map` of the root `AGENTS.md`, role Inbox. If the map has no Inbox: `00_IMPORT/` (create it and say so).
- If the Templates folder holds `Capture.md`, follow it instead of the format below.
- File name and content language: what `AGENTS.md` says wins. Default name `YYYY-MM-DD_Short_Title.md`, no accents, no spaces.

## Steps

1. The text is what the user wrote after the command. If empty, ask "What do you want to capture?" and wait.
2. Clean it lightly: fix dictation errors, keep the user's words, add nothing. Keep the original wording of quotes.
3. Read only what the text makes obvious, never guess:
   - `kind`: idea, task, note, contact, link, meeting, decision (a decision captured here is still to confirm).
   - `source`: dictation, chat, email, meeting, url, photo. A URL goes in `source` as is.
   - `people`: names mentioned. Check the People folder by file name only: link `[[Firstname_Lastname]]` when a note exists, plain name otherwise.
   - `related`: a project, client or concept named in the text, linked if a note with that exact name exists.
   - `due`: only if a date or deadline is stated (`YYYY-MM-DD`).
4. Write `<Inbox>/YYYY-MM-DD_Short_Title.md`:

```markdown
---
type: capture
created: YYYY-MM-DD
kind: idea
source: dictation
people: ["[[Firstname_Lastname]]"]
related: []
due:
status: to-file
---

# <short, clear title>

<cleaned content>

- [ ] <only if it is a task>
```

Leave out a field with nothing in it, except `type`, `created` and `status`.

5. Confirm in one line, in the user's language: "Captured in <Inbox>: <title>." No follow-up discussion.

## Rules

- Capture writes to the inbox only. Filing is the job of `inbox`.
- A long dump with several topics: one capture per topic, same timestamp, then one line listing them.
