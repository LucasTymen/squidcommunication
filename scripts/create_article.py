#!/usr/bin/env python3
"""Génère un nouvel article de blog automatisé avec structure complète.

Usage:
    python scripts/create_article.py "titre-article" \
        --title "Titre complet de l'article" \
        --summary "Résumé de l'article" \
        --keywords "mot-clé1,mot-clé2,mot-clé3" \
        --tags "Tag1,Tag2" \
        --category "technique" \
        --author "Lucas Tymen"
"""
from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import quote

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


def slugify(text: str) -> str:
    """Convertit un texte en slug URL-friendly."""
    # Normalise et enlève les accents (basique)
    text = text.lower()
    text = re.sub(r"[àáâãäå]", "a", text)
    text = re.sub(r"[èéêë]", "e", text)
    text = re.sub(r"[ìíîï]", "i", text)
    text = re.sub(r"[òóôõö]", "o", text)
    text = re.sub(r"[ùúûü]", "u", text)
    text = re.sub(r"[ç]", "c", text)
    text = re.sub(r"[ñ]", "n", text)
    # Remplace les caractères spéciaux par des tirets
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text


def iso_now() -> str:
    """Retourne l'heure actuelle en format ISO 8601."""
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def generate_canonical_url(slug: str, base_url: str = "https://communication.squidresearch.com") -> str:
    """Génère l'URL canonique d'un article."""
    return f"{base_url}/blog/{slug}"


def generate_og_image_url(slug: str, base_url: str = "https://communication.squidresearch.com") -> str:
    """Génère l'URL de l'image Open Graph."""
    return f"{base_url}/og-{slug}.png"


