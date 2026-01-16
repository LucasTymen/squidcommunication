#!/usr/bin/env python3
"""Génère les déclinaisons multi-plateformes d'un article de blog.

Usage:
    python scripts/generate_platform_variants.py <article-slug> \
        [--platforms linkedin facebook threads instagram] \
        [--llm-provider n8n|openai|anthropic] \
        [--dry-run] \
        [--validate-security]
    
Exemples:
    # Générer pour toutes les plateformes (via n8n/Flowise)
    python scripts/generate_platform_variants.py article-1-gain-temps-candidature-93pct
    
    # Générer uniquement LinkedIn et Facebook
    python scripts/generate_platform_variants.py article-1-gain-temps-candidature-93pct \
        --platforms linkedin facebook
    
    # Utiliser OpenAI directement (fallback)
    python scripts/generate_platform_variants.py article-1-gain-temps-candidature-93pct \
        --llm-provider openai
    
    # Dry-run pour tester
    python scripts/generate_platform_variants.py article-1-gain-temps-candidature-93pct --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import requests

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
SECURITY_KEYWORDS_FILE = ROOT / "docs" / "SECURITY_KEYWORDS.md"

# Configuration LLM (peut être surchargée par variables d'environnement)
N8N_URL = os.getenv("N8N_URL", "http://localhost:5679")
FLOWISE_URL = os.getenv("FLOWISE_URL", "http://localhost:3001")
FLOWISE_FLOW_ID = os.getenv("FLOWISE_FLOW_ID", "")
FLOWISE_API_KEY = os.getenv("FLOWISE_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Plateformes supportées avec leurs contraintes
PLATFORM_CONSTRAINTS = {
    "linkedin": {
        "max_length": 3000,
        "hashtags_min": 3,
        "hashtags_max": 5,
        "tone": "professionnel",
        "format": "3-5 paragraphes courts",
        "hashtags_position": "end",
    },
    "facebook": {
        "max_length": 5000,
        "hashtags_min": 3,
        "hashtags_max": 10,
        "tone": "amical et engageant",
        "format": "2-3 paragraphes",
        "hashtags_position": "end",
    },
    "threads": {
        "max_length": 500,
        "hashtags_min": 1,
        "hashtags_max": 3,
        "tone": "conversationnel et direct",
        "format": "1-2 paragraphes courts",
        "hashtags_position": "inline",
    },
    "instagram": {
        "max_length": 2200,
        "hashtags_min": 5,
        "hashtags_max": 30,
        "tone": "visuel et émotionnel",
        "format": "1-2 phrases + caption",
        "hashtags_position": "end",
    },
}


def load_article(article_slug: str) -> tuple[Dict, str]:
    """Charge l'article et son contenu."""
    article_dir = ARTICLES_DIR / f"article-{article_slug}"
    
    if not article_dir.exists():
        raise SystemExit(f"❌ Article non trouvé : {article_dir}")
    
    # Charger campaign.json
    campaign_json_path = article_dir / "campaign.json"
    if not campaign_json_path.exists():
        raise SystemExit(f"❌ campaign.json non trouvé : {campaign_json_path}")
    
    with campaign_json_path.open("r", encoding="utf-8") as f:
        article_data = json.load(f)
    
    # Charger article.md
    article_md_path = article_dir / "article.md"
    if not article_md_path.exists():
        raise SystemExit(f"❌ article.md non trouvé : {article_md_path}")
    
    article_content = article_md_path.read_text(encoding="utf-8")
    
    return article_data, article_content


def load_security_keywords() -> List[str]:
    """Charge la liste des mots-clés sensibles depuis SECURITY_KEYWORDS.md."""
    keywords = []
    
    if not SECURITY_KEYWORDS_FILE.exists():
        # Liste par défaut si fichier non trouvé
        return [
            "OSINT", "forensic", "kali linux", "the harvester", "sherlock",
            "holehe", "h8mail", "recon-ng", "maltego", "shodan", "censys",
        ]
    
    content = SECURITY_KEYWORDS_FILE.read_text(encoding="utf-8")
    
    # Extraire les mots-clés de la section "🚫 Mots-Clés à Éviter Absolument"
    in_section = False
    for line in content.split("\n"):
        if "🚫 Mots-Clés à Éviter Absolument" in line:
            in_section = True
            continue
        if in_section and line.startswith("##"):
            break
        if in_section and line.startswith("- `"):
            # Extraire le contenu entre backticks
            match = re.search(r"`([^`]+)`", line)
            if match:
                keywords.append(match.group(1).lower())
        if in_section and line.startswith("- "):
            # Extraire le texte après le tiret
            text = line[2:].strip()
            if text and not text.startswith("#"):
                keywords.append(text.lower())
    
    return keywords


