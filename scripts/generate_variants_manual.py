#!/usr/bin/env python3
"""Génère manuellement les déclinaisons multi-plateformes avec ton naturel.

Ce script génère les déclinaisons en respectant strictement :
- Ton corporate décontracté
- Humour décalé occasionnel
- Pas d'émojis
- Évite tous les patterns de détection LLM
"""
from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

# Templates de génération par plateforme avec ton naturel
PLATFORM_TEMPLATES = {
    "linkedin": {
        "max_length": 3000,
        "style": "professionnel mais accessible, comme une conversation entre collègues",
        "hashtags_count": (3, 5),
        "hashtags_position": "end",
    },
    "facebook": {
        "max_length": 5000,
        "style": "amical et engageant, ton conversationnel",
        "hashtags_count": (3, 10),
        "hashtags_position": "end",
    },
    "threads": {
        "max_length": 500,
        "style": "direct et punchy, comme un tweet amélioré",
        "hashtags_count": (1, 3),
        "hashtags_position": "inline",
    },
    "instagram": {
        "max_length": 2200,
        "style": "visuel et émotionnel, captivant",
        "hashtags_count": (5, 30),
        "hashtags_position": "end",
    },
}


def generate_linkedin_post(article_data: Dict, article_content: str) -> str:
    """Génère un post LinkedIn naturel."""
    title = article_data.get("content", {}).get("title", "")
    summary = article_data.get("content", {}).get("summary", "")
    hashtags = article_data.get("content", {}).get("hashtags", [])
    slug = article_data.get("slug", "")
    
    # Extraire quelques hashtags pertinents et les formater avec espaces
    selected_hashtags = hashtags[:4] if len(hashtags) >= 4 else hashtags
    hashtags_str = " ".join(selected_hashtags) if isinstance(selected_hashtags, list) else selected_hashtags
    
    # Générer le contenu selon le sujet de l'article
    # Ton naturel, corporate décontracté, éviter patterns LLM
    
    if "matching" in slug.lower() or "algorithme" in slug.lower():
        post = f"""J'ai passé pas mal de temps à chercher comment automatiser le matching entre CV et offres d'emploi. Le problème classique : comment savoir si un CV correspond vraiment à une offre sans passer des heures à comparer manuellement ?

J'ai fini par créer un algorithme de scoring qui donne une note de 0 à 100. Pas de magie noire, juste des critères pondérés : compétences techniques, expérience, localisation, type de contrat, salaire, et quelques autres.

Le truc intéressant, c'est que la formule est transparente. Chaque critère a son poids, et on peut voir exactement pourquoi un CV obtient 78 plutôt que 45. Ça évite les boîtes noires où on ne comprend rien.

Résultat concret : je passe de 30 minutes par candidature à environ 2 minutes. Le système fait le tri initial, je garde la main sur les décisions finales. C'est un gain de temps énorme sans perdre le contrôle.

Si vous avez déjà testé des systèmes de matching, vous savez que beaucoup promettent la lune mais déçoivent. Ici, c'est l'inverse : simple, transparent, efficace.

{hashtags_str}"""
    
    elif "import" in slug.lower() or "csv" in slug.lower():
        post = f"""L'import CSV, c'est souvent le cauchemar silencieux de beaucoup d'applications. Chaque fichier a son format, ses colonnes bizarres, ses données manquantes. J'ai fini par créer un système qui détecte automatiquement le format et valide les données avant même de les traiter.

Le système reconnaît différents séparateurs, détecte les encodages, et valide les types de données. Plus besoin de passer une heure à nettoyer manuellement un fichier avant de l'importer.

L'enrichissement automatique vient en bonus : le système complète les données manquantes quand c'est possible, et signale clairement ce qui ne peut pas être récupéré. Ça fait gagner un temps fou sur les imports de masse.

Ce qui me plaît dans cette approche, c'est qu'elle évite les erreurs silencieuses. Si quelque chose ne va pas, on le sait tout de suite avec un message clair, pas après avoir importé 10 000 lignes incorrectes.

{hashtags_str}"""
    
    elif "job-boards" in slug.lower() or "job boards" in title.lower():
        post = f"""J'ai testé 15 job boards français pour voir lesquels valaient vraiment le coup. Spoiler : la plupart se ressemblent, mais il y a quelques perles cachées.

J'ai comparé les fonctionnalités, les tarifs, l'efficacité réelle. Certains sont chers pour ce qu'ils offrent, d'autres sont gratuits mais limités. Le plus intéressant, c'est de voir comment chacun se différencie vraiment.

L'intégration multi-plateformes était mon objectif : pouvoir poster sur plusieurs job boards en une fois sans perdre la tête. Certains ont des APIs, d'autres non. Certains permettent le scraping, d'autres non. C'est un vrai casse-tête.

Résultat : j'ai créé un système qui gère tout ça automatiquement. Plus besoin de se connecter à chaque plateforme individuellement. Un clic, et c'est envoyé partout où ça a du sens.

{hashtags_str}"""
    
    elif "tor" in slug.lower() or "enrichissement" in slug.lower():
        post = f"""Quand on fait du scraping B2B à grande échelle, se faire bloquer devient vite un problème récurrent. J'ai intégré Tor dans mon workflow pour éviter ça, et ça change vraiment la donne.

La rotation d'IP automatique permet de faire des centaines de requêtes sans se faire détecter. Plus besoin de s'arrêter toutes les 10 requêtes parce qu'on a été bloqué. Le système gère ça tout seul.

L'anonymisation est un bonus : même si on ne fait rien d'illégal, c'est rassurant de savoir que son IP n'est pas tracée partout. Surtout quand on teste des outils ou qu'on fait de la recherche.

Ce qui est intéressant, c'est que ça évite aussi les rate limiting. Les sites voient des requêtes normales depuis différentes IPs, pas un bot qui spam depuis la même adresse. Ça passe beaucoup mieux.

{hashtags_str}"""
    
    elif "securisation" in slug.lower() or "sécurité" in title.lower():
        post = f"""Sécuriser un SaaS B2B, c'est un sujet qui peut vite devenir casse-tête. Authentification, autorisation, protection des données, conformité RGPD... La liste est longue.

J'ai mis en place un système complet : authentification robuste, gestion fine des permissions, chiffrement des données sensibles, logs d'audit pour tout tracer. Rien de révolutionnaire, mais tout est là et ça fonctionne.

Le RGPD était un point important : anonymisation automatique, consentement explicite, droit à l'oubli facile à mettre en œuvre. C'est devenu un réflexe maintenant, pas une contrainte.

Ce qui m'a surpris, c'est à quel point beaucoup d'applications négligent ces aspects. Pourtant, c'est souvent ce qui fait la différence entre un produit professionnel et un prototype qui ne passera jamais en production.

{hashtags_str}"""
    
    elif "gamification" in slug.lower() or "ux" in slug.lower():
        post = f"""La gamification dans l'UX, c'est un sujet qui divise. Certains trouvent ça infantilisant, d'autres adorent. J'ai testé l'approche dans SquidResearch pour voir l'impact réel.

Badges, scores, progression... Le système récompense les actions importantes sans être trop intrusif. Pas de popups agaçantes, juste des indicateurs discrets qui montrent où on en est.

L'impact sur l'engagement est réel : les utilisateurs complètent plus souvent leurs profils, utilisent plus de fonctionnalités. C'est subtil mais efficace.

Ce qui m'a plu, c'est que ça reste optionnel. Ceux qui veulent juste utiliser l'outil sans jouer peuvent le faire. Ceux qui aiment voir leur progression ont les indicateurs. Chacun y trouve son compte.

{hashtags_str}"""
    
    elif "oauth" in slug.lower() or "google" in slug.lower():
        post = f"""Intégrer Google OAuth avec un CRUD complet, c'est plus complexe qu'il n'y paraît. Gestion des tokens, refresh automatique, synchronisation des données, gestion des erreurs... Il y a beaucoup de pièges.

J'ai créé un système qui gère tout ça proprement : connexion OAuth, stockage sécurisé des tokens, refresh avant expiration, synchronisation bidirectionnelle. Rien de révolutionnaire, mais tout est là et ça fonctionne bien.

La gestion des erreurs était importante : que faire si Google est down ? Si le token expire ? Si l'utilisateur révoque l'accès ? Le système gère tous ces cas sans planter.

Ce qui m'a surpris, c'est à quel point la documentation Google peut être confuse sur certains points. J'ai dû tester beaucoup de choses pour trouver les bonnes pratiques. Maintenant c'est solide.

{hashtags_str}"""
    
    else:
        # Template générique pour les autres articles
        post = f"""{summary}

J'ai développé cette fonctionnalité pour répondre à un besoin concret que j'avais. Le résultat dépasse mes attentes, et je pense que ça peut intéresser d'autres personnes dans le même cas.

{hashtags_str}"""
    
    return post.strip()


