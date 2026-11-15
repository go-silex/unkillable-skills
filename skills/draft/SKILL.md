---
name: draft
description: Drafts an email, a message or a post in the user's own voice, using what the second brain knows about the person, the relationship and the business. Never sends anything. Use when the user says "draft", "rédige", "écris un mail à", "réponds à", "prépare un message pour", "write an email to", "reply to".
---

# Draft

Write a message that fits this relationship and this moment, in the user's voice. Answer in the language of the message's recipient, or the user's language if unknown.

## Find the folders

`## Brain map` in the root `AGENTS.md` (or `CLAUDE.md`). Context `_System/Contexte_Global.md` or `_System/Context.md`; People `People/`; Voice `_System/Voice.md` (optional).

## 1. Get the brief

From the user's message: who it is for, what it is about, the goal (inform, ask, close, decline, follow up). If the recipient or the goal is missing, ask both in one question and wait.

## 2. Gather the material

- The person's note and the latest notes that mention them (meetings, decisions, commitments). Read them, do not skim titles.
- The business context, if the message touches the offer, prices or commitments.
- The Voice file if it exists. If not, take the user's voice from messages they wrote in this conversation or in the brain.
- If you find nothing about the person, say so and ask for the minimum: how they know each other, and the goal.

## 3. Write

- Email: subject line, then body. Message: body only. Post: hook line, body, ending.
- Short. One idea per paragraph. A clear ask or next step at the end.
- The tone of this relationship: formal or direct according to past exchanges.
- Then pass it through the `humanize` rules: no stock transitions, no clichés, no em dashes, no bold on whole sentences, no list of exactly three by reflex.
- If useful, one variant (shorter, or warmer). Not more.

## 4. Hand over

Show the draft in the chat. Then:

- List the facts you used that the user should check (dates, numbers, names).
- If the message makes a commitment or records a decision, offer to log it in the person's note or with `decision`.
- If the user corrected your tone, offer to save the lesson in `_System/Voice.md` (create it on a yes).

## Rules

- **Never send.** Even if a mail or chat connector is available, only create a draft there after an explicit yes.
- Never invent history, a promise, a price or a date absent from the brain or the conversation.
