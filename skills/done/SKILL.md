---
name: done
description: End-of-session log for the second brain. Writes what was done, decided and what comes next at the top of the journal, and updates the memory so the next session (or another AI tool) picks up without losing anything. Use when the user says "done", "on clôture", "fin de session", "log la session", "wrap up", "close the session".
---

# Done: end of session

Leave a clean trace of this session in the brain. Local only: nothing is sent anywhere. Answer in the user's language.

## Find the folders

Read the `## Brain map` table in the root `AGENTS.md` (or `CLAUDE.md`). If there is none: Journal `00_COCKPIT/Journal.md`, Memory `_System/MEMORY.md`, Inbox `00_IMPORT/`. If the journal file does not exist, create it with the header `# Journal`.

## 1. Sum up the session

Go through the conversation and keep only what lasts:

- **Done**: what changed, at most 5 bullets, one line each, in plain words (no file dumps, no jargon).
- **Decided**: real decisions only, with the reason in a few words. None is fine.
- **Next time**: concrete next steps as checkboxes.
- **Files**: notes created or changed, as `[[wikilinks]]`, at most 6.

If nothing substantial happened, say "Nothing to log" and stop.

## 2. Add the entry at the top of the journal

Format:

```markdown
## YYYY-MM-DD - <one sentence that sums up the session>

**Done**
- ...

**Decided**
- ...

**Next time**
- [ ] ...

**Files**
- [[...]]

---
```

- Omit an empty section.
- Several sessions the same day: add ` (2)`, ` (3)` after the date.

**Insert, never rewrite.** The journal grows long. Insert the new entry right after the `# Journal` header line (before the first `## ` entry) with a targeted edit. Never rewrite the whole file from what you have read, and never read it page by page to rewrite it: that is how a journal gets truncated. After the edit, check the file is longer than before.

## 3. Update the memory

In the Memory file:

- `## Where things stand`: rewrite to reflect now, 3-6 lines.
- `## Next steps`: replace with the current next steps.
- `## Recent decisions`: add one dated line per real decision; keep the 10 most recent.

Create a missing section rather than reshaping the file.

## 4. Close

Confirm in one or two lines: the entry title and the journal path. If the inbox holds items, add: "<n> items in the inbox: run `inbox` next time."

## Rules

- Write only what happened in this conversation. Never invent a decision or a next step.
- If a decision deserves its own note (it changes direction, money or people), suggest `decision`.
