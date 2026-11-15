---
name: person
description: Creates or updates a person's note in the second brain (client, prospect, partner, colleague, candidate) with who they are, the state of the relationship and how to talk to them. Use when new information about someone appears (call, email, meeting) or when the user says "person", "fiche contact", "mets à jour la fiche de", "qui est", "add this person", "update X's note".
---

# Person

One note per person, answering "who is this" and "what should I know before talking to them". Answer in the user's language.

## Find the folder

`## Brain map` in the root `AGENTS.md` (or `CLAUDE.md`), role People. If there is none: `People/`, `Personnes/` or `Contacts/`. If none exists, ask where people notes should live, and suggest `brain-setup` to record the answer.

## Steps

1. Identify the person (name given by the user, or the people discussed in this conversation). Search the folder and the whole brain for an existing note, including spelling variants and first-name-only mentions. Never create a second note for the same person.
2. Gather the new information: from the user's message, this conversation, or the note the user points to. Only facts that were said or written.
3. Create `<People>/Firstname_Lastname.md` if missing, or update the existing note:

```markdown
---
type: person
created: YYYY-MM-DD
updated: YYYY-MM-DD
company: <if known>
role: <if known>
---

# Firstname Lastname

## Who they are
<role, company, background, in a few lines>

## Relationship
<how we know them, where things stand, last contact with date and a [[link]] to the note that says it>

## How to talk to them
<what they care about, how they decide, what they turned down, tone that works>

## History
- YYYY-MM-DD: <fact> ([[source note]])
```

4. On update: add new facts to the right section, add a dated line to `History`, set `updated:` to today. Correct outdated facts rather than piling contradictions; keep the old one in History if it matters.
5. Link the source note (meeting, email, capture) back to the person with `[[Firstname_Lastname]]`.
6. Confirm in one line: created or updated, and what changed.

## Rules

- No speculation about personality, health, private life or anything the person did not share in a work context.
- Deal or project status lives in its own note. The person note gets one line and a link.
- File names: no accents, no spaces.
