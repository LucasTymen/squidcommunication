#!/usr/bin/env python3
"""Met à jour la structure des articles existants avec la nouvelle architecture.

Usage:
    python scripts/update_articles_structure.py [--articles 3,4,5] [--dry-run]
    
Exemples:
    # Mettre à jour tous les articles (3-9)
    python scripts/update_articles_structure.py
    
    # Mettre à jour uniquement les articles 3, 4, 5
    python scripts/update_articles_structure.py --articles 3,4,5
    
    # Dry-run pour voir ce qui sera fait
    python scripts/update_articles_structure.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

SUPER_ADMIN_USERS = {"lucas"}


def ensure_super_admin() -> None:
    current_user = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    if current_user not in SUPER_ADMIN_USERS:
        raise SystemExit(
            "Accès réservé au super-admin. Merci d'exécuter ce script depuis le compte autorisé."
        )


ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
TEMPLATES_DIR = ROOT / "templates"

# Mapping des articles existants avec leurs métadonnées
ARTICLE_METADATA = {
    2: {
        "slug": "article-2-architecture-docker-enriched",
        "title": "Architecture Docker Enriched",
        "summary": "Découverte de l'architecture Docker de SquidResearch et du module Enriched. Approche data-driven avec infographies sur la dockerisation, les principes de fonctionnement, les mappages et les structures réseau.",
        "category": "Technique/Docker",
        "keywords": ["docker", "architecture", "enrichissement", "B2B", "devops"],
    },
    3: {
        "slug": "article-3-algorithmes-matching-intelligents",
        "title": "Algorithmes matching intelligents",
        "summary": "Comment j'ai automatisé la compatibilité CV/offres avec un scoring mathématique transparent (0-100). Algorithme de matching multi-critères avec pondération intelligente.",
        "category": "Technique/Algo",
        "keywords": ["matching", "algorithme", "scoring", "IA", "recrutement"],
    },
    4: {
        "slug": "article-4-import-csv-intelligent",
        "title": "Import CSV intelligent",
        "summary": "Système d'import CSV intelligent avec validation automatique, détection de formats, et enrichissement automatique des données. Optimisation du workflow d'import de masse.",
        "category": "Technique/UX",
        "keywords": ["import", "CSV", "validation", "UX", "workflow"],
    },
    5: {
        "slug": "article-5-15-job-boards-francais",
        "title": "15 job boards français",
        "summary": "Analyse comparative de 15 job boards français : fonctionnalités, tarifs, efficacité. Retour d'expérience sur l'intégration multi-plateformes.",
        "category": "Business/Data",
        "keywords": ["job boards", "recrutement", "analyse", "comparatif", "France"],
    },
    6: {
        "slug": "article-6-enrichissement-multi-sources-tor",
        "title": "Enrichissement multi-sources Tor",
        "summary": "Pourquoi j'ai intégré Tor dans mon workflow B2B : protection IP, anonymisation, évite rate limiting. Architecture d'enrichissement multi-sources avec rotation IP.",
        "category": "Technique/Sécurité",
        "keywords": ["enrichissement", "Tor", "sécurité", "anonymisation", "B2B"],
    },
    7: {
        "slug": "article-7-securisation-complete",
        "title": "Sécurisation complète",
        "summary": "Sécurisation complète d'un SaaS B2B : authentification, autorisation, protection données, logs audit, conformité RGPD. Retour d'expérience sur les bonnes pratiques.",
        "category": "Technique/Sécurité",
        "keywords": ["sécurité", "RGPD", "authentification", "conformité", "SaaS"],
    },
    8: {
        "slug": "article-8-ux-gamification",
        "title": "UX Gamification",
        "summary": "Comment j'ai intégré la gamification dans l'UX de SquidResearch : badges, scores, progression, motivation utilisateur. Impact mesuré sur l'engagement.",
        "category": "UX/Design",
        "keywords": ["UX", "gamification", "engagement", "design", "utilisateur"],
    },
    9: {
        "slug": "article-9-google-oauth-crud-complet",
        "title": "Google OAuth CRUD complet",
        "summary": "Intégration Google OAuth complète avec CRUD : authentification, gestion tokens, synchronisation données, gestion erreurs. Architecture scalable pour SaaS B2B.",
        "category": "Technique/Auth",
        "keywords": ["OAuth", "Google", "authentification", "CRUD", "API"],
    },
}


def create_new_campaign_json(article_num: int, metadata: Dict, dry_run: bool = False) -> Dict:
    """Crée un campaign.json avec la nouvelle structure."""
    slug = metadata["slug"]
    title = metadata["title"]
    summary = metadata["summary"]
    category = metadata["category"]
    keywords = metadata["keywords"]
    
    # Extraire le slug sans préfixe article-X-
    slug_base = slug.replace(f"article-{article_num}-", "")
    campaign_id = f"2025-01-article-{article_num}-{slug_base}"
    
    # Générer hashtags à partir des keywords
    hashtags = [f"#{kw.capitalize()}" for kw in keywords[:5]] + ["#SquidResearch"]
    
    campaign_data = {
        "schema_version": "1.0",
        "campaign_id": campaign_id,
        "slug": slug,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "owner": "Lucas Tymen",
        "status": "draft",
        "objective": f"Partager {title.lower()} : {summary[:100]}...",
        "message_key": f"{title} - Retour d'expérience SquidResearch",
        "narrative_arc": {
            "episode": article_num,
            "series": "Articles LinkedIn One-Page - SquidResearch",
            "summary": summary,
            "next_episode": f"article-{article_num + 1}-..." if article_num < 9 else None,
        },
        "platforms": ["linkedin", "facebook", "threads", "instagram"],
        "kpis": {
            "target": {
                "linkedin_impressions": 500,
                "linkedin_engagement": 30,
                "cta_clicks": 15,
            },
            "actual": {
                "linkedin_impressions": 0,
                "linkedin_engagement": 0,
                "cta_clicks": 0,
            },
            "source": "manual",
        },
        "content": {
            "title": title,
            "summary": summary,
            "angle": "data-driven",
            "hashtags": hashtags,
            "cta": f"Découvrez {title.lower()} sur SquidResearch. Partagez vos expériences en commentaire.",
            "assets": {
                "original": f"articles/{slug}/assets/original/",
                "sanitized": f"articles/{slug}/assets/sanitized/",
            },
        },
        "seo": {
            "meta_title": f"{title} | SquidResearch",
            "meta_description": summary[:155],
            "keywords": keywords,
            "slug": slug,
            "canonical": f"https://communication.squidresearch.com/articles/{slug}",
            "schema_type": "Article",
            "og_image": f"https://communication.squidresearch.com/og-article-{article_num}.png",
            "og_type": "article",
            "twitter_card": "summary_large_image",
            "lang": "fr",
            "alternate_langs": [],
        },
        "posts": [],
        "security_checklist": {
            "no_ip_visible": False,
            "credentials_masked": False,
            "no_tokens": False,
            "client_data_anonymized": False,
            "internal_urls_masked": False,
            "env_vars_hidden": False,
            "validation_script_run": False,
            "validated_by": "",
            "validated_at": "",
        },
        "sync": {
            "source_repo": "squidResearch",
            "last_pulled": None,
            "last_pushed": None,
            "lock": False,
        },
        "notes": [
            f"Article {article_num} de la série SquidResearch",
            f"Catégorie : {category}",
            "Format one-page pour éviter carrousels chronophages",
            "Ton factuel, pas marketing, expérience personnelle",
        ],
    }
    
    return campaign_data


def ensure_article_structure(article_num: int, metadata: Dict, dry_run: bool = False) -> None:
    """Assure que l'article a la structure complète."""
    slug = metadata["slug"]
    article_dir = ARTICLES_DIR / slug
    
    if not article_dir.exists():
        if dry_run:
            print(f"[DRY-RUN] Créerait : {article_dir}")
        else:
            article_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Dossier créé : {article_dir}")
    
    # Créer campaign.json avec nouvelle structure
    campaign_json_path = article_dir / "campaign.json"
    campaign_data = create_new_campaign_json(article_num, metadata, dry_run)
    
    if dry_run:
        print(f"[DRY-RUN] Écrirait campaign.json : {campaign_json_path}")
        print(json.dumps(campaign_data, indent=2, ensure_ascii=False))
    else:
        with campaign_json_path.open("w", encoding="utf-8") as f:
            json.dump(campaign_data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"✅ campaign.json créé/mis à jour : {campaign_json_path}")
    
    # Créer article.md si n'existe pas
    article_md_path = article_dir / "article.md"
    if not article_md_path.exists():
        template_content = f"""# {metadata['title']}

{metadata['summary']}

---

## Introduction

[TODO: Rédiger l'introduction de l'article]

## Contenu Principal

[TODO: Rédiger le contenu principal]

## Conclusion

[TODO: Rédiger la conclusion]

---

**Catégorie** : {metadata['category']}  
**Mots-clés** : {', '.join(metadata['keywords'])}
"""
        if dry_run:
            print(f"[DRY-RUN] Créerait article.md : {article_md_path}")
        else:
            article_md_path.write_text(template_content, encoding="utf-8")
            print(f"✅ article.md créé : {article_md_path}")
    
    # Créer structure platforms/
    platforms_dir = article_dir / "platforms"
    if dry_run:
        print(f"[DRY-RUN] Créerait structure platforms/")
    else:
        for platform in ["linkedin", "facebook", "threads", "instagram"]:
            platform_dir = platforms_dir / platform
            platform_dir.mkdir(parents=True, exist_ok=True)
            assets_dir = platform_dir / "assets"
            assets_dir.mkdir(parents=True, exist_ok=True)
        print(f"✅ Structure platforms/ créée")
    
    # Créer structure assets/
    assets_dir = article_dir / "assets"
    if dry_run:
        print(f"[DRY-RUN] Créerait structure assets/")
    else:
        (assets_dir / "original").mkdir(parents=True, exist_ok=True)
        (assets_dir / "sanitized").mkdir(parents=True, exist_ok=True)
        print(f"✅ Structure assets/ créée")


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Met à jour la structure des articles existants",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python scripts/update_articles_structure.py
  python scripts/update_articles_structure.py --articles 3,4,5
  python scripts/update_articles_structure.py --dry-run
