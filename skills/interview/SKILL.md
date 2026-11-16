---
name: interview
description: Fills the second brain by interviewing its owner. Seven days, one theme a day, 5 to 10 short questions asked one at a time, easy to answer by dictation on a phone. Checks the brain before each question so it never asks for something already known, files each answer with the brain's routing, and tracks progress in the cockpit. After the seven days it keeps going on the emptiest parts of the brain and the questions left open. Use when the user says "interview", "interviewe-moi", "pose-moi les questions du jour", "remplis mon cerveau", "fill my brain", "ask me today's questions".
---

# Interview

The brain is only as good as what it knows. Ask the owner, one question at a time, and file every answer where it belongs. Talk in the user's language; file content in the language `AGENTS.md` sets, keeping the user's quotes verbatim.

## Find your way

Read the root `AGENTS.md` first; it wins over this skill on everything it states.

- Paths from its `## Brain map`. Progress file: `<Cockpit>/Interview_Progress.md` (default Cockpit `00_COCKPIT/` only if the map has none).
- Routing: the table "If it is… / It goes to…" of `AGENTS.md`, or each folder's `AGENTS.md` or `README.md`. Answers are filed with it, never by guess.
- Confidentiality rules of `AGENTS.md` apply to every answer.
- Templates folder: a new person, decision or project note follows its template.

## Day 1: create the progress file

If `Interview_Progress.md` does not exist:

1. Read the Context file, the Memory and the root `AGENTS.md` to learn who the user is (role, company, team size, tools).
2. Adapt the seven generic themes to that profile (a solo consultant has no "team" day; a CEO of two companies gets one theme per company):

| Day | Generic theme |
|---|---|
| J1 | Your role and your company |
| J2 | Your team |
| J3 | Your typical week |
| J4 | Your projects |
| J5 | Your network |
| J6 | How you decide |
| J7 | What you want to stop |

3. Show the seven themes in one message and ask for a yes or changes. Then write the file:

```markdown
---
updated: YYYY-MM-DD
window: YYYY-MM-DD to YYYY-MM-DD
---

# Interview progress

> The `interview` skill asks 5 to 10 questions a day on one theme. Answers are routed with the routing of the root `AGENTS.md`, tagged `(interview Jn)`.
> Never ask twice: before a question, check the brain and the day's "Already known".

| Day | Date | Theme | Status |
|---|---|---|---|
| J1 | <date> | <theme> | to do |
...

---

## J1 · <theme> (<date>)

Already known (do not ask): <what the brain already says on this theme, with its source>

- [ ] <question>

Log:
```

Write the questions of J1 only. Each later day's questions are written the day it starts, so they use what was learned. A file that already holds questions for later days (prepared by a coach) is kept as is: use its questions, still checked against the brain.

Dates follow the user's working days; `AGENTS.md` may set the window. Status values: `to do`, `in progress`, `done`.

## Each day: run the session

1. Open the progress file. Today's day is the first one not `done` (a missed calendar day does not skip a theme). Set it `in progress`.
2. Before asking, refresh "Already known": search the brain for each question's answer (Context, People, project notes, decisions, previous days' logs). A question already answered is ticked with "(already known: <where>)" and skipped. Questions carried over from the previous day come first.
3. Ask **one question at a time**:
   - One sentence, one thing asked, no sub-questions, no jargon.
   - Easy to answer by voice: "Who are the three people you work with most, and what does each do?" rather than a form.
   - Number it: "3/8 ·".
4. When the answer comes:
   - Clean the dictation lightly, keep the user's words.
   - File each piece with the routing: a person → their note (`person` rules), a priority → Context, a project → its note, a rule about how to work with them → `AGENTS.md` (show the line, ask first), a decision → ask, then `decision` rules. One answer can feed several places.
   - Tag each fact `(interview Jn)`.
   - Reply in one short line: where it went. Then the next question.
5. The user says "skip": move on. "Stop" or "later": end the session; unanswered questions move to the next day under "Carried over".
6. End of day: tick the answered questions, write one line per answer in "Log" (`<question> → <where it was filed>`), set the day `done` (or `in progress` if questions remain), update `updated:`. Close with: how many answered, where things went, tomorrow's theme.

## After the seven days

When every planned day is `done`, `interview` keeps working in open mode. Find the gaps, in this order:

1. Unanswered and carried-over questions in the progress file.
2. Marks in the brain: "to confirm", "open", "unknown", "TODO", "?" in `AGENTS.md`, Context, person notes.
3. Thin parts: roles of the Brain map with few notes, person notes with empty sections, people met recently (calendar or journal) with no note.
4. What changed: a new project, client or tool seen in the journal since the last interview.

Add a section `## Extra · YYYY-MM-DD · <theme of the gaps>` with 5 to 10 questions, add a row to the table, and run it the same way.

## Rules

- Never ask what the brain already knows. If unsure, quote what the brain says and ask "still true?".
- One question per message. Never a list of questions to answer at once.
- Never invent an answer or complete one. A vague answer is filed as said, with "to confirm".
- Never write sensitive answers (health, family, deals under NDA, legal) anywhere `AGENTS.md` does not allow.