def validate_security(content: str, keywords: List[str]) -> List[str]:
    """Détecte les mots-clés sensibles dans le contenu."""
    issues = []
    content_lower = content.lower()
    
    for keyword in keywords:
        if keyword.lower() in content_lower:
            issues.append(f"Mot-clé sensible détecté : '{keyword}'")
    
    # Patterns supplémentaires
    ip_pattern = r"\b(192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1])\.)\d+\.\d+\b"
    if re.search(ip_pattern, content):
        issues.append("IP interne détectée")
    
    credential_patterns = [
        r"password\s*[:=]\s*\S+",
        r"api[_-]?key\s*[:=]\s*\S+",
        r"token\s*[:=]\s*\S+",
        r"secret\s*[:=]\s*\S+",
    ]
    for pattern in credential_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append(f"Pattern credential détecté : {pattern}")
    
    return issues


def generate_variant_via_n8n(
    article_content: str,
    article_metadata: Dict,
    platform: str,
    constraints: Dict,
) -> Optional[str]:
    """Génère une déclinaison via n8n/Flowise."""
    # TODO: Implémenter l'appel n8n/Flowise
    # Pour l'instant, retourne None (génération manuelle)
    return None


def generate_variant_via_openai(
    article_content: str,
    article_metadata: Dict,
    platform: str,
    constraints: Dict,
    dry_run: bool = False,
) -> Optional[str]:
    """Génère une déclinaison via OpenAI API (fallback)."""
    if not OPENAI_API_KEY:
        return None
    
    if dry_run:
        return f"[DRY-RUN] Variante {platform} générée via OpenAI"
    
    # Construire le prompt
    title = article_metadata.get("content", {}).get("title", "Article")
    summary = article_metadata.get("content", {}).get("summary", "")
    
    prompt = f"""Tu es un expert en communication sur {platform.upper()}, avec un style naturel et authentique.

Article original:
Titre: {title}
Résumé: {summary}

Contenu complet:
{article_content[:2000]}...

Contraintes {platform.upper()}:
- Longueur max: {constraints['max_length']} caractères
- Ton: {constraints['tone']}, corporate mais décontracté, avec un peu d'humour décalé occasionnel
- Format: {constraints['format']}
- Hashtags: {constraints['hashtags_min']}-{constraints['hashtags_max']} hashtags ({constraints['hashtags_position']})
- PAS d'émojis

RÈGLES ABSOLUES - ÉVITER ces patterns de détection LLM:
1. PAS de formules de cadrage en introduction ("Dans un monde où...", "Aujourd'hui plus que jamais...")
2. PAS de structure hyper-segmentée (éviter trop de listes, sous-titres)
3. PAS de vocabulaire corporate anglo-saxon ("crucial", "disruptif", "game-changer")
4. PAS d'antithèses binaires avec emphase ("soit... soit...", "d'un côté... de l'autre...")
5. PAS d'intensifieurs à faible coût ("crucial", "essentiel", "vital")
6. PAS de doublement rhétorique (répéter la même idée 3+ fois)
7. PAS de marqueurs de rupture narrative artificiels ("Mais attendez...", "Et là, surprise...")
8. PAS de métadiscours constant ("Je vais vous expliquer...", "Laissez-moi vous dire...")

Style à adopter:
- Ton naturel, comme si tu racontais à un collègue
- Phrases variées (courtes et longues)
- Humour décalé occasionnel mais subtil
- Vocabulaire français naturel, éviter anglicismes
- Structure fluide, pas mécanique
- Aller droit au fait, pas de préambules

Génère un post optimisé pour {platform.upper()} qui:
1. Adapte le contenu au format et ton de la plateforme
2. Respecte les contraintes de longueur
3. Inclut les hashtags appropriés
4. Reste fidèle au message original
5. Est engageant pour l'audience {platform.upper()}
6. Semble écrit par un humain, pas par une IA

Format de réponse (JSON):
{{
  "content": "Texte du post...",
  "hashtags": ["#Tag1", "#Tag2"],
  "estimated_length": 250,
  "tone": "{constraints['tone']}"
}}
"""
    
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": "Tu es un expert en communication sur les réseaux sociaux."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.7,
                "max_tokens": 1000,
            },
            timeout=60,
        )
        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        
        # Parser JSON si possible
        try:
            parsed = json.loads(content)
            return parsed.get("content", content)
        except json.JSONDecodeError:
            return content
            
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Erreur OpenAI : {e}")
        return None


