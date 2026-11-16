# Unkillable skills

Daily rituals for your second brain, in every AI tool you use: Claude Code, OpenAI Codex (ChatGPT) and Google Antigravity. By [Unkillable Companies](https://github.com/go-silex).

*Version française plus bas.*

## What's inside

| Skill | What it does |
|---|---|
| `brain-check` | Health check of the brain: Brain map, sources of truth, templates, folder instructions. Sets it up on first run. Run it first. |
| `connect` | Registers a newly connected tool (CRM, mail, calendar...) as the source of truth for what it owns. |
| `interview` | Fills the brain by interviewing you: 7 days, one theme a day, one question at a time, easy to dictate. |
| `welcome` | Start of session: where things stand, today's meetings, what is waiting, what to do first. |
| `done` | End of session: asks before logging important decisions, writes the journal entry, updates the memory. |
| `capture` | Drops an idea, task or link in the inbox in seconds, with useful metadata. |
| `inbox` | Empties the inbox: proposes where each note goes, files them after your yes. |
| `weekly-review` | Weekly review of the business, then an optional hygiene pass on the brain. |
| `decision` | Logs an important decision: one note, one line in the decisions log, one line in the memory. |
| `challenge` | Stress-tests an idea or a decision against what your brain knows, in short rounds of questions, before you commit. |
| `save-context` | Turns the current conversation into a handover note you can resume anywhere. |
| `person` | Creates or updates a person's note; offers to update your CRM if it owns contacts. |
| `draft` | Drafts an email, message or post in your voice, from what the brain knows. Never sends. |
| `de-ai-ify` | Removes what makes a text sound AI-written, without changing what it says. |
| `slides` | Sets up your brand kit once, then makes 16:9 HTML decks in your brand. |

Skills talk in your language and follow your brain's own rules (paths, templates, naming, language of notes): see [BRAIN_CONTRACT.md](BRAIN_CONTRACT.md). They read your connected tools when your `AGENTS.md` lists them as sources of truth, and never send or write anything outside the brain without your yes.

## Install

French quick guide: [INSTALL_FR.md](INSTALL_FR.md).

### Claude Code

```
/plugin marketplace add go-silex/unkillable-skills
/plugin install unkillable@unkillable-companies
```

Then turn on updates once: `/plugin` > **Marketplaces** > `unkillable-companies` > **Enable auto-update**. New skills then arrive on their own. Type `/unkillable:` to see the skills (for example `/unkillable:done`). Update by hand any time with `/plugin marketplace update unkillable-companies`.

For a notes folder you hand over, you can also declare the plugin in the folder's `.claude/settings.json`: Claude Code offers it when the folder is trusted.

```json
{
  "extraKnownMarketplaces": {
    "unkillable-companies": {
      "source": { "source": "github", "repo": "go-silex/unkillable-skills" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "unkillable@unkillable-companies": true }
}
```

### OpenAI Codex (CLI, IDE, ChatGPT desktop app)

```
codex plugin marketplace add go-silex/unkillable-skills
```

Then open the Plugins directory (`/plugins` in Codex, or Plugins in the ChatGPT desktop app), pick the **Unkillable Companies** marketplace, install **Unkillable**, and start a new session. Call a skill with `$` (for example `$done`) or list them with `/skills`. To get new skills: `codex plugin marketplace upgrade`, then restart the app.

### Google Antigravity

```
agy plugin install https://github.com/go-silex/unkillable-skills
```

Then type `/` followed by the skill name (for example `/done`). In the app, run `/skills reload` or open a new conversation if the skills do not show. To get new skills, run the same install command again.

### Any other tool that reads Agent Skills

Copy the skills into your vault:

```
git clone https://github.com/go-silex/unkillable-skills
bash unkillable-skills/scripts/install-into-vault.sh /path/to/your/vault
```

This writes them to `.agents/skills/` (Codex, Antigravity, Cursor, Gemini CLI) and `.claude/skills/` (Claude Code). Re-run it after `git pull` to update.

## First run

Open your notes folder in your tool and run `brain-check`. It reports what is missing, asks before changing anything, and makes sure your root `AGENTS.md` holds a `## Brain map` (where each thing lives) and a sources-of-truth table (which tool owns which fact). Every skill reads them, so the plugin adapts to your folders and your tools. Keep `AGENTS.md` as the only instruction file: Claude Code, Codex and Antigravity all read it. Do not add a `CLAUDE.md`, it would take precedence in Claude Code. Then run `interview` to fill the brain.

---

## En français

Les rituels quotidiens de ton second cerveau, dans tous tes outils IA : Claude Code, OpenAI Codex (ChatGPT) et Google Antigravity.

- **Vérifier le cerveau** : `brain-check`. **Brancher un outil** : `connect`. **Remplir le cerveau** : `interview`.
- **Début de session** : `welcome`. **Fin de session** : `done`.
- **Capturer** une idée : `capture`. **Vider l'inbox** : `inbox`.
- **Revue de la semaine** : `weekly-review`. **Consigner une décision** : `decision`. **Te faire challenger** sur une idée avant de trancher : `challenge`.
- **Passer le relais** à une autre conversation : `save-context`. **Fiche d'une personne** : `person`.
- **Rédiger** un mail ou un post dans ta voix : `draft`. **Enlever l'effet IA** d'un texte : `de-ai-ify`. **Faire un deck** à ta charte : `slides`.

**Installer** : suis le [guide rapide](INSTALL_FR.md), puis lance `brain-check` dans ton dossier de notes. Il te dit ce qui manque et te demande avant de changer quoi que ce soit. Garde `AGENTS.md` comme seul fichier d'instructions, sans `CLAUDE.md`.

**Appeler un skill** : `/unkillable:done` dans Claude Code, `$done` dans Codex, `/done` dans Antigravity. Tu peux aussi juste le dire : « on clôture la session », « vide mon inbox ».
