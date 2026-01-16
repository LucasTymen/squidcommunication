#!/usr/bin/env python3
"""
Script pour générer tous les articles manquants des semaines 1 et 2 en JSON
Respecte la charte éditoriale stricte : données réelles uniquement, ton personnel, pas de marqueurs LLM
"""

import json
import sys
import os

# Ajouter le répertoire parent au path pour importer si nécessaire
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_content_template(title, category, data_points):
    """Génère un contenu markdown de base selon la charte éditoriale"""
    
    # Template minimal respectant la charte (ton personnel, données réelles, pas de marqueurs LLM)
    content = f"J'ai travaillé sur {title.lower()}. "
    
    if data_points:
        metrics = ", ".join(data_points[:3])  # Limiter à 3 métriques pour éviter la surcharge
        content += f"Résultat : {metrics}."
    
    content += "\n\nLes données proviennent de mesures réelles sur l'usage du projet."
    
    # Ajouter hashtags standards
    hashtags = {
        "Business/ROI": "#SquidResearch #IA #B2B #Productivité #ROI",
        "Technique/Performance": "#SquidResearch #Python #Performance #Tech",
        "Technique/Sécurité": "#SquidResearch #Sécurité #Tor #Tech",
        "IA/Automatisation": "#SquidResearch #IA #Automatisation #Tech",
        "Broadcasting/Social": "#SquidResearch #SocialMedia #Marketing #Campagne",
        "Technique/Django": "#SquidResearch #Django #Python #Tech"
    }
    
    content += f"\n\n{hashtags.get(category, '#SquidResearch #Tech')}"
    
    return content

def get_seo_data(category, title):
    """Génère les données SEO par catégorie"""
    
    seo_map = {
        "Business/ROI": {
            "primary_keywords": ["gain temps", "ROI", "productivité", "prospection B2B"],
            "long_tail_keywords": ["gain temps recrutement", "ROI outils recrutement"],
            "hashtags": ["#SquidResearch", "#IA", "#B2B", "#Productivité", "#ROI"]
        },
        "Technique/Performance": {
            "primary_keywords": ["performance", "bulk operations", "scalable"],
            "long_tail_keywords": ["performance bulk operations", "scalable architecture"],
            "hashtags": ["#SquidResearch", "#Python", "#Performance", "#Tech"]
        },
        "Technique/Sécurité": {
            "primary_keywords": ["sécurité", "Tor", "anonymisation", "protection IP"],
            "long_tail_keywords": ["sécurité SaaS B2B", "protection IP Tor"],
            "hashtags": ["#SquidResearch", "#Sécurité", "#Tor", "#Tech"]
        },
        "IA/Automatisation": {
            "primary_keywords": ["IA", "automatisation", "orchestration", "n8n"],
            "long_tail_keywords": ["orchestration workflow n8n", "automatisation IA"],
            "hashtags": ["#SquidResearch", "#IA", "#Automatisation", "#Tech"]
        },
        "Broadcasting/Social": {
            "primary_keywords": ["social media", "multi-plateformes", "campagne"],
            "long_tail_keywords": ["orchestration campagnes LinkedIn", "multi-plateformes social media"],
            "hashtags": ["#SquidResearch", "#SocialMedia", "#Marketing", "#Campagne"]
        },
        "Technique/Django": {
            "primary_keywords": ["Django", "Python", "ORM", "DRF", "API REST"],
            "long_tail_keywords": ["Django ORM optimisations", "DRF architecture scalable"],
            "hashtags": ["#SquidResearch", "#Django", "#Python", "#Tech"]
        },
        "Technique/Docker": {
            "primary_keywords": ["Docker", "containers", "DevOps", "orchestration"],
            "long_tail_keywords": ["Docker Compose multi-services", "architecture containers"],
            "hashtags": ["#SquidResearch", "#Docker", "#DevOps", "#Tech"]
        }
    }
    
    default_seo = {
        "primary_keywords": ["SquidResearch"],
        "long_tail_keywords": [],
        "hashtags": ["#SquidResearch", "#Tech"]
    }
    
    seo = seo_map.get(category, default_seo).copy()
    seo["meta_title"] = f"{title} | SquidResearch"
    seo["meta_description"] = f"{title}. Données réelles mesurées sur l'usage SquidResearch."
    seo["tags"] = seo["primary_keywords"][:5]
    
    return seo

