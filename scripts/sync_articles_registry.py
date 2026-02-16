#!/usr/bin/env python3
"""
Sync articles-complete.json → articles/

Crée les dossiers articles/ avec campaign.json + article.md pour les articles
published ou ready qui n'existent pas encore dans articles/.

Usage:
    python scripts/sync_articles_registry.py [--dry-run]
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "articles-complete.json"
ARTICLES_DIR = ROOT / "articles"


def load_registry() -> dict:
    with open(REGISTRY, encoding="utf-8") as f:
        return json.load(f)


def article_to_campaign(article: dict) -> dict:
    """Convertit un article du registre en format campaign.json."""
    content = article.get("content_markdown", "")
    summary = content.split("\n\n")[0][:300] if content else ""
    seo = article.get("seo", {}) or {}
    planning = article.get("planning", {}) or {}
    slug = article.get("slug", article.get("id", ""))

    return {
        "schema_version": "2.0",
        "campaign_id": article.get("id", ""),
        "slug": slug,
        "created_at": planning.get("publish_date", "2026-01-01") + "T14:00:00Z",
        "updated_at": planning.get("publish_date", "2026-01-01") + "T14:00:00Z",
        "owner": "Lucas Tymen",
        "status": article.get("status", "draft"),
        "objective": summary,
        "content": {
            "title": article.get("title", ""),
            "summary": summary,
            "category": article.get("category", "Général").split("/")[-1],
            "tags": seo.get("tags", [])[:5],
        },
        "seo": {
            "meta_title": seo.get("meta_title", article.get("title", "")),
            "meta_description": seo.get("meta_description", summary[:160]),
            "keywords": seo.get("primary_keywords", []),
            "slug": slug,
            "schema_type": "Article",
            "lang": "fr",
        },
        "source": "articles-complete.json",
    }


def sync_articles(dry_run: bool = False) -> tuple[int, int]:
    """Sync les articles published/ready du registre vers articles/."""
    if not REGISTRY.exists():
        print(f"❌ Registre introuvable: {REGISTRY}")
        return 0, 0

    data = load_registry()
    articles = data.get("articles", [])
    created = 0
    skipped = 0

    for article in articles:
        status = article.get("status", "draft")
        if status not in ("published", "ready"):
            skipped += 1
            continue

        slug = article.get("slug", article.get("id", ""))
        folder_name = slug
        article_dir = ARTICLES_DIR / folder_name

        if article_dir.exists() and (article_dir / "campaign.json").exists():
            skipped += 1
            continue

        campaign = article_to_campaign(article)
        content = article.get("content_markdown", "")

        if dry_run:
            print(f"[DRY-RUN] Créerait {folder_name}/")
            created += 1
            continue

        article_dir.mkdir(parents=True, exist_ok=True)

        campaign_path = article_dir / "campaign.json"
        with open(campaign_path, "w", encoding="utf-8") as f:
            json.dump(campaign, f, ensure_ascii=False, indent=2)

        article_path = article_dir / "article.md"
        with open(article_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ {folder_name}/")
        created += 1

    return created, skipped


def main():
    parser = argparse.ArgumentParser(description="Sync articles-complete.json → articles/")
    parser.add_argument("--dry-run", action="store_true", help="Afficher sans écrire")
    args = parser.parse_args()

    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    created, skipped = sync_articles(dry_run=args.dry_run)

    print(f"\n📊 Créés: {created}, Ignorés: {skipped}")


if __name__ == "__main__":
    main()
