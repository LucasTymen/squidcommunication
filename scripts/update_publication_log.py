#!/usr/bin/env python3
"""Met à jour le journal de publication avec les actions réalisées.

Usage:
    python scripts/update_publication_log.py --action published --article article-1 --platform linkedin --date 2025-12-15
    python scripts/update_publication_log.py --action prepared --article article-3
"""
from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent
LOG_FILE = ROOT / "docs" / "PUBLICATION_LOG.md"


def update_log(action: str, article_slug: str, platform: Optional[str] = None, date: Optional[str] = None) -> None:
    """Met à jour le journal de publication."""
    if not LOG_FILE.exists():
        print(f"❌ Fichier log non trouvé : {LOG_FILE}")
        return
    
    content = LOG_FILE.read_text(encoding="utf-8")
    
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    date_str = date or datetime.utcnow().strftime("%Y-%m-%d")
    
    # Extraire le numéro d'article du slug
    article_num_match = re.search(r"article-(\d+)", article_slug)
    article_num = article_num_match.group(1) if article_num_match else "?"
    
    if action == "published":
        # Ajouter dans la section Articles Publiés
        new_entry = f"| {article_num} | `{article_slug}` | [Titre] | {date_str} | {platform or 'Multi'} | ✅ Publié |\n"
        
        # Trouver la ligne après le header du tableau
        pattern = r"(\| # \| Slug \| Titre \| Date Publication \| Plateformes \| Statut \|\n\|.*?\n)"
        match = re.search(pattern, content)
        if match:
            content = content.replace(match.group(1), match.group(1) + new_entry)
            print(f"✅ Article ajouté dans Articles Publiés")
        
        # Retirer de Articles Prêts à Publier si présent
        pattern_ready = rf"\| {article_num} \| `{article_slug}`.*?\n"
        content = re.sub(pattern_ready, "", content)
        
    elif action == "prepared":
        # Mettre à jour le statut dans Articles Prêts à Publier
        pattern = rf"(\| {article_num} \| `{article_slug}` \| .*? \| )(.*?)( \| .*? \|)"
        replacement = r"\1🟢 Prêt\3"
        content = re.sub(pattern, replacement, content)
        print(f"✅ Statut mis à jour pour {article_slug}")
    
    # Ajouter entrée dans Historique
    history_entry = f"""
### [{now}] {action.capitalize()} - {article_slug}

**Action** : {action}
**Article** : {article_slug}
{f'**Plateforme** : {platform}' if platform else ''}
**Date** : {date_str}

---
"""
    
    # Trouver la section Historique
    history_pattern = r"(## 🔄 Historique des Actions\n)"
    history_match = re.search(history_pattern, content)
    if history_match:
        content = content.replace(history_match.group(1), history_match.group(1) + history_entry)
        print(f"✅ Entrée ajoutée dans Historique")
    
    # Mettre à jour la date de dernière mise à jour
    content = re.sub(
        r"\*\*Dernière mise à jour\*\* : \d{4}-\d{2}-\d{2}",
        f"**Dernière mise à jour** : {datetime.utcnow().strftime('%Y-%m-%d')}",
        content,
        count=1,
    )
    
    LOG_FILE.write_text(content, encoding="utf-8")
    print(f"✅ Journal de publication mis à jour")


def parse_args() -> argparse.Namespace:
    """Parse les arguments."""
    parser = argparse.ArgumentParser(description="Met à jour le journal de publication")
    parser.add_argument("--action", required=True, choices=["published", "prepared"], help="Action réalisée")
    parser.add_argument("--article", required=True, help="Slug de l'article")
    parser.add_argument("--platform", help="Plateforme (pour published)")
    parser.add_argument("--date", help="Date (format YYYY-MM-DD, défaut: aujourd'hui)")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    update_log(args.action, args.article, args.platform, args.date)