def generate_facebook_post(article_data: Dict, article_content: str) -> str:
    """Génère un post Facebook naturel."""
    title = article_data.get("content", {}).get("title", "")
    summary = article_data.get("content", {}).get("summary", "")
    hashtags = article_data.get("content", {}).get("hashtags", [])
    slug = article_data.get("slug", "")
    
    selected_hashtags = hashtags[:6] if len(hashtags) >= 6 else hashtags
    hashtags_str = " ".join(selected_hashtags) if isinstance(selected_hashtags, list) else selected_hashtags
    
    # Contenu spécifique selon l'article, ton plus décontracté pour Facebook
    if "matching" in slug.lower() or "algorithme" in slug.lower():
        post = f"""Quand j'ai commencé à automatiser mes candidatures, j'ai vite réalisé que le vrai défi était le matching. Comment savoir si mon CV correspond vraiment à une offre sans y passer la journée ?

J'ai développé un système de scoring qui attribue une note de 0 à 100. Rien de révolutionnaire en apparence, mais la différence c'est la transparence. Chaque critère compte : compétences, expérience, localisation, type de contrat, salaire. Et surtout, on voit pourquoi on obtient telle ou telle note.

Le résultat ? Je passe de 30 minutes par candidature à 2 minutes. Le système fait le gros du travail, je garde la main sur les choix importants.

Ce qui me plaît dans cette approche, c'est qu'elle évite les promesses marketing habituelles. Pas de "IA révolutionnaire" ou de "technologie disruptive". Juste un algorithme qui fonctionne et qu'on peut comprendre.

Si vous cherchez un moyen d'optimiser votre recherche d'emploi sans perdre votre âme dans le processus, cette approche vaut le détour.

{hashtags_str}"""
    
    elif "import" in slug.lower() or "csv" in slug.lower():
        post = f"""L'import CSV, vous connaissez ? C'est ce truc qui semble simple mais qui finit toujours par vous faire perdre une après-midi. Formats différents, colonnes qui changent, données manquantes... Le classique.

J'ai créé un système qui détecte automatiquement tout ça. Séparateurs, encodages, types de données. Plus besoin de jouer aux devinettes avant chaque import.

Le bonus, c'est l'enrichissement automatique. Le système complète ce qui peut l'être et vous dit clairement ce qui manque. Ça change la vie sur les gros imports.

Ce qui est bien, c'est que les erreurs sont signalées tout de suite. Pas après avoir importé des milliers de lignes incorrectes. Un message clair, et on sait quoi corriger.

{hashtags_str}"""
    
    elif "job-boards" in slug.lower() or "job boards" in title.lower():
        post = f"""J'ai testé 15 job boards français. Verdict : la plupart se ressemblent, mais il y a quelques pépites cachées.

J'ai comparé fonctionnalités, tarifs, efficacité réelle. Certains sont chers pour ce qu'ils offrent, d'autres gratuits mais limités. Le plus intéressant, c'est de voir comment chacun se différencie vraiment.

Mon objectif était l'intégration multi-plateformes : poster sur plusieurs job boards en une fois sans devenir fou. Certains ont des APIs, d'autres non. C'est un vrai casse-tête.

Résultat : j'ai créé un système qui gère tout ça automatiquement. Plus besoin de se connecter à chaque plateforme individuellement. Un clic, et c'est envoyé partout où ça a du sens.

{hashtags_str}"""
    
    elif "tor" in slug.lower() or "enrichissement" in slug.lower():
        post = f"""Quand on fait du scraping B2B à grande échelle, se faire bloquer devient vite un problème récurrent. J'ai intégré Tor dans mon workflow pour éviter ça.

La rotation d'IP automatique permet de faire des centaines de requêtes sans se faire détecter. Plus besoin de s'arrêter toutes les 10 requêtes parce qu'on a été bloqué.

L'anonymisation est un bonus : même si on ne fait rien d'illégal, c'est rassurant de savoir que son IP n'est pas tracée partout. Surtout quand on teste des outils.

Ce qui est intéressant, c'est que ça évite aussi les rate limiting. Les sites voient des requêtes normales depuis différentes IPs, pas un bot qui spam depuis la même adresse.

{hashtags_str}"""
    
    elif "securisation" in slug.lower() or "sécurité" in title.lower():
        post = f"""Sécuriser un SaaS B2B, c'est un sujet qui peut vite devenir casse-tête. Authentification, autorisation, protection des données, conformité RGPD... La liste est longue.

J'ai mis en place un système complet : authentification robuste, gestion fine des permissions, chiffrement des données sensibles, logs d'audit pour tout tracer. Rien de révolutionnaire, mais tout est là.

Le RGPD était important : anonymisation automatique, consentement explicite, droit à l'oubli facile. C'est devenu un réflexe maintenant.

Ce qui m'a surpris, c'est à quel point beaucoup d'applications négligent ces aspects. Pourtant, c'est souvent ce qui fait la différence entre un produit professionnel et un prototype.

{hashtags_str}"""
    
    elif "gamification" in slug.lower() or "ux" in slug.lower():
        post = f"""La gamification dans l'UX, c'est un sujet qui divise. Certains trouvent ça infantilisant, d'autres adorent. J'ai testé l'approche dans SquidResearch.

Badges, scores, progression... Le système récompense les actions importantes sans être trop intrusif. Pas de popups agaçantes, juste des indicateurs discrets.

L'impact sur l'engagement est réel : les utilisateurs complètent plus souvent leurs profils, utilisent plus de fonctionnalités. C'est subtil mais efficace.

Ce qui m'a plu, c'est que ça reste optionnel. Ceux qui veulent juste utiliser l'outil peuvent le faire. Ceux qui aiment voir leur progression ont les indicateurs.

{hashtags_str}"""
    
    elif "oauth" in slug.lower() or "google" in slug.lower():
        post = f"""Intégrer Google OAuth avec un CRUD complet, c'est plus complexe qu'il n'y paraît. Gestion des tokens, refresh automatique, synchronisation des données... Il y a beaucoup de pièges.

J'ai créé un système qui gère tout ça proprement : connexion OAuth, stockage sécurisé des tokens, refresh avant expiration, synchronisation bidirectionnelle. Rien de révolutionnaire, mais ça fonctionne bien.

La gestion des erreurs était importante : que faire si Google est down ? Si le token expire ? Si l'utilisateur révoque l'accès ? Le système gère tous ces cas sans planter.

Ce qui m'a surpris, c'est à quel point la documentation Google peut être confuse. J'ai dû tester beaucoup de choses pour trouver les bonnes pratiques.

{hashtags_str}"""
    
    else:
        post = f"""{summary}

J'ai développé cette fonctionnalité pour répondre à un besoin concret. Le résultat dépasse mes attentes.

{hashtags_str}"""
    
    return post.strip()


