# Unkillable skills

Daily rituals for your second brain, in every AI tool you use: Claude Code, OpenAI Codex (ChatGPT) and Google Antigravity. By [Unkillable Companies](https://github.com/go-silex).

*Version française plus bas.*

## What's inside

| Skill | What it does |
|---|---|
| `brain-setup` | Prepares the folder: finds or creates inbox, journal, memory, decisions, people; writes the Brain map in `AGENTS.md`. Run it first. |
| `welcome` | Start of session: where things stand, what is waiting, what to do first. |
| `done` | End of session: logs what was done and decided at the top of the journal, updates the memory. |
| `capture` | Drops an idea, task or link in the inbox in seconds. |
| `inbox` | Empties the inbox: files every note in the right place, with links. |
| `weekly-review` | Weekly review of the business, then an optional hygiene pass on the brain. |
| `decision` | Logs a decision with its context, options, reason and when to revisit it. |
| `save-context` | Turns the current conversation into a handover note you can resume anywhere. |
| `person` | Creates or updates a person's note. |
| `draft` | Drafts an email, message or post in your voice, from what the brain knows. Never sends. |
| `humanize` | Removes what makes a text sound AI-written, without changing what it says. |

Skills answer in your language. Nothing leaves your machine: no Slack, no external service.

## Install

### Claude Code

```
/plugin marketplace add go-silex/unkillable-skills
/plugin install unkillable@unkillable-companies
```

Then type `/unkillable:` to see the skills (for example `/unkillable:done`). Update later with `/plugin marketplace update unkillable-companies`.

### OpenAI Codex (CLI, IDE, ChatGPT desktop app)

```
codex plugin marketplace add go-silex/unkillable-skills
```

Then open the Plugins directory (`/plugins` in Codex, or Plugins in the ChatGPT desktop app), install **Unkillable**, and start a new session. Call a skill with `$` (for example `$done`) or list them with `/skills`.

### Google Antigravity

```
agy plugin install https://github.com/go-silex/unkillable-skills
```

Then type `/` followed by the skill name (for example `/done`). In the app, run `/skills reload` or open a new conversation if the skills do not show.

### Any other tool that reads Agent Skills

Copy the skills into your vault:

```
git clone https://github.com/go-silex/unkillable-skills
bash unkillable-skills/scripts/install-into-vault.sh /path/to/your/vault
```

This writes them to `.agents/skills/` (Codex, Antigravity, Cursor, Gemini CLI) and `.claude/skills/` (Claude Code). Re-run it to update.

## First run

Open your notes folder in your tool and run `brain-setup`. It shows what it found, asks before creating anything, and writes a `## Brain map` table in `AGENTS.md`. Every skill reads that table to know where your inbox, journal and memory live, so the plugin adapts to your folder names. `CLAUDE.md` becomes `@AGENTS.md`, so all tools read the same instructions.

---

## En français

Les rituels quotidiens de ton second cerveau, dans tous tes outils IA : Claude Code, OpenAI Codex (ChatGPT) et Google Antigravity.

- **Début de session** : `welcome`. **Fin de session** : `done`.
- **Capturer** une idée : `capture`. **Vider l'inbox** : `inbox`.
- **Revue de la semaine** : `weekly-review`. **Consigner une décision** : `decision`.
- **Passer le relais** à une autre conversation : `save-context`. **Fiche d'une personne** : `person`.
- **Rédiger** un mail ou un post dans ta voix : `draft`. **Enlever l'effet IA** d'un texte : `humanize`.

**Installer** : voir les commandes ci-dessus pour ton outil, puis lance `brain-setup` dans ton dossier de notes. Il te montre ce qu'il a trouvé et te demande avant de créer quoi que ce soit.

**Appeler un skill** : `/unkillable:done` dans Claude Code, `$done` dans Codex, `/done` dans Antigravity. Tu peux aussi juste le dire : « on clôture la session », « vide mon inbox ».
