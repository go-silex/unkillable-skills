---
name: connect
description: Registers a newly connected tool (CRM, mail, calendar, chat, drive, task tool, meeting recorder) in the second brain, so every skill knows which facts that tool owns. Updates the "Sources of truth" table and the routing in AGENTS.md, settles what the brain keeps versus what the tool keeps, and tests one read. Use when the user says "connect", "j'ai connecté", "nouveau connecteur", "ajoute Attio", "add a source", "I connected my CRM", or when brain-check finds a connected tool missing from the table.
---

# Connect a tool

A tool the brain does not know about creates two truths. Register it so every skill reads the tool for what it owns, and stops copying it. Talk in the user's language. Content in the language `AGENTS.md` sets.

## 1. Identify the tool

- Which tool, and which account if there are several (for example two Gmail accounts, one per company).
- Is a connector available in this session? Try one harmless read (list one record, one event, one thread). Say whether it works. If no connector exists, the tool can still be registered: skills will then give the user what to update by hand.

## 2. Settle what it owns

Propose, then let the user correct. Typical splits:

| Tool | Owns | The brain keeps |
|---|---|---|
| CRM (Attio, HubSpot, Pipedrive, Folk) | contact details, company records, deal stage, owner | who the person is, how to talk to them, history of the relationship, a link to the record |
| Mail | written exchanges | nothing copied; a decision or a commitment found in a mail goes to its note |
| Calendar | who, when | meeting notes |
| Meeting recorder (Granola, Claap, Fathom) | what was said | the summary that matters, decisions, person updates |
| Task tool (Notion, Linear, Asana, Spark) | tasks, owner, due date, status | no task lists; a link |
| Drive, signed documents | contracts, statutes, board packs | a link in the note's `## Sources` |
| Chat (Slack, WhatsApp) | conversations | nothing copied; what matters goes to its note |

Ask one grouped question: "Does <tool> own <facts>? Does anything else it holds count as the truth?" Wait for the answer.

## 3. Update the brain

Show the changes, apply on a yes:

1. **Sources of truth** table in the root `AGENTS.md` (any heading containing "truth" or "Sources"): one row per fact the tool owns, in the table's existing columns. If the table has an `Owner` column, use its external value (often `externe` or `external`). If the table is missing, create `## Sources of truth` with `Fact | Source of truth | Does not count`.
2. **Overlaps**: if a brain role covers the same thing (People and a CRM), add one line to that folder's `AGENTS.md` or `README.md`: what the tool owns, what the note keeps, and the field that links them (for example `crm:` in the person frontmatter).
3. **Routing**: if the tool changes where something goes (tasks now go to the task tool), update that routing row.
4. **Source ranking**: if `AGENTS.md` ranks sources ("when two sources disagree"), ask where the new tool sits.

## 4. Close

Three lines at most: rows added, what changes in practice ("`person` will now offer to update Attio; `welcome` will read your calendar"), and whether the test read worked.

## Disconnect

The user drops a tool: mark its rows "(disconnected YYYY-MM-DD)" and ask what owns those facts now. Never delete the rows silently.

## Rules

- Never copy data from the tool into the brain while registering it.
- Never write into the tool here. This skill only reads, to test.
