#!/usr/bin/env python3
"""Aperçu des déclinaisons multi-plateformes d'un article.

Usage:
    python scripts/preview_article.py <article-slug> [--platform linkedin] [--format terminal|html]
    
Exemples:
    # Aperçu de toutes les plateformes (terminal)
    python scripts/preview_article.py article-3-algorithmes-matching-intelligents
    
    # Aperçu LinkedIn uniquement
    python scripts/preview_article.py article-3 --platform linkedin
    
    # Aperçu HTML (pour ouvrir dans un navigateur)
    python scripts/preview_article.py article-3 --format html > preview.html
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"


def extract_content_from_markdown(file_path: Path) -> Dict[str, str]:
    """Extrait le contenu et les métadonnées d'un fichier markdown."""
    if not file_path.exists():
        return {}
    
    content = file_path.read_text(encoding="utf-8")
    
    # Extraire la section Contenu
    content_match = re.search(r"## Contenu\n\n(.*?)\n\n---", content, re.DOTALL)
    post_content = content_match.group(1).strip() if content_match else ""
    
    # Extraire les métadonnées
    metadata = {}
    length_match = re.search(r"\*\*Longueur\*\* : (\d+)", content)
    if length_match:
        metadata["length"] = int(length_match.group(1))
    
    tone_match = re.search(r"\*\*Ton\*\* : (.+)", content)
    if tone_match:
        metadata["tone"] = tone_match.group(1).strip()
    
    status_match = re.search(r"\*\*Statut\*\* : (.+)", content)
    if status_match:
        metadata["status"] = status_match.group(1).strip()
    
    return {
        "content": post_content,
        "metadata": metadata,
    }


def preview_terminal(article_slug: str, platforms: List[str]) -> None:
    """Affiche un aperçu en terminal."""
    article_dir = ARTICLES_DIR / article_slug
    
    if not article_dir.exists():
        print(f"❌ Article non trouvé : {article_dir}")
        return
    
    # Charger campaign.json
    campaign_json_path = article_dir / "campaign.json"
    if not campaign_json_path.exists():
        print(f"❌ campaign.json non trouvé")
        return
    
    with campaign_json_path.open("r", encoding="utf-8") as f:
        article_data = json.load(f)
    
    title = article_data.get("content", {}).get("title", article_slug)
    
    print("=" * 80)
    print(f"APERÇU ARTICLE : {title}")
    print(f"Slug : {article_slug}")
    print("=" * 80)
    print()
    
    for platform in platforms:
        post_file = article_dir / "platforms" / platform / "post-01.md"
        
        if not post_file.exists():
            print(f"⚠️  {platform.upper()} : Fichier non trouvé")
            print()
            continue
        
        data = extract_content_from_markdown(post_file)
        content = data.get("content", "")
        metadata = data.get("metadata", {})
        
        print("-" * 80)
        print(f"📱 {platform.upper()}")
        print("-" * 80)
        
        if metadata.get("status"):
            print(f"Statut : {metadata['status']}")
        if metadata.get("length"):
            print(f"Longueur : {metadata['length']} caractères")
        if metadata.get("tone"):
            print(f"Ton : {metadata['tone']}")
        print()
        
        # Afficher le contenu avec wrap intelligent
        lines = content.split("\n")
        for line in lines:
            if len(line) > 78:
                # Découper les longues lignes
                words = line.split()
                current_line = ""
                for word in words:
                    if len(current_line + " " + word) <= 78:
                        current_line += (" " if current_line else "") + word
                    else:
                        if current_line:
                            print(current_line)
                        current_line = word
                if current_line:
                    print(current_line)
            else:
                print(line)
        
        print()
        print()


