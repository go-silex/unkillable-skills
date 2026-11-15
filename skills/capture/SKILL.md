---
name: capture
description: Drops an idea, a note, a task or a link into the second brain's inbox in seconds, without deciding where it goes. Use when the user says "capture", "note ça", "garde ça", "jette ça dans l'inbox", "remind me", "save this idea", or dictates a raw thought to keep.
---

# Capture

The user throws a raw thought (often dictated). Drop it cleanly into the inbox. Filing comes later with `inbox`. Speed first.

## Find the inbox

`## Brain map` in the root `AGENTS.md` (or `CLAUDE.md`), role Inbox. If there is none: `00_IMPORT/`, then `Inbox/`. If neither exists, create `00_IMPORT/` and say so.

## Steps

1. The text to capture is what the user wrote after the command. If empty, ask "What do you want to capture?" and wait.
2. Clean it lightly: fix dictation errors, keep the user's words, add nothing.
3. Detect the kind (idea, task, note, contact, link) and write a short clear title.
4. Write `<Inbox>/YYYY-MM-DD-<short-title>.md`:

```markdown
---
type: capture
created: YYYY-MM-DD
---

# <title>

<cleaned content>

- [ ] <only if it is a task>
```

5. If an existing note is an obvious match, add one `[[link]]`. Do not search hard.
6. Confirm in one line, in the user's language: "Captured in <Inbox>: <title>." No follow-up discussion.

## Rules

- No questions unless the input is empty.
- Never file outside the inbox: that is the job of `inbox`.
- File names: no accents, no spaces (use `-`).
