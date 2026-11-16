# Brain contract

What the Unkillable skills expect from a second brain. Any brain that follows this contract works with the plugin, whatever its folder names. A brain builder (for example the Academy's brain factory) only has to write the three sections below in the root `AGENTS.md`.

## 1. `AGENTS.md` only

- The root `AGENTS.md` is the single instruction file. Claude Code, Codex and Antigravity all read it.
- No `CLAUDE.md`. Claude Code reads `AGENTS.md` on its own when no `CLAUDE.md` exists (tested on Claude Code 2.1.325). A `CLAUDE.md` in the brain or in a parent folder takes precedence, so keep the brain away from any folder that holds one.
- A folder that needs its own rules gets its own `AGENTS.md` (a stream, a client, a project). The root file says so.

## 2. `## Brain map`

A table of roles and paths. Skills never assume a path: they read this table. Defaults apply only to a role missing from the table.

| Role | What it holds | Default if absent |
|---|---|---|
| Inbox | Raw captures waiting to be filed | `00_IMPORT/` |
| Cockpit | Steering notes, reviews, interview progress | `00_COCKPIT/` |
| Journal | One entry per work session, newest first | `00_COCKPIT/Journal.md` |
| Memory | Where things stand, next steps, recent decisions | `_System/MEMORY.md` |
| Context | Who the user is, the business, priorities | `_System/Context.md` |
| Decisions | One note per decision subject (current decision + dated history), plus `Decisions_Log.md` | `00_COCKPIT/Decisions/` |
| People | One note per person | `People/` |
| Templates | Note templates (`Person.md`, `Decision.md`, `Meeting.md`...) | `_System/Templates/` |
| Voice | How the user writes (optional) | `_System/Voice.md` |
| Brand | Brand kit, logos, deck template (optional) | `_System/Brand/` |

Extra roles are allowed. A skill ignores a role it does not use.

## 3. Sources of truth

A table that says which place owns each fact. Any heading works if it contains "truth" or "Sources" (for example `## Where the truth is`). Expected columns: `Fact | Source of truth`, optionally `Owner` and `Does not count`.

- A row whose source is a folder of the brain: the brain owns the fact.
- A row whose source is a tool (CRM, mail, calendar, task tool, drive): the tool owns the fact. The brain keeps a link and reads the tool, never a copy. A skill that learns such a fact offers to update the tool through its connector, after a yes.
- A new tool gets connected: the `connect` skill adds its rows. `brain-check` flags connected tools missing from the table.

## 4. Conventions the skills respect

When `AGENTS.md` (or a folder's `AGENTS.md`) states a rule, it beats the skill's default:

- language of the content (the skills always talk to the user in the user's language);
- file names and date formats (default: `YYYY-MM-DD_Short_Title.md`, no accents, no spaces);
- ritual days (weekly review day, interview window);
- routing (where each kind of note goes);
- confidentiality rules.

## 5. Frontmatter the skills write

Every note a skill creates has `type` and `created: YYYY-MM-DD`. Other fields only when known, never guessed.

| `type` | Fields |
|---|---|
| `capture` | `kind`, `source`, `people`, `related`, `due`, `status: to-file` |
| `decision` | `status` (active, replaced), `area`, `updated` |
| `person` | `updated`, `company`, `role`, `emails`, `crm` (link to the CRM record if a CRM owns contacts) |
| `meeting`, `project`, `process`, `source`, `reference` | `source`, `people`, `related` |

A template in the Templates folder replaces this table for its type.
