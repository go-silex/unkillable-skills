# Installer le plugin Unkillable (5 minutes)

Le plugin ajoute à ton outil IA les rituels de ton second cerveau : vider l'inbox, clore une session, brancher un outil, faire le point en début de session. Il marche dans Claude Code, Codex (ChatGPT) et Antigravity.

## 0. Ce qu'il te faut

- **Claude Code** (app Claude desktop, onglet Code, ou terminal) : un compte Claude payant (Pro, Max, Team ou Enterprise). Rien d'autre à installer.
- **Codex ou Antigravity** : en plus, **Git**, un petit outil souvent absent des ordinateurs neufs. Vérifie dans le Terminal (Mac) ou PowerShell (Windows) avec `git --version`. Une réponse du type `git version 2.x` : c'est bon. Sinon :
  - **Mac** : tape `xcode-select --install`, puis clique **Installer** dans la fenêtre qui s'ouvre (5 à 10 minutes, ton mot de passe Mac peut être demandé). Ça installe aussi Python, utile pour le skill `slides`.
  - **Windows** : installe **Git for Windows** depuis [git-scm.com/downloads/win](https://git-scm.com/downloads/win), options par défaut, en gardant cochée l'option qui ajoute Git au PATH.
  - Puis ferme et rouvre ton outil pour qu'il voie Git.

## 1. Installer, selon ton outil

### Claude Code (app desktop ou terminal)

Dans une conversation, tape ces deux lignes, l'une après l'autre (copie-colle la première, elle est longue) :

```
/plugin marketplace add https://raw.githubusercontent.com/go-silex/unkillable-skills/main/install/claude-marketplace.json
/plugin install unkillable@unkillable-companies
```

Puis, une seule fois, active les mises à jour automatiques : tape `/plugin`, va dans **Marketplaces**, choisis `unkillable-companies`, puis **Enable auto-update**. Les nouveaux skills arriveront tout seuls.

Cette méthode télécharge le plugin en ZIP depuis GitHub : pas besoin de Git. Si tu as déjà Git, `/plugin marketplace add go-silex/unkillable-skills` marche aussi (garde une seule des deux méthodes).

### Codex ou l'app ChatGPT

Dans un terminal :

```
codex plugin marketplace add go-silex/unkillable-skills
```

Puis dans l'app ChatGPT (ou `/plugins` dans Codex) : **Plugins**, marketplace **Unkillable Companies**, installe **Unkillable**, et ouvre une nouvelle conversation.

Pour recevoir les nouveaux skills : `codex plugin marketplace upgrade`, puis redémarre l'app.

### Antigravity

Dans un terminal :

```
agy plugin install https://github.com/go-silex/unkillable-skills
```

Pour recevoir les nouveaux skills : relance la même commande.

## 2. Ouvrir ton cerveau

Ouvre ton dossier de notes dans l'outil (le dossier qui contient ton `AGENTS.md`). Puis lance `brain-check` : il vérifie que tout est en place et te demande avant de changer quoi que ce soit.

## 3. Les commandes du quotidien

| Pour… | Claude Code | Codex | Antigravity |
|---|---|---|---|
| Faire le point en début de session | `/unkillable:welcome` | `$welcome` | `/welcome` |
| Clore une session | `/unkillable:done` | `$done` | `/done` |
| Noter une idée vite | `/unkillable:capture` | `$capture` | `/capture` |
| Ranger l'inbox | `/unkillable:inbox` | `$inbox` | `/inbox` |
| Brancher un nouvel outil (CRM, mail…) | `/unkillable:connect` | `$connect` | `/connect` |
| Te faire challenger avant de trancher | `/unkillable:challenge` | `$challenge` | `/challenge` |

Tu peux aussi le dire avec tes mots : « on reprend », « on clôture », « vide mon inbox », « j'ai connecté Attio ».

La liste complète des skills est dans le [README](README.md).

## Si ça bloque

| Message | Solution |
|---|---|
| `Executable not found in $PATH: "git"`, `Command 'git' not found` (Windows), `Failed to clone`, `git: command not found` | Git manque. Claude Code : utilise la première commande de l'étape 1 (l'adresse en `https://`), elle n'a pas besoin de Git. Codex ou Antigravity : installe Git (étape 0), puis ferme et rouvre l'outil. |
| `xcrun: error: invalid active developer path` (Mac) | Les outils Apple sont absents ou cassés après une mise à jour de macOS : `xcode-select --install`, puis rouvre l'outil. |
| `Plugin "unkillable" not found in marketplace` | La première commande (`marketplace add`) a échoué ou n'a pas été lancée : relance-la, puis la seconde. |
| Les commandes `/unkillable:` n'apparaissent pas | Ouvre une nouvelle conversation (ou redémarre l'app). |
| `python3: command not found` pendant `slides` | Pas bloquant : le deck est fait quand même. Pour le contrôle automatique : `xcode-select --install` (Mac) ou Python depuis python.org (Windows). |

## Bon à savoir

- `welcome`, `person` et `connect` lisent ton agenda, tes mails ou ton CRM seulement si ces outils sont **connectés** à ton IA (dans l'app Claude : Paramètres, Connecteurs). Sans connecteur, ils travaillent avec ton cerveau seul.
- Le plugin ne crée jamais de `CLAUDE.md` : ton `AGENTS.md` suffit pour les trois outils. Si un `CLAUDE.md` existe dans ton dossier ou au-dessus, il passe devant : `brain-check` te le signale.
- Rien ne part de ton ordinateur sans ton accord : pas d'envoi de mail, pas d'écriture dans ton CRM sans un oui.