def create_platform_variant_file(
    article_dir: Path,
    platform: str,
    content: str,
    metadata: Dict,
    dry_run: bool = False,
) -> None:
    """Crée le fichier de déclinaison pour une plateforme."""
    platforms_dir = article_dir / "platforms"
    platform_dir = platforms_dir / platform
    assets_dir = platform_dir / "assets"
    
    if not dry_run:
        platform_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)
    
    # Nom du fichier (post-01.md pour le premier)
    variant_file = platform_dir / "post-01.md"
    
    # Template Markdown avec métadonnées
    template = f"""# {platform.upper()} Post - {metadata.get('content', {}).get('title', 'Article')}

**Plateforme** : {platform.upper()}  
**Généré le** : {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC  
**Statut** : draft

---

## Contenu

{content}

---

## Métadonnées

- **Longueur** : {len(content)} caractères
- **Ton** : {PLATFORM_CONSTRAINTS[platform]['tone']}
- **Format** : {PLATFORM_CONSTRAINTS[platform]['format']}

---

## Assets

- Images : `assets/image-01.png`
- Vidéos : `assets/video-01.mp4`

---

## Notes

[TODO: Ajouter notes, modifications, etc.]

"""
    
    if dry_run:
        print(f"[DRY-RUN] Écriture : {variant_file}")
        print("\n" + "="*80)
        print(template)
        print("="*80)
    else:
        variant_file.write_text(template, encoding="utf-8")
        print(f"✅ Déclinaison créée : {variant_file}")


def update_campaign_json(
    article_dir: Path,
    platform: str,
    variant_file: str,
    dry_run: bool = False,
) -> None:
    """Met à jour campaign.json avec les nouvelles déclinaisons."""
    campaign_json_path = article_dir / "campaign.json"
    
    with campaign_json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Ajouter la déclinaison dans posts si pas déjà présent
    posts = data.get("posts", [])
    
    # Vérifier si une déclinaison pour cette plateforme existe déjà
    existing = next((p for p in posts if p.get("platform") == platform), None)
    
    if not existing:
        posts.append({
            "post_id": f"{platform}-01",
            "platform": platform,
            "format": "post",
            "status": "draft",
            "file": f"platforms/{platform}/post-01.md",
            "analytics": {
                "impressions": 0,
                "engagement": {"likes": 0, "comments": 0, "shares": 0},
            },
        })
        data["posts"] = posts
        data["updated_at"] = datetime.utcnow().isoformat() + "Z"
    
    if not dry_run:
        with campaign_json_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"✅ campaign.json mis à jour")
    else:
        print(f"[DRY-RUN] Mise à jour campaign.json simulée")


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Génère les déclinaisons multi-plateformes d'un article",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python scripts/generate_platform_variants.py article-1-gain-temps-candidature-93pct
  python scripts/generate_platform_variants.py article-1 --platforms linkedin facebook
  python scripts/generate_platform_variants.py article-1 --llm-provider openai --dry-run
  python scripts/generate_platform_variants.py article-1 --validate-security
