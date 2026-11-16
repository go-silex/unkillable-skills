---
name: inbox
description: Processes the second brain's inbox. Reads every captured note, proposes where each one goes (destination, title, type, links), waits for the user's yes, then files them following the brain's own routing, merges duplicates and updates people notes. Use when the user says "inbox", "inbox processor", "triage", "trier", "vide l'inbox", "range l'inbox", "process my inbox", "clean up captures".
---

# Inbox: empty the inbox

File every captured item in the right place, linked, so the brain does not rot. Talk in the user's language; content in the language `AGENTS.md` sets.

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states.

- Inbox path: its `## Brain map`, role Inbox (default `00_IMPORT/` only if the map has none).
- Destinations: its routing (a table "If it is… / It goes to…" or a section per folder), then the `AGENTS.md` or `README.md` of the destination folder. Never guess a destination.
- Sources of truth: if a tool owns a fact (a task tool owns tasks, a CRM owns contact details), the item goes to that tool, not to a note. Offer it, after a yes, through the connector.
- Templates: when filing turns a capture into a person, a decision or a meeting note, follow the Templates folder's template for that type.
- Confidentiality rules of `AGENTS.md` apply to where things go.

## 1. Read and plan

1. List the inbox (ignore hidden files and the inbox's own `README` or `AGENTS.md`).
2. Read each item fully, with its frontmatter (`kind`, `people`, `related`, `due` help routing).
3. For each one, decide: destination, title, final `type`, links, and whether it merges into an existing note (search for real: same topic, same person, same name variants).

## 2. Show the plan, wait for a yes

```
<n> items in the inbox

1. <title> → <destination> (<type>) · links: <...>
2. <title> → merge into [[Existing note]]
3. <title> → task in <project or cockpit>
4. <title> → stays in the inbox: <why>, could go to <suggestion>
...
Shall I file them? (yes / numbers to change / no)
```

Act only after the yes. The user may correct some lines: apply the corrections, then file. Skip the wait only if the user said so in the request ("trie sans me demander", "go ahead").

## 3. File

For each approved line:

- **Title** improved if vague. File name per the brain's convention (default `YYYY-MM-DD_Short_Title.md` for dated notes, `Title_Case.md` otherwise; no accents, no spaces).
- **Frontmatter**: `type` becomes what the note is now (table below); keep `created`; drop `status: to-file` and `kind`; keep `source`, `people`, `related`, `due`. Never fill a field you do not know.
- **Links**: `[[links]]` to existing notes (people, projects, clients), checked for real.
- **Merge**: add the content to the existing note under a dated line, then move the capture to the archive folder (or ask if there is none). Never delete.
- **Task**: `- [ ]` in the project note or the cockpit, or in the task tool if it owns tasks; then archive the capture.
- **Person mentioned with new information**: update their note (`person` skill rules).
- **Decision**: a decision captured is still to confirm; ask, then use the `decision` skill.
- **Unclassifiable or too thin**: leaves the inbox untouched (keeps `type: capture`).

| The note is | `type` |
|---|---|
| A meeting or call summary | `meeting` |
| An idea or a piece of work to carry | `project` |
| A choice that was made | `decision` |
| A reusable way of doing things | `process` |
| An article, PDF or reading (`source:` holds the URL or origin) | `source` |
| A lasting reference | `reference` |
| A person | `person` |

The brain's own conventions file or templates win over this table.

## 4. End check and report

- No note outside the inbox still has `type: capture` or `status: to-file`. Fix any you meet and say so.
- Report: `<n> filed` (title → destination, one line each), `<n> links`, `<n> people updated`, `<n> left in the inbox and why`.

## Rules

- Never delete without an explicit yes.
- Never change the meaning while cleaning.
