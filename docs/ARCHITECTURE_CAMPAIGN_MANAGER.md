# 🏗️ Architecture - Campaign Manager Multi-Articles

**Date** : 2025-12-12  
**Objectif** : Plateforme de gestion de campagnes multi-articles avec déploiement multi-plateformes

---

## 🎯 Vue d'Ensemble

### Besoins Identifiés

1. **Campagne multi-articles** : Une campagne peut contenir 34+ articles
2. **Déploiement multi-plateformes** : Chaque article adapté pour LinkedIn, Instagram, Twitter, etc.
3. **Templates par format** : Article, carousel, story, etc.
4. **Organisation hiérarchique** : Catégories → Campagnes → Articles
5. **Interface drag & drop** : Organiser visuellement les articles

---

## 📁 Structure de Données

### Hiérarchie

```
categories/
├── articles-techniques/
│   ├── campagne-q1-2026/
│   │   ├── campaign.json
│   │   ├── articles/
│   │   │   ├── article-1-gain-temps/
│   │   │   │   ├── content.md (contenu de base Markdown)
│   │   │   │   ├── templates/
│   │   │   │   │   ├── linkedin-article.md
│   │   │   │   │   ├── linkedin-carousel.md
│   │   │   │   │   ├── instagram-post.md
│   │   │   │   │   └── twitter-thread.md
│   │   │   │   └── metadata.json
│   │   │   ├── article-2-enrichissement/
│   │   │   └── article-3-matching/
│   │   └── deployment.json
│   └── campagne-q2-2026/
├── articles-business/
└── articles-techniques-python/
```

### Schema JSON

#### `category.json`
```json
{
  "category_id": "articles-techniques",
  "name": "Articles Techniques",
  "description": "Articles techniques Python, Django, Docker",
  "campaigns": [
    "campagne-q1-2026",
    "campagne-q2-2026"
  ],
  "created_at": "2025-12-12T20:00:00Z",
  "updated_at": "2025-12-12T20:00:00Z"
}
```

#### `campaign.json`
```json
{
  "schema_version": "2.0",
  "campaign_id": "campagne-q1-2026",
  "category_id": "articles-techniques",
  "name": "Campagne Q1 2026",
  "description": "Articles techniques pour Q1 2026",
  "status": "draft | scheduled | active | completed",
  "created_at": "2025-12-12T20:00:00Z",
  "updated_at": "2025-12-12T20:00:00Z",
  "articles": [
    {
      "article_id": "article-1-gain-temps",
      "order": 1,
      "status": "draft | ready | published",
      "content_file": "articles/article-1-gain-temps/content.md",
      "templates": {
        "linkedin": {
          "article": "articles/article-1-gain-temps/templates/linkedin-article.md",
          "carousel": "articles/article-1-gain-temps/templates/linkedin-carousel.md"
        },
        "instagram": {
          "post": "articles/article-1-gain-temps/templates/instagram-post.md"
        },
        "twitter": {
          "thread": "articles/article-1-gain-temps/templates/twitter-thread.md"
        }
      },
      "deployment": {
        "linkedin": {
          "article": {
            "status": "draft",
            "scheduled_at": null,
            "published_at": null,
            "url": null
          },
          "carousel": {
            "status": "draft",
            "scheduled_at": null,
            "published_at": null,
            "url": null
          }
        },
        "instagram": {
          "post": {
            "status": "draft",
            "scheduled_at": null,
            "published_at": null,
            "url": null
          }
        }
      }
    }
  ],
  "kpis": {
    "target": {
      "total_articles": 34,
      "total_deployments": 100,
      "linkedin_impressions": 5000
    },
    "actual": {
      "total_articles": 3,
      "total_deployments": 0,
      "linkedin_impressions": 0
    }
  }
}
```

#### `article/metadata.json`
```json
{
  "article_id": "article-1-gain-temps",
  "title": "Comment j'ai réduit mon temps de candidature de 30 min à 2 min",
  "category": "articles-techniques",
  "campaign_id": "campagne-q1-2026",
  "order": 1,
  "status": "draft",
  "content_file": "content.md",
  "created_at": "2025-12-12T20:00:00Z",
  "updated_at": "2025-12-12T20:00:00Z",
  "tags": ["recrutement", "automatisation", "python"],
  "target_platforms": ["linkedin", "instagram", "twitter"],
  "templates_used": {
    "linkedin": ["article", "carousel"],
    "instagram": ["post"],
    "twitter": ["thread"]
  }
}
```

#### `deployment.json` (au niveau campagne)
```json
{
  "campaign_id": "campagne-q1-2026",
  "deployments": [
    {
      "article_id": "article-1-gain-temps",
      "platform": "linkedin",
      "format": "article",
      "status": "draft | scheduled | published",
      "scheduled_at": "2025-12-15T10:00:00Z",
      "published_at": null,
      "url": null,
      "analytics": {
        "impressions": 0,
        "engagement": 0,
        "clicks": 0
      }
    }
  ],
  "schedule": {
    "strategy": "spread | burst | custom",
    "start_date": "2025-12-15T10:00:00Z",
    "end_date": "2026-03-31T23:59:59Z",
    "frequency": "daily | weekly | custom"
  }
}
```

