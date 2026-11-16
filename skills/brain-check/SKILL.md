---
name: brain-check
description: Health check of the second brain. Checks that AGENTS.md exists and holds a Brain map, that every mapped folder exists, that each connected tool is listed as a source of truth, that templates and folder instructions are in place, and that no CLAUDE.md shadows AGENTS.md. Proposes fixes and applies them after a yes. Sets the brain up on first install. Use when the user says "brain-check", "check my brain", "santé du cerveau", "vérifie le cerveau", "setup my brain", "brain-setup", or when another skill cannot find a folder.
---

# Brain check

Check that the brain is ready for the Unkillable skills, report what is wrong, fix it after a yes. Talk in the user's language. The full contract is `BRAIN_CONTRACT.md` at the plugin root; this skill holds what you need if you cannot reach it.

## 1. Read, change nothing yet

- List the root two levels deep. Read the root `AGENTS.md`, and each top-level folder's `AGENTS.md` or `README.md`.
- Look for a `CLAUDE.md` in the brain and in each parent folder up to the home folder.

## 2. Run the checks

| # | Check | Pass when |
|---|---|---|
| 1 | Instructions | A root `AGENTS.md` exists. |
| 2 | No `CLAUDE.md` | None in the brain. None in a parent folder (Claude Code would read it instead of `AGENTS.md`). |
| 3 | Brain map | `AGENTS.md` has a `## Brain map` table with the roles Inbox, Cockpit, Journal, Memory, Context, Decisions, People, Templates. Voice and Brand are optional. |
| 4 | Paths | Every path in the map exists. |
| 5 | Sources of truth | `AGENTS.md` has a table with a "Source of truth" column. |
| 6 | Connectors | Every external tool connected in this session (mail, calendar, chat, CRM, drive, task tool, meeting notes) appears in that table. Look at your available tools to list them. |
| 7 | Routing | `AGENTS.md` says where each kind of note goes (a routing table or a section per folder). |
| 8 | Templates | The Templates folder holds at least `Person.md` and `Decision.md`. |
| 9 | Folder instructions | Each top-level folder is described somewhere: its own `AGENTS.md` or `README.md`, or the routing of the root `AGENTS.md`. Only a folder described nowhere fails. |
| 10 | Inbox | Fewer than 15 items. No note outside the inbox still has `type: capture`. |
| 11 | Old commands | No file in `.claude/commands/`, `.opencode/command/` or `.agents/workflows/` duplicates a plugin skill (`done`, `capture`, `triage`, `inbox`, `decision`, `weekly-review`, `briefing`, `draft`). |

## 3. Report

```
Brain check: <n>/11 OK

To fix
- <check>: <what is wrong> → <proposed fix>

OK
- <checks that pass, one line>
```

Then ask: "Shall I apply these fixes?" Wait for a yes. The user can pick some.

## 4. Fixes

Apply only what was approved. Never delete, rename or overwrite a user's note.

- **No `AGENTS.md`**: create it with three sections: who the brain is for (left to fill), `## Brain map`, `## Sources of truth`. If folders already exist, map them as they are. If the user starts from nothing, propose the default tree below, and create it only on a yes.
- **`CLAUDE.md` with content**: show it, propose to move its content into `AGENTS.md` (section by section, ask on any conflict), then move `CLAUDE.md` to the archive folder (or `_System/Archive/`). A `CLAUDE.md` holding only `@AGENTS.md` is simply archived. A `CLAUDE.md` in a parent folder: tell the user to move the brain out of that folder; never touch the parent file.
- **Role missing from the map**: find the folder that plays the role (names like `Inbox`, `00_Inbox`, `Personnes`, `Contacts`, `Journal`, `Templates`, `Modeles`) and add the row. If none exists, propose the default path and create it on a yes.
- **Path missing on disk**: ask whether the folder moved (search for it) or should be created.
- **No sources table**: add one with the brain-owned rows (context, memory, journal, decisions, people), one row per connected tool, and the line "A new tool gets connected: run `connect`". Then ask what each tool owns (`connect` skill).
- **Connected tool not in the table**: run the `connect` steps for it.
- **No template**: create `Person.md` and `Decision.md` in the Templates folder from the formats in the `person` and `decision` skills. Not blocking: the skills use their own format meanwhile.
- **Folder without instructions**: write a 3-line `README.md` saying what goes there, drawn from the routing; ask if unclear.
- **Old commands**: move them to the archive folder, after a yes. Tell the user the plugin now provides them in every tool.

Default tree, only when the user starts from nothing:

```
00_IMPORT/          Inbox
00_COCKPIT/         Cockpit, Journal.md, Decisions/
_System/            Context.md, MEMORY.md, Templates/
People/
```

## 5. Close

One line per fix applied, then the next skill to try: `welcome` to start a session, `interview` to fill the brain, `capture` to drop an idea.

## Rules

- Never invent business context. The Context file stays empty until the user fills it, or asks you to draft it from their notes.
- Never write a `CLAUDE.md`.