# Articles manquants à générer (structure simplifiée)
articles_to_generate = [
    {"id": "article-12", "slug": "article-12-bulk-operations-20-entreprises-42s", "title": "Bulk operations : 20 entreprises en 42s", "category": "Technique/Performance", "priority": "medium", "format": "post", "date": "2026-01-07", "data": ["42s/10 entreprises", "18s/5 entreprises"]},
    {"id": "article-13", "slug": "article-13-protection-ip-tor-integree", "title": "Protection IP Tor intégrée", "category": "Technique/Sécurité", "priority": "medium", "format": "post", "date": "2026-01-07", "data": ["Tor intégré", "Évite rate limiting"]},
    {"id": "article-16", "slug": "article-16-multi-canal-relances-automatisees", "title": "Multi-canal relances automatisées", "category": "Business/ROI", "priority": "medium", "format": "post", "date": "2026-01-08", "data": ["Email + LinkedIn + Téléphone", "17 relances programmées", "93% gain temps"]},
    {"id": "article-17", "slug": "article-17-conformite-rgpd-complete", "title": "Conformité RGPD complète", "category": "Sécurité/Conformité", "priority": "medium", "format": "post", "date": "2026-01-08", "data": ["Export RGPD", "Anonymisation automatique", "Logs audit"]},
    {"id": "article-18", "slug": "article-18-marque-inpi-e-soleau", "title": "Marque INPI + e-Soleau", "category": "Business/IP", "priority": "medium", "format": "post", "date": "2026-01-08", "data": ["SquidResearch® INPI", "e-Soleau DSO2025026228"]},
    {"id": "article-19", "slug": "article-19-architecture-50k-lignes-6-mois", "title": "Architecture 50K+ lignes, 6 mois développement", "category": "Technique/Stack", "priority": "medium", "format": "article", "date": "2026-01-09", "data": ["50K+ lignes", "83 apps Django", "6 mois développement"]},
    {"id": "article-20", "slug": "article-20-systeme-quotas-early-adopters", "title": "Système de quotas et early adopters", "category": "Business/Stratégie", "priority": "medium", "format": "post", "date": "2026-01-09", "data": ["Quotas illimités à vie", "Early adopter status"]},
    {"id": "article-21", "slug": "article-21-pricing-modulaire-3-modules", "title": "Pricing modulaire : 3 modules indépendants", "category": "Business/Pricing", "priority": "medium", "format": "post", "date": "2026-01-09", "data": ["9€/12€/15€ par module", "Bundle 25€/49€"]},
    {"id": "article-22", "slug": "article-22-architecture-modulaire-achat-carte", "title": "Architecture modulaire : achat à la carte", "category": "Business/Product", "priority": "medium", "format": "post", "date": "2026-01-09", "data": ["Modules indépendants", "Upsell facile"]},
    {"id": "article-24", "slug": "article-24-botfriendly-optimisation-ats", "title": "BotFriendly : Optimisation mots-clés ATS", "category": "IA/Optimisation", "priority": "medium", "format": "post", "date": "2026-01-11", "data": ["6 crédits/optimisation", "Système crédits"]},
    {"id": "article-26", "slug": "article-26-n8n-flowise-orchestration-ia", "title": "n8n + Flowise : Orchestration IA asynchrone", "category": "IA/Automatisation", "priority": "medium", "format": "article", "date": "2026-01-11", "data": ["Intégration n8n/Flowise", "Workflows asynchrones"]},
    {"id": "article-27", "slug": "article-27-generation-contenu-ia-multi-plateformes", "title": "Génération contenu IA multi-plateformes", "category": "IA/Créative", "priority": "medium", "format": "article", "date": "2026-01-11", "data": ["Social Campaign Engine", "8 plateformes"]},
    {"id": "article-28", "slug": "article-28-ab-testing-campagnes-sociales", "title": "A/B Testing intégré campagnes sociales", "category": "Broadcasting/Testing", "priority": "medium", "format": "post", "date": "2026-01-13", "data": ["Moteur A/B testing", "84 tests", "~90% coverage"]},
    {"id": "article-29", "slug": "article-29-compliance-engine-verification", "title": "Compliance Engine : Vérification automatique", "category": "Sécurité/Contenu", "priority": "medium", "format": "post", "date": "2026-01-13", "data": ["Mots interdits", "Disclaimers", "Validation"]},
    {"id": "article-30", "slug": "article-30-templates-head-of-email", "title": "Templates Head of : Campagnes email optimisées", "category": "Broadcasting/Email", "priority": "medium", "format": "post", "date": "2026-01-13", "data": ["5 templates optimisés", "Éditeur complet"]},
    {"id": "article-31", "slug": "article-31-social-campaign-engine-8-plateformes", "title": "Social Campaign Engine : 8 plateformes unifiées", "category": "Broadcasting/Social", "priority": "high", "format": "article", "date": "2026-01-13", "data": ["LinkedIn, Instagram, TikTok, YouTube, Facebook, Threads, Bluesky, Pinterest"]},
    {"id": "article-32", "slug": "article-32-oauth-comptes-sociaux-connexion-unifiee", "title": "OAuth comptes sociaux : Connexion unifiée", "category": "Broadcasting/Integration", "priority": "medium", "format": "post", "date": "2026-01-14", "data": ["LinkedIn, Twitter/X, TikTok", "Meta Graph API"]},
    {"id": "article-33", "slug": "article-33-platform-adapters-adaptation-contenu", "title": "Platform Adapters : Adaptation contenu automatique", "category": "Broadcasting/Adaptation", "priority": "medium", "format": "post", "date": "2026-01-14", "data": ["4 adaptateurs", "LinkedIn, Instagram, Twitter, TikTok"]},
    {"id": "article-34", "slug": "article-34-launch-scenario-builder-storytelling", "title": "Launch Scenario Builder : Storytelling automatisé", "category": "Broadcasting/Narrative", "priority": "medium", "format": "post", "date": "2026-01-14", "data": ["Teasing → lancement → followup", "Templates"]},
    {"id": "article-35", "slug": "article-35-performance-dashboard-cross-platform", "title": "Performance Dashboard cross-platform", "category": "Broadcasting/Analytics", "priority": "medium", "format": "post", "date": "2026-01-14", "data": ["Analytics unifiées", "Comparaison plateformes"]},
    {"id": "article-36", "slug": "article-36-content-campaign-manager-architecture", "title": "Content Campaign Manager : Architecture complète", "category": "Broadcasting/Architecture", "priority": "medium", "format": "article", "date": "2026-01-15", "data": ["6 modèles", "API REST", "100+ tests", "~2,500 lignes"]},
    {"id": "article-37", "slug": "article-37-campagnes-email-sequences-automatisees", "title": "Campagnes email : Séquences automatisées", "category": "Broadcasting/Email", "priority": "medium", "format": "post", "date": "2026-01-15", "data": ["Statuts, actions", "Tracking", "Templates"]},
    {"id": "article-38", "slug": "article-38-monitoring-email-automatique", "title": "Monitoring email automatique", "category": "Broadcasting/Email", "priority": "medium", "format": "post", "date": "2026-01-15", "data": ["Détection réponses", "Arrêt relances auto"]},
    {"id": "article-39", "slug": "article-39-seo-geo-optimisation-articles", "title": "SEO/GEO : Optimisation articles utilisateurs", "category": "SEO/Technique", "priority": "medium", "format": "post", "date": "2026-01-15", "data": ["Schema.org", "Open Graph", "Twitter Cards", "sitemap"]},
    {"id": "article-40", "slug": "article-40-api-llm-info-referencement-ia", "title": "API LLM Info : Optimisation référencement IA", "category": "SEO/IA", "priority": "medium", "format": "post", "date": "2026-01-15", "data": ["Endpoint /api/llm-info/", "Optimisation ChatGPT/Claude"]},
    {"id": "article-42", "slug": "article-42-django-orm-optimisations-bulk", "title": "Django ORM : Optimisations bulk", "category": "Technique/Django", "priority": "medium", "format": "post", "date": "2026-01-16", "data": ["select_related", "prefetch_related", "461 classes"]},
    {"id": "article-43", "slug": "article-43-drf-architecture-scalable-83-endpoints", "title": "DRF architecture scalable : 83 endpoints", "category": "Technique/Django", "priority": "high", "format": "post", "date": "2026-01-16", "data": ["83 fichiers View/Model", "API REST"]},
    {"id": "article-44", "slug": "article-44-celery-redis-orchestration-asynchrones", "title": "Celery + Redis : Orchestration asynchrones", "category": "Technique/Python", "priority": "high", "format": "article", "date": "2026-01-16", "data": ["Celery 5.5.3", "Redis 6.4.0", "Celery Beat"]},
    {"id": "article-45", "slug": "article-45-async-vs-celery-quand-utiliser", "title": "Async vs Celery : quand utiliser", "category": "Technique/Python", "priority": "medium", "format": "post", "date": "2026-01-17", "data": ["Django 5.2 async", "Celery tâches longues"]},
    {"id": "article-46", "slug": "article-46-django-migrations-gestion-complexes", "title": "Django migrations : Gestion complexes", "category": "Technique/Django", "priority": "medium", "format": "post", "date": "2026-01-17", "data": ["83 apps", "Dépendances", "Rollback"]},
    {"id": "article-47", "slug": "article-47-django-signals-vs-methodes-models", "title": "Django signals : vs méthodes models", "category": "Technique/Django", "priority": "medium", "format": "post", "date": "2026-01-17", "data": ["Patterns Django", "Performance"]},
    {"id": "article-48", "slug": "article-48-django-middleware-logging-cors", "title": "Django middleware : Logging, CORS, sécurité", "category": "Technique/Django", "priority": "medium", "format": "post", "date": "2026-01-17", "data": ["Custom middleware", "CORS", "Security headers"]},
    {"id": "article-49", "slug": "article-49-django-admin-personnalisation-b2b", "title": "Django admin : Personnalisation SaaS B2B", "category": "Technique/Django", "priority": "medium", "format": "post", "date": "2026-01-18", "data": ["83 fichiers admin.py", "Customisations"]},
    {"id": "article-50", "slug": "article-50-django-testing-coverage-70-95", "title": "Django testing : Coverage 70% → 95%", "category": "Technique/Django", "priority": "medium", "format": "post", "date": "2026-01-18", "data": ["Coverage 70.59%", "Objectif 95%", "97.67% success"]},
    {"id": "article-51", "slug": "article-51-module-monitoring-production", "title": "Module Monitoring Production", "category": "Technique/DevOps", "priority": "medium", "format": "post", "date": "2026-01-18", "data": ["SystemHealth", "ErrorLog", "PerformanceMetric"]},
    {"id": "article-52", "slug": "article-52-security-audit-audit-securite-complet", "title": "Security Audit : Audit sécurité complet", "category": "Sécurité/Audit", "priority": "medium", "format": "post", "date": "2026-01-18", "data": ["SecurityAudit", "README_SECURITY", "Audit détaillé"]},
    {"id": "article-53", "slug": "article-53-docker-compose-multi-services", "title": "Docker Compose multi-services : 9+ services", "category": "Technique/Docker", "priority": "high", "format": "article", "date": "2026-01-18", "data": ["Django, PostgreSQL, Redis, Celery, n8n, Flowise, Tor", "Architecture multi-containers"]}
]

print(f"Total articles à générer: {len(articles_to_generate)}")
print("Structure JSON prête pour génération")

