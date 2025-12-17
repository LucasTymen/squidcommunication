# 📐 Schéma Visuel - Campaign Manager

**Date** : 2025-12-12

---

## 🏗️ Architecture Hiérarchique

```
┌─────────────────────────────────────────────────────────────┐
│                    CAMPAIGN MANAGER                           │
│                  (Interface Drag & Drop)                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │      CATÉGORIES (Dossiers)          │
        │  ┌──────────────────────────────┐   │
        │  │ Articles Techniques          │   │
        │  │ Articles Business            │   │
        │  │ Articles Python              │   │
        │  └──────────────────────────────┘   │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │      CAMPAGNES (Sous-dossiers)      │
        │  ┌──────────────────────────────┐   │
        │  │ Campagne Q1 2026             │   │
        │  │ Campagne Q2 2026             │   │
        │  │ Campagne Incubateurs          │   │
        │  └──────────────────────────────┘   │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │      ARTICLES (Drag & Drop)         │
        │  ┌──────────────────────────────┐   │
        │  │ 📄 Article 1 (ordre: 1)     │   │
        │  │ 📄 Article 2 (ordre: 2)     │   │
        │  │ 📄 Article 3 (ordre: 3)     │   │
        │  │ ...                          │   │
        │  │ 📄 Article 34 (ordre: 34)   │   │
        │  └──────────────────────────────┘   │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │      CONTENU DE BASE (Markdown)    │
        │  ┌──────────────────────────────┐   │
        │  │ content.md                   │   │
        │  │ (Texte Markdown unique)      │   │
        │  └──────────────────────────────┘   │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │      TEMPLATES (Adaptations)        │
        │  ┌──────────────────────────────┐   │
        │  │ linkedin-article.md          │   │
        │  │ linkedin-carousel.md         │   │
        │  │ instagram-post.md            │   │
        │  │ twitter-thread.md            │   │
        │  └──────────────────────────────┘   │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │      DÉPLOIEMENT (Multi-plateformes)│
        │  ┌──────────────────────────────┐   │
        │  │ LinkedIn (article)            │   │
        │  │ LinkedIn (carousel)           │   │
        │  │ Instagram (post)              │   │
        │  │ Twitter (thread)              │   │
        │  └──────────────────────────────┘   │
        └─────────────────────────────────────┘
```

---

## 🎨 Interface Drag & Drop

```
┌─────────────────────────────────────────────────────────────┐
│  Campaign Manager - Campagne Q1 2026                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📁 Articles Techniques                                     │
│    └─ 📁 Campagne Q1 2026                                   │
│         ├─ 📄 Article 1 (draft)      [drag]                │
│         ├─ 📄 Article 2 (ready)      [drag]                │
│         ├─ 📄 Article 3 (draft)      [drag]                │
│         └─ ... (31 autres articles)                        │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  📄 Article 1 - Gain de temps (93%)                  │   │
│  │  ────────────────────────────────────────────────   │   │
│  │  Status: draft | ready | published                  │   │
│  │                                                      │   │
│  │  📝 Contenu de base:                                │   │
│  │  [Éditeur Markdown]                                 │   │
│  │                                                      │   │
│  │  🎨 Templates générés:                              │   │
│  │  ✅ LinkedIn Article                                 │   │
│  │  ✅ LinkedIn Carousel                                │   │
│  │  ✅ Instagram Post                                   │   │
│  │  ⏳ Twitter Thread (en cours)                        │   │
│  │                                                      │   │
│  │  🚀 Déploiements:                                   │   │
│  │  📅 LinkedIn Article: 15/12/2025 10:00              │   │
│  │  📅 Instagram Post: 16/12/2025 14:00                │   │
│  │                                                      │   │
│  │  [Générer Templates] [Planifier] [Déployer]         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  📁 Articles Business                                       │
│    └─ 📁 Campagne Q2 2026                                   │
│         └─ [Zone de drop pour déplacer articles]            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Workflow Complet

```
1. CRÉATION
   ┌─────────────┐
   │ Créer       │
   │ Campagne    │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │ Ajouter     │
   │ Articles    │
   │ (34)        │
   └──────┬──────┘
          │
          ▼
2. ORGANISATION
   ┌─────────────┐
   │ Drag & Drop │
   │ Réorganiser │
   │ Articles    │
   └──────┬──────┘
          │
          ▼
3. CONTENU
   ┌─────────────┐
   │ Éditer      │
   │ content.md  │
   │ (Markdown)  │
   └──────┬──────┘
          │
          ▼
4. ADAPTATION
   ┌─────────────┐
   │ Générer     │
   │ Templates   │
   │ (Auto)      │
   └──────┬──────┘
          │
          ▼
5. PLANIFICATION
   ┌─────────────┐
   │ Planifier   │
   │ Déploiement │
   │ (Calendrier)│
   └──────┬──────┘
          │
          ▼
6. DÉPLOIEMENT
   ┌─────────────┐
   │ Publier     │
   │ Multi-plate │
   │ formes      │
   └──────┬──────┘
          │
          ▼
7. ANALYTICS
   ┌─────────────┐
   │ Suivre      │
   │ Performance │
   └─────────────┘
```

---

## 📊 Exemple Concret : Campagne 34 Articles

```
Campagne Q1 2026 (34 articles)
├── Article 1: Gain de temps (93%)
│   ├── content.md (650 mots)
│   ├── templates/
│   │   ├── linkedin-article.md (650 mots)
│   │   ├── linkedin-carousel.md (5 slides)
│   │   ├── instagram-post.md (300 mots)
│   │   └── twitter-thread.md (8 tweets)
│   └── deployment/
│       ├── linkedin-article: 15/12/2025 10:00
│       ├── linkedin-carousel: 16/12/2025 10:00
│       ├── instagram-post: 17/12/2025 14:00
│       └── twitter-thread: 18/12/2025 09:00
│
├── Article 2: Enrichissement (100%)
│   └── (même structure)
│
├── Article 3: Matching IA
│   └── (même structure)
│
└── ... (31 autres articles)
```

**Total déploiements** : 34 articles × 4 formats = **136 déploiements**

---

## 🎯 Avantages de cette Architecture

1. **Hiérarchie claire** : Catégories → Campagnes → Articles
2. **Contenu unique** : Un seul `content.md` par article
3. **Adaptation automatique** : Templates générés depuis le contenu de base
4. **Déploiement flexible** : Chaque template peut être déployé indépendamment
5. **Organisation visuelle** : Drag & drop pour réorganiser facilement

---

**Dernière mise à jour** : 2025-12-12