""",
    )
    parser.add_argument(
        "article_slug",
        help="Slug de l'article (sans préfixe 'article-')",
    )
    parser.add_argument(
        "--platforms",
        nargs="+",
        default=["linkedin", "facebook", "threads", "instagram"],
        choices=["linkedin", "facebook", "threads", "instagram"],
        help="Plateformes cibles (défaut: toutes)",
    )
    parser.add_argument(
        "--llm-provider",
        default="n8n",
        choices=["n8n", "openai", "anthropic"],
        help="Fournisseur LLM (défaut: n8n)",
    )
    parser.add_argument(
        "--validate-security",
        action="store_true",
        help="Valider la sécurité avant génération",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simuler la génération sans créer de fichiers",
    )
    return parser.parse_args(argv)


def main() -> None:
    """Point d'entrée principal."""
    ensure_super_admin()
    args = parse_args()
    
    # Normaliser le slug (enlever préfixe si présent)
    slug = args.article_slug.replace("article-", "") if args.article_slug.startswith("article-") else args.article_slug
    
    print(f"📝 Génération déclinaisons pour : article-{slug}")
    print(f"   Plateformes : {', '.join(args.platforms)}")
    print(f"   LLM Provider : {args.llm_provider}")
    
    # Charger l'article
    article_data, article_content = load_article(slug)
    
    article_dir = ARTICLES_DIR / f"article-{slug}"
    title = article_data.get("content", {}).get("title", "Article")
    print(f"   Titre : {title}\n")
    
    # Charger les mots-clés de sécurité
    security_keywords = load_security_keywords()
    
    # Valider sécurité si demandé
    if args.validate_security:
        print("🔒 Validation sécurité...")
        issues = validate_security(article_content, security_keywords)
        if issues:
            print("❌ Problèmes de sécurité détectés :")
            for issue in issues:
                print(f"   - {issue}")
            if not args.dry_run:
                response = input("\nContinuer malgré les problèmes ? (o/N): ")
                if response.lower() != "o":
                    raise SystemExit("Génération annulée par l'utilisateur")
        else:
            print("✅ Aucun problème de sécurité détecté\n")
    
    # Générer les déclinaisons pour chaque plateforme
    generated_count = 0
    
    for platform in args.platforms:
        if platform not in PLATFORM_CONSTRAINTS:
            print(f"⚠️  Plateforme non supportée : {platform}")
            continue
        
        print(f"🎯 Génération {platform.upper()}...")
        constraints = PLATFORM_CONSTRAINTS[platform]
        
        # Générer le contenu
        variant_content = None
        
        if args.llm_provider == "n8n":
            variant_content = generate_variant_via_n8n(
                article_content, article_data, platform, constraints
            )
            if not variant_content:
                print(f"   ⚠️  n8n non disponible, passage en mode manuel")
                # Pour l'instant, création fichier template vide
                variant_content = f"[TODO: Générer le contenu {platform.upper()} depuis l'article original]\n\n{article_content[:500]}..."
        
        elif args.llm_provider == "openai":
            variant_content = generate_variant_via_openai(
                article_content, article_data, platform, constraints, args.dry_run
            )
        
        if variant_content:
            # Valider sécurité du contenu généré
            issues = validate_security(variant_content, security_keywords)
            if issues:
                print(f"   ⚠️  Problèmes sécurité détectés dans le contenu généré :")
                for issue in issues:
                    print(f"      - {issue}")
            
            # Créer le fichier
            create_platform_variant_file(
                article_dir, platform, variant_content, article_data, args.dry_run
            )
            
            # Mettre à jour campaign.json
            update_campaign_json(
                article_dir, platform, f"platforms/{platform}/post-01.md", args.dry_run
            )
            
            generated_count += 1
            print(f"   ✅ {platform.upper()} généré\n")
        else:
            print(f"   ❌ Échec génération {platform.upper()}\n")
    
    if args.dry_run:
        print(f"\n[DRY-RUN] {generated_count} déclinaison(s) simulée(s)")
    else:
        print(f"\n✅ {generated_count} déclinaison(s) générée(s) avec succès")
        print(f"\n📝 Prochaines étapes :")
        print(f"   1. Vérifier les fichiers dans : {article_dir / 'platforms'}")
        print(f"   2. Ajuster le contenu si nécessaire")
        print(f"   3. Valider sécurité : python scripts/generate_platform_variants.py {slug} --validate-security")
        print(f"   4. Prévisualiser : python scripts/preview_article.py {slug}")


if __name__ == "__main__":
    main()

