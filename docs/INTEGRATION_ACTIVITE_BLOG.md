# 📋 Intégration page activité ↔ blog personnel

> Document de référence pour l'orchestrateur et l'équipe technique — mise en relation de la page d'activité et du blog pour échange d'informations.

**Dernière mise à jour** : 2026-02-16

---

## 1. Chemins relatifs et absolus

### Racine du projet

| Contexte | Chemin |
|----------|--------|
| **Racine absolue** | `/home/lucas/tools/squidCommunication` |
| **Racine relative** (depuis le repo) | `.` ou `squidCommunication/` |

### Chemins relatifs à la racine

```
squidCommunication/
├── articles-complete.json      # Registre principal des articles (97 articles)
├── articles-pedagogiques.json  # Registre pédagogique (40 articles)
├── articles-planning.json      # Planification des articles
├── communication_log.md        # Journal des mises à jour communication
│
├── landing/                    # Site vitrine (Next.js) — page activité + blog
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx        # Page d'accueil (activité)
│   │   │   ├── blog/
│   │   │   │   ├── page.tsx    # Liste des articles du blog
│   │   │   │   └── [slug]/page.tsx  # Article individuel
│   │   │   ├── sitemap.ts
│   │   │   └── layout.tsx
│   │   └── lib/
│   │       ├── campaigns.ts    # Charge articles depuis articles/
│   │       ├── markdown.ts
│   │       └── seo.ts
│   └── package.json
│
├── articles/                   # Articles structurés (feed du blog)
│   └── article-XX-nom-slug/
│       ├── campaign.json       # Métadonnées (slug, SEO, statut)
│       ├── article.md          # Contenu markdown
│       └── platforms/          # Déclinaisons par plateforme
│           ├── linkedin/
│           ├── instagram/
│           └── ...
│
├── docs/                       # Documentation
│   ├── PUBLICATION_LOG.md      # Journal de publication
│   ├── ARTICLES_PEDAGOGIQUES.md
│   └── INTEGRATION_ACTIVITE_BLOG.md  # Ce document
│
├── scripts/                    # Scripts d'automatisation
│   ├── preview_article.py
│   ├── update_publication_log.py
│   └── ...
│
└── workflows/n8n/              # Workflows n8n
    └── publish_article_social.json
```

### Chemins depuis la racine du projet

| Fichier / Dossier | Chemin relatif | Usage |
|-------------------|----------------|-------|
| Registre articles principal | `articles-complete.json` | Base de connaissances, 97 articles |
| Registre pédagogique | `articles-pedagogiques.json` | 40 articles pédagogiques |
| Journal communication | `communication_log.md` | Log des campagnes et mises à jour |
| Journal publication | `docs/PUBLICATION_LOG.md` | Traçabilité articles publiés |
| Feed blog (landing) | `articles/` | Structure `article-XX/campaign.json` + `article.md` |
| Page activité | `landing/src/app/page.tsx` | Page d'accueil |
| Page blog liste | `landing/src/app/blog/page.tsx` | Liste des articles |
| Page article | `landing/src/app/blog/[slug]/page.tsx` | Article individuel |
| Loader articles | `landing/src/lib/campaigns.ts` | Charge depuis `../articles` (relatif à `landing/`) |

---

## 2. Les différents logs

| Log | Chemin | Contenu |
|-----|--------|---------|
| **Communication log** | `communication_log.md` | Journal des mises à jour, campagnes, features (2025-11 à 2026-02) |
| **Publication log** | `docs/PUBLICATION_LOG.md` | Articles publiés, prêts à publier, planning, statistiques |
| **Git logs** | `.git/logs/HEAD`, `.git/logs/refs/heads/main` | Historique des commits |

### Détail `communication_log.md`

- Entrées horodatées (format `[YYYY-MM-DD HH:MM]`)
- Campagnes préparées, scripts créés, articles convertis
- Statistiques (articles publiés, déclinaisons, taux de préparation)

### Détail `docs/PUBLICATION_LOG.md`

- Tableau articles publiés (slug, date, plateformes)
- Tableau articles prêts à publier (déclinaisons)
- Planning par priorité
- Historique des actions (validation, aperçu, publication)

---

## 3. Registre des articles

### Registre principal : `articles-complete.json`

