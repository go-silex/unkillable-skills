---
name: brain-setup
description: Sets up a notes folder as a second brain the other Unkillable skills can use. Finds or creates the inbox, journal, memory and decision folders, writes the "Brain map" in AGENTS.md so every AI tool (Claude Code, Codex, Antigravity) reads the same instructions. Use on first install, when a skill cannot find a folder, or when the user says "setup my brain", "configure le cerveau", "brain-setup", "installe le plugin dans ce dossier".
---

# Brain setup

Make the current folder ready for the Unkillable skills, without breaking what is already there. Answer in the user's language.

## 1. Look before touching anything

- List the root of the folder (two levels deep) and read `AGENTS.md` and `CLAUDE.md` if they exist.
- If `AGENTS.md` already has a `## Brain map` section, show it and ask whether anything should change. Stop there if not.

## 2. Find each role

Every Unkillable skill works with these roles. For each one, take the first path that exists; if none exists, propose the default.

| Role | What it holds | Look for (in order) | Default to create |
|---|---|---|---|
| Inbox | Raw captures waiting to be filed | `00_IMPORT/`, `00_Inbox/`, `Inbox/`, `_Inbox/` | `00_IMPORT/` |
| Cockpit | Steering notes, reviews, briefings | `00_COCKPIT/`, `Cockpit/` | `00_COCKPIT/` |
| Journal | One entry per work session, newest first | `00_COCKPIT/Journal.md`, `Journal.md` | `00_COCKPIT/Journal.md` |
| Memory | Where things stand, next steps, recent decisions | `_System/MEMORY.md`, `MEMORY.md` | `_System/MEMORY.md` |
| Context | Who the user is, the business, priorities | `_System/Contexte_Global.md`, `_System/Context.md`, `CONTEXT.md` | `_System/Context.md` |
| Decisions | One note per decision | `00_COCKPIT/Decisions/`, `Decisions/` | `00_COCKPIT/Decisions/` |
| People | One note per person | `People/`, `Personnes/`, `Contacts/` | `People/` |
| Voice | How the user writes (optional) | `_System/Voice.md`, `_System/Style.md` | none, created by `draft` later |

## 3. Show the plan, then act

Show the table you would write (role, path, "exists" or "to create") and ask for a yes. Then:

1. Create only the missing folders and files. New files get a one-line header, nothing else. Memory starts with three sections: `## Where things stand`, `## Next steps`, `## Recent decisions`.
2. Write or update the `## Brain map` section in `AGENTS.md`:

```markdown
## Brain map

| Role | Path |
|---|---|
| Inbox | `00_IMPORT/` |
| Cockpit | `00_COCKPIT/` |
| Journal | `00_COCKPIT/Journal.md` |
| Memory | `_System/MEMORY.md` |
| Context | `_System/Contexte_Global.md` |
| Decisions | `00_COCKPIT/Decisions/` |
| People | `People/` |
```

3. Make every tool read the same instructions:
   - `AGENTS.md` is the single source. Codex and Antigravity read it; Claude Code reads `CLAUDE.md`.
   - If `CLAUDE.md` holds real content and `AGENTS.md` does not exist: move the content into `AGENTS.md`, and replace `CLAUDE.md` with the single line `@AGENTS.md`. Ask first.
   - If both hold different content: do not merge on your own. Show the difference and ask.
   - If `AGENTS.md` exists and `CLAUDE.md` does not: create `CLAUDE.md` with `@AGENTS.md`.

## 4. Check old commands

If `.claude/commands/` or `.opencode/command/` hold commands with the same names as the Unkillable skills (`done`, `capture`, `triage`, `decision`, `weekly-review`, `briefing`, `draft`), tell the user the plugin now provides them in every tool, and offer to move the old files into `_System/Archive/commands/`. Never delete them.

## 5. Confirm

Three lines at most: what was created, where the Brain map lives, and the next skill to try (`welcome` to start a session, `capture` to drop an idea).

## Rules

- Never delete, rename or overwrite a user's note.
- Never invent business context. The Context file stays empty until the user fills it or the user asks you to draft it from their notes.