def preview_html(article_slug: str, platforms: List[str]) -> str:
    """Génère un aperçu HTML."""
    article_dir = ARTICLES_DIR / article_slug
    
    if not article_dir.exists():
        return f"<p>❌ Article non trouvé : {article_slug}</p>"
    
    # Charger campaign.json
    campaign_json_path = article_dir / "campaign.json"
    if not campaign_json_path.exists():
        return "<p>❌ campaign.json non trouvé</p>"
    
    with campaign_json_path.open("r", encoding="utf-8") as f:
        article_data = json.load(f)
    
    title = article_data.get("content", {}).get("title", article_slug)
    summary = article_data.get("content", {}).get("summary", "")
    
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aperçu : {title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
            color: #333;
        }}
        .header {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            margin: 0 0 10px 0;
            color: #2563eb;
        }}
        .header .slug {{
            color: #666;
            font-size: 14px;
        }}
        .platform {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .platform h2 {{
            margin: 0 0 20px 0;
            color: #2563eb;
            border-bottom: 2px solid #2563eb;
            padding-bottom: 10px;
        }}
        .metadata {{
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
            padding: 15px;
            background: #f9fafb;
            border-radius: 4px;
            font-size: 14px;
        }}
        .metadata span {{
            color: #666;
        }}
        .metadata strong {{
            color: #333;
        }}
        .content {{
            line-height: 1.8;
            white-space: pre-wrap;
            font-size: 16px;
        }}
        .content p {{
            margin: 0 0 15px 0;
        }}
        .status-draft {{
            color: #f59e0b;
        }}
        .status-ready {{
            color: #10b981;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <div class="slug">Slug : {article_slug}</div>
        {f'<p style="color: #666; margin-top: 15px;">{summary}</p>' if summary else ''}
    </div>
"""
    
    for platform in platforms:
        post_file = article_dir / "platforms" / platform / "post-01.md"
        
        if not post_file.exists():
            html += f"""
    <div class="platform">
        <h2>📱 {platform.upper()}</h2>
        <p>⚠️ Fichier non trouvé</p>
    </div>
"""
            continue
        
        data = extract_content_from_markdown(post_file)
        content = data.get("content", "")
        metadata = data.get("metadata", {})
        
        status = metadata.get("status", "draft")
        status_class = "status-ready" if status == "ready" else "status-draft"
        
        html += f"""
    <div class="platform">
        <h2>📱 {platform.upper()}</h2>
        <div class="metadata">
            <span><strong>Statut:</strong> <span class="{status_class}">{status}</span></span>
            <span><strong>Longueur:</strong> {metadata.get('length', 'N/A')} caractères</span>
            <span><strong>Ton:</strong> {metadata.get('tone', 'N/A')}</span>
        </div>
        <div class="content">{content.replace(chr(10), '<br>')}</div>
    </div>
"""
    
    html += """
</body>
</html>
"""
    
    return html


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Aperçu des déclinaisons multi-plateformes d'un article",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python scripts/preview_article.py article-3-algorithmes-matching-intelligents
  python scripts/preview_article.py article-3 --platform linkedin
  python scripts/preview_article.py article-3 --format html > preview.html
""",
    )
    parser.add_argument(
        "article_slug",
        help="Slug de l'article (sans préfixe 'article-' si présent)",
    )
    parser.add_argument(
        "--platform",
        default=None,
        choices=["linkedin", "facebook", "threads", "instagram"],
        help="Aperçu d'une seule plateforme (défaut: toutes)",
    )
    parser.add_argument(
        "--format",
        default="terminal",
        choices=["terminal", "html"],
        help="Format d'aperçu (défaut: terminal)",
    )
    return parser.parse_args(argv)


def main() -> None:
    """Point d'entrée principal."""
    args = parse_args()
    
    # Normaliser le slug
    slug = args.article_slug.replace("article-", "") if args.article_slug.startswith("article-") else args.article_slug
    article_slug = f"article-{slug}" if not slug.startswith("article-") else slug
    
    # Déterminer les plateformes
    if args.platform:
        platforms = [args.platform]
    else:
        platforms = ["linkedin", "facebook", "threads", "instagram"]
    
    if args.format == "html":
        html = preview_html(article_slug, platforms)
        print(html)
    else:
        preview_terminal(article_slug, platforms)


if __name__ == "__main__":
    main()