def generate_threads_post(article_data: Dict, article_content: str) -> str:
    """Génère un post Threads naturel."""
    title = article_data.get("content", {}).get("title", "")
    summary = article_data.get("content", {}).get("summary", "")
    hashtags = article_data.get("content", {}).get("hashtags", [])
    slug = article_data.get("slug", "")
    
    selected_hashtags = hashtags[:2] if len(hashtags) >= 2 else hashtags
    hashtags_str = " ".join(selected_hashtags) if isinstance(selected_hashtags, list) else selected_hashtags
    
    # Contenu spécifique selon l'article, format court pour Threads
    if "matching" in slug.lower() or "algorithme" in slug.lower():
        post = f"""J'ai automatisé le matching CV/offres avec un scoring 0-100. Transparent, efficace, pas de boîte noire. Résultat : 30 min → 2 min par candidature. {hashtags_str}"""
    
    elif "import" in slug.lower() or "csv" in slug.lower():
        post = f"""Import CSV intelligent : détection automatique de format, validation des données, enrichissement auto. Plus besoin de nettoyer manuellement avant import. {hashtags_str}"""
    
    elif "job-boards" in slug.lower() or "job boards" in title.lower():
        post = f"""J'ai testé 15 job boards français. Verdict : la plupart se ressemblent, quelques pépites cachées. J'ai créé un système pour poster partout en un clic. {hashtags_str}"""
    
    elif "tor" in slug.lower() or "enrichissement" in slug.lower():
        post = f"""Scraping B2B à grande échelle sans se faire bloquer : rotation IP automatique avec Tor, anonymisation, évite rate limiting. Ça change vraiment la donne. {hashtags_str}"""
    
    elif "securisation" in slug.lower() or "sécurité" in title.lower():
        post = f"""Sécuriser un SaaS B2B : authentification robuste, permissions fines, RGPD, logs d'audit. Rien de révolutionnaire, mais tout est là et ça fonctionne. {hashtags_str}"""
    
    elif "gamification" in slug.lower() or "ux" in slug.lower():
        post = f"""Gamification UX : badges, scores, progression discrets. Impact réel sur l'engagement sans être intrusif. Optionnel, chacun y trouve son compte. {hashtags_str}"""
    
    elif "oauth" in slug.lower() or "google" in slug.lower():
        post = f"""Google OAuth avec CRUD complet : gestion tokens, refresh auto, synchronisation bidirectionnelle. Gère tous les cas d'erreur sans planter. {hashtags_str}"""
    
    else:
        post = f"""{summary[:200]}... {hashtags_str}"""
    
    return post.strip()