---

## 🎨 Système de Templates

### Structure Template

```
templates/
├── linkedin/
│   ├── article.md.template
│   ├── carousel.md.template
│   └── post.md.template
├── instagram/
│   ├── post.md.template
│   ├── carousel.md.template
│   └── story.md.template
└── twitter/
    ├── thread.md.template
    └── tweet.md.template
```

### Template Example : `linkedin/article.md.template`

```markdown
# {{title}}

{{content}}

---

**Question** : {{cta_question}}

Partagez vos expériences en commentaire 👇

---

{{hashtags}}
```

### Adaptation Automatique

**Règles par plateforme** :
- **LinkedIn Article** : Contenu complet (500-800 mots), format Markdown
- **LinkedIn Carousel** : 5-8 slides, 1 idée par slide, format court
- **Instagram Post** : 200-300 mots max, emojis, hashtags
- **Twitter Thread** : 5-10 tweets, 280 caractères max par tweet

**Script d'adaptation** :
```python
def adapt_content(content_md, platform, format_type):
    """
    Adapte le contenu Markdown de base pour une plateforme/format spécifique
    """
    if platform == "linkedin" and format_type == "article":
        return content_md  # Pas de modification
    elif platform == "linkedin" and format_type == "carousel":
        return convert_to_carousel(content_md)  # Découpe en slides
    elif platform == "instagram" and format_type == "post":
        return shorten_content(content_md, max_words=300)  # Raccourcir
    elif platform == "twitter" and format_type == "thread":
        return convert_to_thread(content_md)  # Découpe en tweets
```

---

## 🖥️ Interface Utilisateur

### Option 1 : Application Web Dédiée (Next.js/React)

**Avantages** :
- Interface moderne et réactive
- Drag & drop natif (react-beautiful-dnd, dnd-kit)
- Déploiement indépendant (Vercel)
- Stack moderne (Next.js 16, React 19, TypeScript)

**Structure** :
```
campaign-manager/
├── app/
│   ├── categories/
│   ├── campaigns/
│   ├── articles/
│   └── deployment/
├── components/
│   ├── DragDropArticleList.tsx
│   ├── TemplateSelector.tsx
│   ├── PlatformDeployment.tsx
│   └── CampaignDashboard.tsx
└── lib/
    ├── templates/
    └── adapters/
```

**Fonctionnalités** :
- Vue hiérarchique : Catégories → Campagnes → Articles
- Drag & drop : Déplacer articles entre campagnes
- Éditeur Markdown : Édition directe du contenu de base
- Prévisualisation : Voir l'adaptation par plateforme
- Planification : Calendrier de déploiement
- Analytics : Suivi des performances

### Option 2 : Intégration SquidResearch (Django)

**Avantages** :
- Intégration avec l'existant
- Base de données unifiée
- Authentification existante
- API REST déjà en place

**Structure** :
```
squidResearch/
├── apps/
│   └── campaigns/
│       ├── models.py (Campaign, Article, Deployment)
│       ├── views.py (API + Templates)
│       ├── templates/
│       │   └── campaigns/
│       │       ├── dashboard.html
│       │       ├── article_list.html (drag & drop)
│       │       └── deployment.html
│       └── static/
│           └── js/
│               └── drag-drop.js (SortableJS)
```

**Fonctionnalités** :
- Dashboard Django avec drag & drop (SortableJS)
- API REST pour CRUD campagnes/articles
- Templates Django pour l'interface
- Intégration avec apps existantes

---

## 🔄 Workflow

### 1. Création Campagne

```bash
# Script CLI
python scripts/create_campaign.py \
  --category "articles-techniques" \
  --name "Campagne Q1 2026" \
  --articles 34
```

### 2. Création Article

```bash
python scripts/create_article.py \
  --campaign "campagne-q1-2026" \
  --title "Article 1" \
  --content "content.md" \
  --platforms linkedin instagram twitter
```

### 3. Adaptation Templates

```bash
python scripts/adapt_templates.py \
  --article "article-1-gain-temps" \
  --platforms linkedin instagram twitter
```

### 4. Déploiement

```bash
python scripts/deploy_campaign.py \
  --campaign "campagne-q1-2026" \
  --platform linkedin \
  --format article \
  --schedule "2025-12-15T10:00:00Z"
```

---

## 🎯 Recommandation

**Option hybride** : Application Next.js pour l'interface + API Django SquidResearch

**Architecture** :
- **Frontend** : Next.js (campaign-manager) avec drag & drop
- **Backend** : API Django SquidResearch (apps/campaigns)
- **Stockage** : Fichiers Markdown dans `squidCommunication/`
- **Sync** : API REST entre Next.js et Django

**Avantages** :
- Interface moderne (Next.js)
- Réutilisation backend Django
- Séparation des responsabilités
- Déploiement indépendant

---

## 📋 Prochaines Étapes

1. **Phase 1** : Structure de données (JSON schemas)
2. **Phase 2** : Scripts CLI (création, adaptation, déploiement)
3. **Phase 3** : Interface drag & drop (Next.js ou Django)
4. **Phase 4** : Système de templates automatique
5. **Phase 5** : Déploiement multi-plateformes

---

**Dernière mise à jour** : 2025-12-12

