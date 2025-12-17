# 📁 Exemple Structure - Campaign Manager

**Objectif** : Montrer la structure concrète d'une campagne multi-articles

---

## 📂 Structure Complète

```
categories/
├── articles-techniques/
│   ├── category.json
│   └── campagne-q1-2026/
│       ├── campaign.json
│       ├── deployment.json
│       └── articles/
│           ├── article-1-example/
│           │   ├── content.md (contenu de base)
│           │   ├── metadata.json
│           │   ├── templates/
│           │   │   ├── linkedin-article.md
│           │   │   ├── linkedin-carousel.md
│           │   │   ├── instagram-post.md
│           │   │   └── twitter-thread.md
│           │   └── deployment/
│           │       └── (logs de déploiement)
│           ├── article-2/
│           ├── article-3/
│           └── ... (34 articles au total)
│
├── articles-business/
│   └── campagne-q2-2026/
│
└── articles-python/
    └── campagne-incubateurs/
```

---

## 🎯 Workflow

1. **Créer campagne** → `campaign.json` avec liste d'articles
2. **Créer articles** → Dossiers avec `content.md` et `metadata.json`
3. **Générer templates** → Adaptation automatique par plateforme
4. **Organiser** → Drag & drop pour réorganiser l'ordre
5. **Planifier** → `deployment.json` avec dates de publication
6. **Déployer** → Publication automatique multi-plateformes

---

## 📝 Fichiers Clés

- **`category.json`** : Métadonnées de la catégorie
- **`campaign.json`** : Métadonnées de la campagne + liste articles
- **`content.md`** : Contenu de base Markdown (unique par article)
- **`metadata.json`** : Métadonnées de l'article
- **`templates/*.md`** : Adaptations par plateforme/format
- **`deployment.json`** : Planification et logs de déploiement

---

**Note** : Ceci est un exemple. La structure réelle sera générée par les scripts CLI.