- **Schéma** : `schema_version: "2.0"`
- **Métadonnées** : `total_articles`, `published`, `ready`, `draft`, `last_updated`
- **Structure par article** :
  - `id`, `slug`, `title`, `category`, `priority`, `status`
  - `content_markdown` : contenu complet
  - `seo` : primary_keywords, long_tail_keywords, hashtags, meta_title, meta_description
  - `planning` : start_date, publish_date, publish_time
  - `data_points`, `visualizations`, `comments`
- **Statut actuel** : 97 articles, 14 publiés, 44 prêts, 71 brouillons
- **Articles LinkedIn** : `article-linkedin-01` à `article-linkedin-13` (source: linkedin, status: published)

### Registre pédagogique : `articles-pedagogiques.json`

- 40 articles par catégorie (Python, Matching, Enrichissement, etc.)
- Structure similaire à `articles-complete.json`
- Fichier indépendant mais contenu potentiellement fusionné dans articles-complete

### Feed du blog (landing) : `articles/`

Le blog consomme les articles depuis le dossier `articles/` avec :
- Un dossier par article : `article-XX-nom-slug/`
- `campaign.json` : métadonnées (campaign_id, slug, content, seo, status)
- `article.md` : contenu markdown
- Le loader `landing/src/lib/campaigns.ts` utilise `path.join(process.cwd(), "..", "articles")` (depuis `landing/`)

**Sync en place** : Le script `scripts/sync_articles_registry.py` synchronise les articles published/ready du registre vers `articles/`. Exécuter après chaque mise à jour du registre.

---

## 4. Synchronisation des équipes

### Workflow de synchronisation

| Équipe | Rôle | Fichiers / Actions |
|--------|------|--------------------|
| **Rédaction** | Créer et publier du contenu | `articles-complete.json` — Ajouter des articles, définir `status: "published"` ou `"ready"` |
| **Technique** | Alimenter le blog et la page activité | `python scripts/sync_articles_registry.py` — Crée `articles/*/campaign.json` + `article.md` pour chaque article published/ready |
| **Web design** | Mise en page et UX | `landing/src/app/page.tsx`, `landing/src/app/blog/` — Affiche les articles sur la page d'accueil et le blog |

### Commandes

```bash
# Synchroniser le registre vers le blog (depuis la racine du projet)
python scripts/sync_articles_registry.py

# Dry-run (afficher sans écrire)
python scripts/sync_articles_registry.py --dry-run
```

### Flux de données

```
articles-complete.json (registre)
        │
        │  sync_articles_registry.py
        ▼
articles/ (dossiers par article)
   ├── campaign.json
   └── article.md
        │
        │  loadAllArticles() / loadArticleBySlug()
        ▼
landing (Next.js)
   ├── Page d'accueil (Derniers articles, Épisodes publiés)
   └── Blog (/blog, /blog/[slug])
```

---

## 5. Points d'intégration pour activité ↔ blog

### Pour alimenter le blog depuis le registre

- **Source de vérité** : `articles-complete.json`
- **Cible** : `articles/` (structure `campaign.json` + `article.md`)
- **Script** : `python scripts/sync_articles_registry.py` — synchronise les articles published/ready (pour les articles `status: published` ou `ready`)

### Pour alimenter la page activité

- La page `landing/src/app/page.tsx` est la page d'accueil
- Peut consommer des métriques ou résumés depuis `articles-complete.json` (ex. nombre d’articles, derniers publiés)
- Ou depuis une API / fichier dérivé

### Chemins relatifs depuis `landing/`

- Vers registre : `../articles-complete.json`
- Vers articles : `../articles/`
- Vers docs : `../docs/`

---

## 6. Récapitulatif pour l'orchestrateur

| Besoin | Fichier / Chemin | Format |
|--------|------------------|--------|
| Liste complète des articles | `articles-complete.json` | JSON |
| Articles pédagogiques | `articles-pedagogiques.json` | JSON |
| Journal des campagnes | `communication_log.md` | Markdown |
| Journal des publications | `docs/PUBLICATION_LOG.md` | Markdown |
| Articles affichés sur le blog | `articles/*/campaign.json` + `article.md` | JSON + MD |
| Racine du projet | `/home/lucas/tools/squidCommunication` ou `.` | — |

---

## 7. Contact technique

Pour toute question sur l’intégration : se référer à ce document et aux chemins indiqués.
