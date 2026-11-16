---
name: done
description: End-of-session log for the second brain. Spots the important decisions taken in the session and asks before logging them, then writes what was done, decided and what comes next at the top of the journal, and updates the memory so the next session (or another AI tool) picks up without losing anything. Use when the user says "done", "on clôture", "fin de session", "log la session", "wrap up", "close the session".
---

# Done: end of session

Leave a clean trace of this session in the brain. Local only: nothing is sent anywhere. Talk in the user's language; write content in the language `AGENTS.md` sets.

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states.

- Paths come from its `## Brain map`. For a role missing from the map only: Journal `00_COCKPIT/Journal.md`, Memory `_System/MEMORY.md`, Decisions `00_COCKPIT/Decisions/`, Inbox `00_IMPORT/`. If the journal does not exist, create it with the header `# Journal`.
- If the Templates folder holds `Journal_Entry.md`, use its format instead of the one below.

## 1. Spot the important decisions

Go through the conversation and list the choices that were made. Keep only the **important** ones: a choice that changes direction, money, people, a commitment to someone outside, or that would be costly to undo.

Not a decision: a task ("send the email to Michel"), a preference for this session, an idea still open, something only said or suggested.

For each important one, ask in one message:

```
It looks like you decided:
1. <decision, one line>
2. ...
Shall I log them in the decisions? (yes / which ones / no)
```

On a yes, write them with the `decision` skill's format and rules (note, decisions log, memory line). If none is important, skip this step silently.

## 2. Sum up the session

Keep only what lasts:

- **Done**: what changed, at most 5 bullets, one line each, plain words.
- **Decided**: the decisions confirmed in step 1, with a link to their note. Minor choices worth remembering can appear as "said, not decided".
- **Next time**: concrete next steps as checkboxes.
- **Files**: notes created or changed, as `[[wikilinks]]`, at most 6.

If nothing substantial happened, say "Nothing to log" and stop.

## 3. Add the entry at the top of the journal

```markdown
## YYYY-MM-DD · <one sentence that sums up the session>

**Done**
- ...

**Decided**
- ... ([[decision note]])

**Next time**
- [ ] ...

**Files**
- [[...]]

---
```

- Omit an empty section. Several sessions the same day: add ` (2)`, ` (3)` after the date.
- **Insert, never rewrite.** Insert the entry right after the header block (before the first `## ` entry) with a targeted edit. Never rewrite the whole file from what you read: that is how a journal gets truncated. After the edit, check the file is longer than before.

## 4. Update the memory

- `## Where things stand`: rewrite to reflect now, 3 to 6 lines.
- `## Next steps`: replace with the current next steps.
- `## Recent decisions`: already updated in step 1; keep the 10 most recent.

Create a missing section rather than reshaping the file.

## 5. Close

One or two lines: the entry title and the journal path. If the inbox holds items: "<n> items in the inbox: run `inbox` next time."

## Rules

- Write only what happened in this conversation. Never invent a decision or a next step.
- Never log a decision without the user's yes.