def build_article_json(
    slug: str,
    title: str,
    summary: str,
    keywords: List[str],
    tags: List[str],
    category: str,
    author: str,
    meta_title: Optional[str] = None,
    meta_description: Optional[str] = None,
) -> Dict:
    """Construit la structure JSON complète d'un article."""
    now = iso_now()
    date_str = now.split("T")[0]  # YYYY-MM-DD
    campaign_id = f"{date_str}-{slug}"

    # Meta title et description par défaut si non fournis
    if not meta_title:
        meta_title = f"{title} | SquidResearch Blog"
    if not meta_description:
        meta_description = summary[:160] if len(summary) > 160 else summary

    article_data: Dict[str, object] = {
        "schema_version": "1.0",
        "campaign_id": campaign_id,
        "slug": slug,
        "created_at": now,
        "updated_at": now,
        "owner": author,
        "status": "draft",
        "objective": f"Article de blog : {title}",
        "message_key": summary[:100],
        "platforms": ["blog"],
        "kpis": {
            "target": {
                "page_views": 100,
                "engagement_time": 120,  # secondes
                "cta_clicks": 10,
            },
            "actual": {
                "page_views": 0,
                "engagement_time": 0,
                "cta_clicks": 0,
            },
            "source": "manual",
        },
        "content": {
            "summary": summary,
            "title": title,
            "angle": "blog",
            "hashtags": tags,
            "cta": "Découvrir SquidResearch",
            "category": category,
            "tags": tags,
            "author": author,
            "assets": {
                "original": f"articles/{slug}/assets/original/",
                "sanitized": f"articles/{slug}/assets/sanitized/",
            },
        },
        "seo": {
            "meta_title": meta_title,
            "meta_description": meta_description,
            "keywords": keywords,
            "slug": slug,
            "canonical": generate_canonical_url(slug),
            "schema_type": "Article",
            "og_image": generate_og_image_url(slug),
            "og_type": "article",
            "twitter_card": "summary_large_image",
            "lang": "fr",
            "alternate_langs": [],
        },
        "posts": [
            {
                "post_id": "blog-article-01",
                "platform": "blog",
                "format": "article",
                "status": "draft",
                "template": "templates/blog-article.md",
                "scheduled_date": None,
                "file": "article.md",
                "analytics": {
                    "page_views": 0,
                    "engagement_time": 0,
                    "social_shares": 0,
                },
            }
        ],
        "security_checklist": {
            "no_ip_visible": True,
            "credentials_masked": True,
            "no_tokens": True,
            "client_data_anonymized": True,
            "internal_urls_masked": True,
            "env_vars_hidden": True,
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
        "notes": [],
    }
    return article_data


def ensure_directory(path: Path, dry_run: bool = False) -> None:
    """Crée un répertoire s'il n'existe pas."""
    if path.exists():
        return
    if dry_run:
        print(f"[DRY-RUN] mkdir -p {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)


def load_template(template_path: Path) -> str:
    """Charge un template ou retourne un template par défaut."""
    if template_path.exists():
        return template_path.read_text(encoding="utf-8")
    # Template par défaut pour article de blog
    return """# {title}

**Auteur** : {author}  
**Date** : {date}  
**Catégorie** : {category}  
**Tags** : {tags}

---

## Résumé

{summary}

---

## Introduction

[TODO: Rédiger l'introduction]

---

## Section 1

[TODO: Contenu de la première section]

---

## Section 2

[TODO: Contenu de la deuxième section]

---

## Conclusion

[TODO: Rédiger la conclusion]

---

## Ressources

- [Lien utile 1](#)
- [Lien utile 2](#)

---

**Call-to-Action** : Découvrez [SquidResearch](https://squidresearch.com) pour automatiser vos correspondances et enrichissement B2B.
"""


def create_article_file(
    article_dir: Path,
    template_content: str,
    context: Dict[str, str],
    dry_run: bool = False,
) -> None:
    """Crée le fichier article.md avec le template rempli."""
    article_path = article_dir / "article.md"
    filled_content = template_content.format(**context)
    
    if dry_run:
        print(f"[DRY-RUN] would write {article_path}")
        print("\n" + "="*80)
        print(filled_content)
        print("="*80)
    else:
        article_path.write_text(filled_content, encoding="utf-8")
        print(f"✅ Article créé : {article_path}")


def create_readme(article_dir: Path, slug: str, title: str, dry_run: bool = False) -> None:
    """Crée un README pour l'article."""
    readme_path = article_dir / "README.md"
    readme_content = f"""# {title}

Article de blog : {slug}

## Structure

- `campaign.json` : Métadonnées complètes de l'article (SEO, KPIs, etc.)
- `article.md` : Contenu Markdown de l'article
- `assets/original/` : Assets originaux (non versionnés)
- `assets/sanitized/` : Assets sanitizés pour publication (versionnés)

## Workflow

1. ✅ Structure créée
2. 📝 Rédiger le contenu dans `article.md`
3. 🎨 Ajouter les assets dans `assets/sanitized/`
4. ✅ Valider la sécurité (`scripts/validate-campaign.sh`)
5. 🚀 Publier (Next.js génère automatiquement la page)
"""
    if dry_run:
        print(f"[DRY-RUN] would write {readme_path}")
    else:
        readme_path.write_text(readme_content, encoding="utf-8")
        print(f"✅ README créé : {readme_path}")


def write_campaign_json(article_dir: Path, data: Dict, dry_run: bool = False) -> None:
    """Écrit le fichier campaign.json."""
    json_path = article_dir / "campaign.json"
    if dry_run:
        print(f"[DRY-RUN] would write {json_path}")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        with json_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"✅ campaign.json créé : {json_path}")


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Génère un nouvel article de blog avec structure complète",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python scripts/create_article.py "automatisation-recherche-emploi" \\
      --title "Comment automatiser votre recherche d'emploi avec Python" \\
      --summary "Guide complet pour automatiser vos candidatures" \\
      --keywords "python,automatisation,recherche-emploi" \\
      --tags "Python,Productivity" \\
      --category "technique"

  python scripts/create_article.py "gain-temps-candidature" \\
      --title "Gain de temps : 93% sur vos candidatures" \\
      --summary "Comment réduire de 30 min à 2 min par candidature" \\
      --keywords "gain-temps,productivite,roi" \\
      --category "business" \\
      --dry-run
""",
    )
    parser.add_argument("slug", help="Slug de l'article (ex: automatisation-recherche-emploi)")
    parser.add_argument(
        "--title",
        required=True,
        help="Titre complet de l'article",
    )
    parser.add_argument(
        "--summary",
        required=True,
        help="Résumé de l'article (utilisé pour meta description)",
    )
    parser.add_argument(
        "--keywords",
        default="",
        help="Mots-clés SEO séparés par des virgules (ex: python,automatisation,roi)",
    )
    parser.add_argument(
        "--tags",
        default="",
        help="Tags de catégorisation séparés par des virgules (ex: Python,Productivity)",
    )
    parser.add_argument(
        "--category",
        default="technique",
        choices=["technique", "business", "tutoriel", "cas-usage", "news"],
        help="Catégorie de l'article (défaut: technique)",
    )
    parser.add_argument(
        "--author",
        default="Lucas Tymen",
        help="Auteur de l'article (défaut: Lucas Tymen)",
    )
    parser.add_argument(
        "--meta-title",
        dest="meta_title",
        help="Titre SEO personnalisé (défaut: généré automatiquement)",
    )
    parser.add_argument(
        "--meta-description",
        dest="meta_description",
        help="Description SEO personnalisée (défaut: utilise --summary)",
    )
    parser.add_argument(
        "--template",
        help="Chemin vers un template Markdown personnalisé (optionnel)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simule la création sans écrire de fichiers",
    )
    return parser.parse_args(argv)


def main() -> None:
    """Point d'entrée principal."""
    ensure_super_admin()
    args = parse_args()

    # Validation et normalisation du slug
    slug_base = slugify(args.slug)
    article_dir = ARTICLES_DIR / f"article-{slug_base}"

    if article_dir.exists() and not args.dry_run:
        raise SystemExit(f"❌ L'article existe déjà : {article_dir}")

    # Parsing des listes
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()] if args.keywords else []
    tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else []

    # Construction des données JSON
    article_data = build_article_json(
        slug=slug_base,
        title=args.title,
        summary=args.summary,
        keywords=keywords,
        tags=tags,
        category=args.category,
        author=args.author,
        meta_title=args.meta_title,
        meta_description=args.meta_description,
    )

    # Chargement du template
    if args.template:
        template_path = Path(args.template)
    else:
        template_path = TEMPLATES_DIR / "blog-article.md"
    
    template_content = load_template(template_path)

    # Context pour remplir le template
    context = {
        "title": args.title,
        "author": args.author,
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "category": args.category,
        "tags": ", ".join(tags) if tags else "Général",
        "summary": args.summary,
    }

    # Création de la structure
    print(f"📝 Création de l'article : {slug_base}")
    print(f"   Dossier : {article_dir}")

    ensure_directory(article_dir, args.dry_run)
    ensure_directory(article_dir / "assets" / "original", args.dry_run)
    ensure_directory(article_dir / "assets" / "sanitized", args.dry_run)

    # Écriture des fichiers
    write_campaign_json(article_dir, article_data, args.dry_run)
    create_article_file(article_dir, template_content, context, args.dry_run)
    create_readme(article_dir, slug_base, args.title, args.dry_run)

    if args.dry_run:
        print("\n[DRY-RUN] Création simulée. Utilisez sans --dry-run pour créer réellement.")
    else:
        print(f"\n✅ Article créé avec succès : {article_dir}")
        print(f"\n📝 Prochaines étapes :")
        print(f"   1. Éditer le contenu : {article_dir / 'article.md'}")
        print(f"   2. Ajouter des assets : {article_dir / 'assets/sanitized/'}")
        print(f"   3. Valider la sécurité : scripts/validate-campaign.sh {article_dir}")
        print(f"   4. L'article sera automatiquement disponible sur /blog/{slug_base}")


if __name__ == "__main__":
    main()

