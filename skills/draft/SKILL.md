---
name: draft
description: Drafts an email, a message or a post in the user's own voice, using the brain's voice guide and what it knows about the person, the relationship and the business. Builds the voice guide from the user's own texts if none exists. Never sends anything. Use when the user says "draft", "rédige", "écris un mail à", "réponds à", "prépare un message pour", "write an email to", "reply to".
---

# Draft

Write a message that fits this relationship and this moment, in the user's voice. Write in the recipient's language, or the user's if unknown.

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states.

- Paths from its `## Brain map`: Voice, People, Context. For a role missing from the map only: Voice `_System/Voice.md`.
- Sources of truth: if a mail or chat tool is connected, the past exchanges with this person live there.

## Where the voice comes from

In this order, first found wins, and say which one you used:

1. The **Voice** file of the Brain map (a voice guide: tone, words used, words never used, signature, examples).
2. A voice section in `AGENTS.md` or in the Context file.
3. The user's own sent messages to this person, through the mail or chat connector (read 3 to 5).
4. Texts the user wrote in this conversation or in the brain (journal, dictations).

If you had to fall back to 3 or 4, offer at the end: "Shall I build your voice guide from these examples?" On a yes, write the Voice file: tone in 3 lines, how they open and close, words they use, words they never use, length, 2 short real examples. Add the Voice row to the Brain map if missing.

## 1. Get the brief

Who it is for, what it is about, the goal (inform, ask, close, decline, follow up). If the recipient or the goal is missing, ask both in one question and wait.

## 2. Gather the material

- The person's note and the latest notes that mention them. Read them, do not skim titles.
- The last exchange with them, if a connector gives access.
- The business context, if the message touches the offer, prices or commitments.
- Nothing found about the person: say so and ask how they know each other.

## 3. Write

- Email: subject, then body. Message: body only. Post: hook line, body, ending.
- Short. One idea per paragraph. A clear ask or next step at the end.
- The register of this relationship (formal or direct), from past exchanges.
- Then apply the `de-ai-ify` rules: no stock transitions, no clichés, no em dashes, no bold on whole sentences, no list of three by reflex.
- One variant at most (shorter, or warmer).

## 4. Hand over

- Show the draft. List the facts the user should check (dates, numbers, names).
- If it records a commitment or a decision, offer to log it (`person`, `decision`).
- If the user corrects the tone, offer to add the lesson to the Voice file.

## Rules

- **Never send.** With a mail or chat connector, create a draft there only after an explicit yes.
- Never invent history, a promise, a price or a date absent from the brain, the connected tools or the conversation.