""",
    )
    parser.add_argument(
        "--articles",
        default="3,4,5,6,7,8,9",
        help="Numéros d'articles à traiter (défaut: 3,4,5,6,7,8,9)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simuler les modifications sans créer de fichiers",
    )
    return parser.parse_args(argv)


def main() -> None:
    """Point d'entrée principal."""
    ensure_super_admin()
    args = parse_args()
    
    # Parser les numéros d'articles
    article_nums = [int(n.strip()) for n in args.articles.split(",")]
    
    print(f"📝 Mise à jour structure articles : {', '.join(map(str, article_nums))}")
    if args.dry_run:
        print("   Mode DRY-RUN (simulation)\n")
    
    updated_count = 0
    
    for article_num in article_nums:
        if article_num not in ARTICLE_METADATA:
            print(f"⚠️  Article {article_num} non trouvé dans les métadonnées")
            continue
        
        metadata = ARTICLE_METADATA[article_num]
        slug = metadata["slug"]
        
        print(f"\n🎯 Article {article_num} : {slug}")
        
        try:
            ensure_article_structure(article_num, metadata, args.dry_run)
            updated_count += 1
        except Exception as e:
            print(f"❌ Erreur : {e}")
    
    if args.dry_run:
        print(f"\n[DRY-RUN] {updated_count} article(s) simulé(s)")
    else:
        print(f"\n✅ {updated_count} article(s) mis à jour avec succès")
        print(f"\n📝 Prochaines étapes :")
        print(f"   1. Vérifier les campaign.json créés")
        print(f"   2. Rédiger les article.md si nécessaire")
        print(f"   3. Générer déclinaisons : python scripts/generate_platform_variants.py <slug>")


if __name__ == "__main__":
    main()