def generate_instagram_post(article_data: Dict, article_content: str) -> str:
    """Génère un post Instagram naturel."""
    title = article_data.get("content", {}).get("title", "")
    summary = article_data.get("content", {}).get("summary", "")
    hashtags = article_data.get("content", {}).get("hashtags", [])
    slug = article_data.get("slug", "")
    
    selected_hashtags = hashtags[:15] if len(hashtags) >= 15 else hashtags
    hashtags_str = " ".join(selected_hashtags) if isinstance(selected_hashtags, list) else selected_hashtags
    
    # Contenu spécifique selon l'article, format visuel et émotionnel pour Instagram
    if "matching" in slug.lower() or "algorithme" in slug.lower():
        post = f"""Le matching CV/offres, c'est souvent la partie la plus chronophage d'une candidature. J'ai créé un algorithme de scoring qui donne une note de 0 à 100, avec une transparence totale sur les critères.

Compétences techniques, expérience, localisation, type de contrat, salaire : chaque élément compte et on sait pourquoi. Pas de boîte noire, pas de promesses marketing. Juste un système qui fonctionne.

Le gain de temps est réel : de 30 minutes à 2 minutes par candidature. Le système fait le tri initial, je garde le contrôle sur les décisions importantes.

Si vous cherchez à optimiser votre recherche d'emploi sans perdre en qualité, cette approche mérite qu'on s'y attarde.

{hashtags_str}"""
    
    elif "import" in slug.lower() or "csv" in slug.lower():
        post = f"""L'import CSV, c'est souvent le problème qui vous fait perdre une après-midi. Formats différents, colonnes qui changent, données manquantes.

J'ai créé un système qui détecte automatiquement tout ça : séparateurs, encodages, types de données. Plus besoin de nettoyer manuellement avant chaque import.

L'enrichissement automatique complète ce qui peut l'être et signale clairement ce qui manque. Ça change vraiment la vie sur les imports de masse.

Si vous travaillez avec des fichiers CSV régulièrement, cette approche peut vous faire gagner un temps précieux.

{hashtags_str}"""
    
    elif "job-boards" in slug.lower() or "job boards" in title.lower():
        post = f"""J'ai testé 15 job boards français. La plupart se ressemblent, mais il y a quelques pépites cachées qui valent vraiment le détour.

J'ai comparé fonctionnalités, tarifs, efficacité réelle. Certains sont chers pour ce qu'ils offrent, d'autres gratuits mais limités.

J'ai créé un système qui gère l'intégration multi-plateformes automatiquement. Plus besoin de se connecter à chaque job board individuellement. Un clic, et c'est envoyé partout.

Si vous cherchez un moyen d'optimiser votre recherche d'emploi, cette approche vaut vraiment le coup.

{hashtags_str}"""
    
    elif "tor" in slug.lower() or "enrichissement" in slug.lower():
        post = f"""Quand on fait du scraping B2B à grande échelle, se faire bloquer devient vite un problème récurrent. J'ai intégré Tor dans mon workflow pour éviter ça.

La rotation d'IP automatique permet de faire des centaines de requêtes sans se faire détecter. Plus besoin de s'arrêter toutes les 10 requêtes.

L'anonymisation est un bonus rassurant, surtout quand on teste des outils ou qu'on fait de la recherche.

Ça évite aussi les rate limiting. Les sites voient des requêtes normales depuis différentes IPs, pas un bot qui spam depuis la même adresse.

{hashtags_str}"""
    
    elif "securisation" in slug.lower() or "sécurité" in title.lower():
        post = f"""Sécuriser un SaaS B2B, c'est un sujet qui peut vite devenir casse-tête. Authentification, autorisation, protection des données, conformité RGPD.

J'ai mis en place un système complet : authentification robuste, gestion fine des permissions, chiffrement des données, logs d'audit. Tout est là et ça fonctionne.

Le RGPD était important : anonymisation automatique, consentement explicite, droit à l'oubli facile. C'est devenu un réflexe maintenant.

Beaucoup d'applications négligent ces aspects, pourtant c'est souvent ce qui fait la différence entre un produit professionnel et un prototype.

{hashtags_str}"""
    
    elif "gamification" in slug.lower() or "ux" in slug.lower():
        post = f"""La gamification dans l'UX, c'est un sujet qui divise. Certains trouvent ça infantilisant, d'autres adorent. J'ai testé l'approche dans SquidResearch.

Badges, scores, progression... Le système récompense les actions importantes sans être trop intrusif. Pas de popups agaçantes, juste des indicateurs discrets.

L'impact sur l'engagement est réel : les utilisateurs complètent plus souvent leurs profils, utilisent plus de fonctionnalités. C'est subtil mais efficace.

Ça reste optionnel. Ceux qui veulent juste utiliser l'outil peuvent le faire. Ceux qui aiment voir leur progression ont les indicateurs.

{hashtags_str}"""
    
    elif "oauth" in slug.lower() or "google" in slug.lower():
        post = f"""Intégrer Google OAuth avec un CRUD complet, c'est plus complexe qu'il n'y paraît. Gestion des tokens, refresh automatique, synchronisation des données.

J'ai créé un système qui gère tout ça proprement : connexion OAuth, stockage sécurisé des tokens, refresh avant expiration, synchronisation bidirectionnelle.

La gestion des erreurs était importante : que faire si Google est down ? Si le token expire ? Le système gère tous ces cas sans planter.

La documentation Google peut être confuse sur certains points. J'ai dû tester beaucoup de choses pour trouver les bonnes pratiques.

{hashtags_str}"""
    
    else:
        post = f"""{summary}

J'ai développé cette fonctionnalité pour répondre à un besoin concret. Le résultat dépasse mes attentes.

{hashtags_str}"""
    
    return post.strip()


