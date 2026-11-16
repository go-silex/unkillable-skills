---
name: person
description: Creates or updates a person's note in the second brain (client, prospect, partner, colleague, candidate) with who they are, the state of the relationship and how to talk to them, following the brain's own person template. If a CRM owns contact details, it offers to update the CRM record too. Use when new information about someone appears (call, email, meeting) or when the user says "person", "fiche contact", "mets à jour la fiche de", "qui est", "add this person", "update X's note".
---

# Person

One note per person, answering "who is this" and "what should I know before talking to them". Talk in the user's language; content in the language `AGENTS.md` sets.

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states.

- People path from its `## Brain map` (role People). If the map has none: ask where people notes live, and suggest `brain-check`.
- Template: if the Templates folder holds `Person.md`, follow it exactly (sections, frontmatter, which sections are replaced and which are only added to). Read the People folder's `README.md` or `AGENTS.md` too.
- Sources of truth: find who owns contact details, company, deal stage. If a CRM owns them, the note keeps the rest and a link (`crm:` field) to the record.

## Steps

1. Identify the person. Search the People folder and the whole brain for an existing note: name variants, first name only, email, aliases. Never create a second note for the same person.
2. Gather the new information: from the user's message, this conversation, or the note they point to. Only facts that were said or written, each with a short source tag if the brain uses them (`(meeting 2026-11-20)`).
3. Create or update the note (template first; otherwise the format below). On update: replace what the template says to replace, add a dated line to the history, set `updated:` to today. Correct outdated facts rather than piling contradictions.
4. Link the source note (meeting, email, capture) to the person with `[[Firstname_Lastname]]`.
5. **CRM**: if a CRM owns contact facts and something it owns changed (role, company, email, phone, stage, next step), list the changes and ask: "Update <CRM> too?" On a yes, update the record through the connector, then put its link in `crm:`. No connector: give the user the list to update by hand.
6. Confirm in one line: created or updated, what changed, and the CRM status.

Default format, when the brain has no template:

```markdown
---
type: person
created: YYYY-MM-DD
updated: YYYY-MM-DD
company:
role:
emails: []
crm:
---

# Firstname Lastname

## Who they are
## Relationship
<how we know them, where things stand, last contact with a [[link]]>
## How to talk to them
<what they care about, how they decide, what they turned down, tone that works>
## History
- YYYY-MM-DD: <fact> ([[source]])
```

## Rules

- No speculation about personality, health, private life, or anything not shared in a work context.
- Deal or project status lives in its own note or in the CRM. The person note gets one line and a link.
- Never write in the CRM without a yes.
- File name per the brain's convention (default `Firstname_Lastname.md`, no accents, no spaces).
