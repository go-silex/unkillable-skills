# Installer le plugin Unkillable (5 minutes)

Le plugin ajoute à ton outil IA les rituels de ton second cerveau : vider l'inbox, clore une session, brancher un outil, faire le point en début de session. Il marche dans Claude Code, Codex (ChatGPT) et Antigravity.

## 1. Installer, selon ton outil

### Claude Code (app desktop ou terminal)

Dans une conversation, tape ces deux lignes, l'une après l'autre :

```
/plugin marketplace add go-silex/unkillable-skills
/plugin install unkillable@unkillable-companies
```

Puis, une seule fois, active les mises à jour automatiques : tape `/plugin`, va dans **Marketplaces**, choisis `unkillable-companies`, puis **Enable auto-update**. Les nouveaux skills arriveront tout seuls.

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

## Bon à savoir

- Le plugin ne crée jamais de `CLAUDE.md` : ton `AGENTS.md` suffit pour les trois outils. Si un `CLAUDE.md` existe dans ton dossier ou au-dessus, il passe devant : `brain-check` te le signale.
- Rien ne part de ton ordinateur sans ton accord : pas d'envoi de mail, pas d'écriture dans ton CRM sans un oui.