def generate_variants_for_article(article_slug: str, platforms: list[str] = None) -> None:
    """Génère les déclinaisons pour un article."""
    if platforms is None:
        platforms = ["linkedin", "facebook", "threads", "instagram"]
    
    article_dir = ARTICLES_DIR / article_slug
    
    # Charger campaign.json
    campaign_json_path = article_dir / "campaign.json"
    with campaign_json_path.open("r", encoding="utf-8") as f:
        article_data = json.load(f)
    
    # Charger article.md
    article_md_path = article_dir / "article.md"
    article_content = article_md_path.read_text(encoding="utf-8") if article_md_path.exists() else ""
    
    generators = {
        "linkedin": generate_linkedin_post,
        "facebook": generate_facebook_post,
        "threads": generate_threads_post,
        "instagram": generate_instagram_post,
    }
    
    for platform in platforms:
        if platform not in generators:
            continue
        
        generator = generators[platform]
        content = generator(article_data, article_content)
        
        # Créer le fichier
        platform_dir = article_dir / "platforms" / platform
        platform_dir.mkdir(parents=True, exist_ok=True)
        (platform_dir / "assets").mkdir(parents=True, exist_ok=True)
        
        variant_file = platform_dir / "post-01.md"
        
        template = f"""# {platform.upper()} Post - {article_data.get('content', {}).get('title', 'Article')}

**Plateforme** : {platform.upper()}  
**Généré le** : {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC  
**Statut** : draft

---

## Contenu

{content}

---

## Métadonnées

- **Longueur** : {len(content)} caractères
- **Ton** : {PLATFORM_TEMPLATES[platform]['style']}
- **Format** : {PLATFORM_TEMPLATES[platform].get('format', 'post')}

---

## Assets

- Images : `assets/image-01.png`
- Vidéos : `assets/video-01.mp4`

---

## Notes

[TODO: Ajouter notes, modifications, etc.]

"""
        
        variant_file.write_text(template, encoding="utf-8")
        print(f"✅ {platform.upper()} généré : {variant_file}")
        
        # Mettre à jour campaign.json
        posts = article_data.get("posts", [])
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
            article_data["posts"] = posts
            article_data["updated_at"] = datetime.utcnow().isoformat() + "Z"
            
            with campaign_json_path.open("w", encoding="utf-8") as f:
                json.dump(article_data, f, indent=2, ensure_ascii=False)
                f.write("\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate_variants_manual.py <article-slug> [platforms...]")
        sys.exit(1)
    
    article_slug = sys.argv[1]
    platforms = sys.argv[2:] if len(sys.argv) > 2 else None
    
    generate_variants_for_article(article_slug, platforms)
    print(f"\n✅ Déclinaisons générées pour {article_slug}")

