#!/usr/bin/env bash
# Copies the skills into a vault, for tools or setups without plugin support.
# Claude Code reads .claude/skills/, Codex and Antigravity read .agents/skills/.
# Usage: bash scripts/install-into-vault.sh /path/to/vault
set -euo pipefail
VAULT="${1:?usage: install-into-vault.sh /path/to/vault}"
SRC="$(cd "$(dirname "$0")/.." && pwd)/skills"
[ -d "$VAULT" ] || { echo "Not a folder: $VAULT" >&2; exit 1; }
for target in "$VAULT/.agents/skills" "$VAULT/.claude/skills"; do
  mkdir -p "$target"
  for s in "$SRC"/*/; do
    name="$(basename "$s")"
    rm -rf "${target:?}/$name"
    cp -R "$s" "$target/$name"
  done
  echo "Copied $(ls "$SRC" | wc -l | tr -d ' ') skills into $target"
done
