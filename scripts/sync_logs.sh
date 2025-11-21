#!/usr/bin/env bash
# Synchronise les journaux de communication entre squidCommunication et squidResearch.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESEARCH_ROOT="/home/lucas/tools/squidResearch"
COMM_LOG="$ROOT/communication_log.md"
RESEARCH_LOG="$RESEARCH_ROOT/communication_projet.md"
DIRECTION="push"
DRY_RUN=0

usage() {
  cat <<USAGE
Usage: $0 [--direction push|pull] [--dry-run]

  --direction push : copie communication_log.md -> squidResearch
  --direction pull : copie squidResearch -> communication_log.md
  --dry-run        : affiche les opérations sans copier
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --direction)
      shift
      DIRECTION="$1"
      ;;
    --dry-run)
      DRY_RUN=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
  shift || true
done

backup_file() {
  local file="$1"
  if [[ -f "$file" ]]; then
    local ts
    ts="$(date -u +%Y%m%d_%H%M%S)"
    local backup="${file}.bak_${ts}"
    if [[ $DRY_RUN -eq 1 ]]; then
      echo "[DRY-RUN] backup $file -> $backup"
    else
      cp "$file" "$backup"
    fi
  fi
}

case "$DIRECTION" in
  push)
    echo "➡️  Synchronisation vers squidResearch"
    [[ -f "$COMM_LOG" ]] || { echo "Fichier manquant: $COMM_LOG" >&2; exit 1; }
    backup_file "$RESEARCH_LOG"
    if [[ $DRY_RUN -eq 1 ]]; then
      echo "[DRY-RUN] cp $COMM_LOG -> $RESEARCH_LOG"
    else
      cp "$COMM_LOG" "$RESEARCH_LOG"
    fi
    ;;
  pull)
    echo "⬅️  Synchronisation depuis squidResearch"
    [[ -f "$RESEARCH_LOG" ]] || { echo "Fichier manquant: $RESEARCH_LOG" >&2; exit 1; }
    backup_file "$COMM_LOG"
    if [[ $DRY_RUN -eq 1 ]]; then
      echo "[DRY-RUN] cp $RESEARCH_LOG -> $COMM_LOG"
    else
      cp "$RESEARCH_LOG" "$COMM_LOG"
    fi
    ;;
  *)
    echo "Direction inconnue: $DIRECTION" >&2
    exit 1
    ;;
 esac

echo "✅ Terminé"
