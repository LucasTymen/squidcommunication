# 🎨 Guide Visualisations Qualité - Articles LinkedIn

> **Version** : 1.0.0  
> **Date** : 2026-01-05  
> **Objectif** : Standards et processus pour créer des visualisations de qualité (graphiques, infographies)

---

## 🎯 Objectif & Philosophie

**Principes** :
- **Qualité avant tout** : Visualisations professionnelles, épurées, aérées
- **Cohérence visuelle** : Style uniforme sur tous les articles
- **Lisibilité** : Informations claires, hiérarchie visuelle évidente
- **Data-driven** : Utiliser uniquement métriques réelles mesurées

**Outils Recommandés** :
- **Napkin** : Graphiques et diagrammes techniques (recommandé pour data)
- **Canva** : Infographies, carrousels (si besoin)
- **Excalidraw** : Schémas techniques simples
- **Figma** : Design system avancé (si ressources disponibles)

---

## 📊 Types de Visualisations par Article

### 1. Articles Business/ROI

**Visualisations Nécessaires** :
- **Graphiques de performance** : Gains de temps, ROI, métriques mesurées
- **Comparaisons avant/après** : Temps manuel vs automatisé
- **Graphiques temporels** : Évolution des métriques

**Format Recommandé** : Napkin (graphiques data)

**Exemple Article 10 "100% taux réussite enrichissement"** :
```
- Graphique barres : Temps moyen enrichissement (82s vs 20min manuel)
- Graphique camembert : Taux réussite (100% vs moyenne secteur)
- Tableau : Métriques (6-7 emails/recherche, 82s moyen)
```

**Spécifications Napkin** :
- Style : Minimalist, clean
- Couleurs : Palette SquidResearch (à définir)
- Typographie : Lisible, sans-serif

---

### 2. Articles Techniques/Algo

**Visualisations Nécessaires** :
- **Diagrammes d'architecture** : Flux algorithmique, structure
- **Graphiques de scoring** : Distribution scores, critères pondération
- **Schémas techniques** : Workflow, processus

**Format Recommandé** : Napkin (diagrammes) + Excalidraw (schémas simples)

**Exemple Article 3 "Algorithmes matching intelligents"** :
```
- Diagramme de flux : Processus matching (entrée CV → critères → score)
- Graphique barres : Pondération critères (40% compétences, 25% mission, etc.)
- Schéma : Architecture algorithme (inputs → calcul → outputs)
```

**Spécifications** :
- Style : Technique mais accessible
- Légendes : Clairement identifiées
- Couleurs : Différenciées par catégorie

---

### 3. Articles IA/Automatisation

**Visualisations Nécessaires** :
- **Diagrammes workflow** : Orchestration, pipelines IA
- **Graphiques de performance** : Temps de traitement, accuracy
- **Schémas architecture** : n8n + Flowise, intégrations

**Format Recommandé** : Napkin (workflows) + Excalidraw (schémas)

**Exemple Article 23 "Module IA Documents"** :
```
- Diagramme workflow : CV → Analyse IA → Scoring ATS → Suggestions
- Graphique barres : Coverage tests (94.23%), performance
- Schéma architecture : n8n + Flowise + Django
```

---

### 4. Articles Docker/Infrastructure

**Visualisations Nécessaires** :
- **Schémas architecture** : Multi-containers, networking
- **Graphiques de performance** : Réduction taille images, optimisation
- **Diagrammes de flux** : Démarrage séquentiel, health checks

**Format Recommandé** : Excalidraw (architecture) + Napkin (performance)

**Exemple Article 53 "Docker Compose multi-services"** :
```
- Schéma architecture : 9 services (Django, PostgreSQL, Redis, etc.)
- Graphique : Taille images (2GB → 800MB)
- Diagramme flux : Démarrage séquentiel (db → web → worker)
```

---

### 5. Carrousels (5% des articles)

**Visualisations Nécessaires** :
- **Slides structurées** : 5-10 slides avec infographies
- **Métriques visuelles** : Chiffres clés, comparaisons
- **Graphiques multiples** : Différentes métriques par slide

**Format Recommandé** : Canva (templates carrousels) + Napkin (graphiques)

**Structure Carrousel** :
```
Slide 1 : Titre + Accroche visuelle
Slide 2 : Problème (graphique/métrique)
Slide 3 : Solution (diagramme)
Slide 4 : Résultat (graphique performance)
Slide 5 : CTA
```

**Spécifications Canva** :
- Dimensions : 1080x1080px (carré) pour LinkedIn
- Template réutilisable : Style cohérent
- Graphiques : Import depuis Napkin si besoin

---

## 🛠️ Processus de Création

### Phase 1 : Préparation

**1. Identifier les visualisations nécessaires** :
- Lire article rédigé
- Identifier métriques/data à visualiser
- Déterminer type de visualisation (graphique, diagramme, schéma)

**2. Préparer les données** :
- Extraire métriques réelles depuis `growth/data-driven-metrics.md`
- Structurer données pour visualisation
- Vérifier cohérence chiffres

**Exemple Préparation** :
```
Article : "100% taux réussite enrichissement"

Données à visualiser :
- Temps enrichissement : 82s vs 20min (97% gain)
- Taux réussite : 100% (15+ entreprises testées)
- Emails trouvés : 6-7/recherche (moyenne)

Visualisations :
1. Graphique barres : Comparaison temps (82s vs 20min)
2. Graphique camembert : Taux réussite (100%)
3. Tableau : Métriques détaillées
```

---

### Phase 2 : Création Napkin

**1. Créer compte/workspace Napkin** :
- Setup palette couleurs SquidResearch (à définir)
- Template de base pour graphiques
- Style cohérent (minimalist, clean)

**2. Créer graphiques** :

**Graphique Barres** (Comparaison temps) :
```
Titre : "Temps moyen enrichissement contact"
Axe X : Méthode (Manuel vs Automatique)
Axe Y : Temps (secondes)
Barres :
  - Manuel : 1200s (20min)
  - Automatique : 82s
Légende : 97% de gain de temps
Style : Minimalist, couleurs contrastées
```

**Graphique Camembert** (Taux réussite) :
```
Titre : "Taux de réussite enrichissement"
Données :
  - Réussite : 100% (15 entreprises)
  - Échec : 0%
Style : Simple, 2 couleurs (vert réussite, gris échec)
```

**3. Exporter graphiques** :
- Format : PNG haute résolution (300 DPI minimum)
- Dimensions : Adaptées à l'article (largeur max 1200px pour LinkedIn)
- Nommage : `article-{id}-graphique-{type}.png`

---

### Phase 3 : Intégration Article

**1. Ajouter visualisations dans JSON** :

```json
{
  "id": "article-10",
  "visualizations": {
    "enabled": true,
    "images": [
      {
        "id": "graphique-temps-enrichissement",
        "type": "bar_chart",
        "tool": "napkin",
        "file": "assets/article-10-graphique-temps.png",
        "alt": "Comparaison temps enrichissement : 82s vs 20min",
        "caption": "Temps moyen enrichissement contact : 97% de gain avec automatisation"
      },
      {
        "id": "graphique-taux-reussite",
        "type": "pie_chart",
        "tool": "napkin",
        "file": "assets/article-10-graphique-taux.png",
        "alt": "Taux réussite enrichissement : 100%",
        "caption": "100% de taux de réussite sur 15+ entreprises testées"
      }
    ]
  }
}
```

**2. Référencer dans article Markdown** :

```markdown
J'ai testé l'algorithme sur 15 entreprises. Résultat : 100% de taux de réussite, 
6-7 emails trouvés par recherche, 82 secondes en moyenne.

![Comparaison temps enrichissement](assets/article-10-graphique-temps.png)

Le graphique montre un gain de 97% par rapport à la recherche manuelle.

![Taux réussite enrichissement](assets/article-10-graphique-taux.png)

Sur 15 entreprises testées, aucune recherche n'a échoué.
```

---

### Phase 4 : Qualité & Validation

**Checklist Qualité** :

- [ ] **Résolution** : 300 DPI minimum (haute qualité)
- [ ] **Dimensions** : Adaptées LinkedIn (max 1200px largeur)
- [ ] **Lisibilité** : Texte clair, légendes visibles
- [ ] **Cohérence** : Style uniforme, palette couleurs cohérente
- [ ] **Data accurate** : Chiffres correspondant aux métriques réelles
- [ ] **Accessibilité** : Alt text descriptif, contraste suffisant
- [ ] **Format** : PNG haute qualité (ou SVG si vectoriel)

**Validation** :
- Vérifier correspondance chiffres graphique vs article
- Contrôler lisibilité (texte lisible à petite taille)
- Valider cohérence visuelle avec autres articles

---

## 📐 Standards Visuels

### Palette Couleurs (À Définir)

**Proposition Palette SquidResearch** :
- **Primaire** : Bleu tech (ex: #0ea5e9)
- **Secondaire** : Violet (ex: #8b5cf6)
- **Success** : Vert (ex: #10b981)
- **Neutral** : Gris (ex: #6b7280)
- **Accent** : Orange (ex: #f59e0b)

**Usage** :
- Graphiques performance : Bleu (automatique) vs Gris (manuel)
- Taux réussite : Vert (100%)
- Comparaisons : Couleurs contrastées mais harmonieuses

---

### Typographie

**Police Graphiques** :
- **Titres** : Sans-serif bold (ex: Inter Bold)
- **Légendes** : Sans-serif regular (ex: Inter Regular)
- **Chiffres** : Sans-serif bold, grande taille (ex: Inter Bold 24pt)

**Hiérarchie** :
- Titre : 20-24pt
- Légendes axes : 12-14pt
- Données labels : 14-16pt
- Notes : 10-12pt

---

### Style Graphiques

**Barres** :
- Largeur barres : 40-60px
- Espacement : 20-30px entre barres
- Couleurs : Contrastées, cohérentes
- Grille : Subtile, pas intrusive

**Lignes** :
- Épaisseur lignes : 2-3px
- Points : 6-8px diamètre
- Légendes : Claires, visibles

**Camemberts** :
- Maximum 5 segments (au-delà, regrouper)
- Légendes : Extérieures, lisibles
- Pourcentages : Visibles sur segments si >5%

**Schémas** :
- Flèches : Nettes, direction claire
- Boîtes : Arrondies légèrement (4-8px radius)
- Espacement : Aéré, pas surchargé

---

## 🔄 Workflow Intégré

### Dans `articles-planning.json` :

```json
{
  "id": "article-10",
  "visualizations": {
    "enabled": true,
    "tool": "napkin",
    "required": [
      {
        "type": "bar_chart",
        "data": {
          "manuel": 1200,
          "automatique": 82
        },
        "title": "Temps moyen enrichissement",
        "status": "pending" // pending | in_progress | done
      },
      {
        "type": "pie_chart",
        "data": {
          "reussite": 100,
          "echec": 0
        },
        "title": "Taux réussite",
        "status": "pending"
      }
    ],
    "images": []
  }
}
```

### Script d'Intégration (Futur)

**`scripts/prepare_visualizations.py`** :
- Lit `articles-planning.json`
- Identifie visualisations `status: pending`
- Génère spécifications Napkin (manuel pour l'instant)
- Met à jour statut `in_progress` → `done` après création

---

## 📚 Ressources & Outils

### Napkin

**Avantages** :
- Graphiques data professionnels
- Export haute résolution
- Style minimaliste adapté
- Templates réutilisables

**Process** :
1. Créer workspace SquidResearch
2. Définir palette couleurs (une fois)
3. Créer template de base (une fois)
4. Réutiliser pour tous les articles

**Exemples Types Graphiques** :
- Bar charts (comparaisons)
- Line charts (évolutions)
- Pie charts (répartition)
- Scatter plots (corrélations)
- Flowcharts (processus)

---

### Canva (Carrousels)

**Avantages** :
- Templates carrousels LinkedIn (1080x1080px)
- Design system facile
- Export optimisé

**Usage** :
- Uniquement pour carrousels (5% des articles)
- Template réutilisable par catégorie
- Graphiques importés depuis Napkin si besoin

---

### Excalidraw (Schémas Techniques)

**Avantages** :
- Schémas techniques simples
- Style "hand-drawn" professionnel
- Export PNG/SVG

**Usage** :
- Architecture systèmes
- Workflows simples
- Diagrammes de flux

---

## ✅ Checklist Création Visualisation

### Avant Création

- [ ] **Article rédigé** : Contenu finalisé avec données réelles
- [ ] **Données validées** : Métriques correspondant à `growth/data-driven-metrics.md`
- [ ] **Type identifié** : Graphique, diagramme, schéma
- [ ] **Outil choisi** : Napkin, Canva, Excalidraw selon type

### Pendant Création

- [ ] **Palette cohérente** : Couleurs SquidResearch
- [ ] **Style uniforme** : Minimalist, clean, aéré
- [ ] **Lisibilité** : Texte clair, légendes visibles
- [ ] **Data accurate** : Chiffres exacts, pas d'arrondis trompeurs

### Après Création

- [ ] **Export haute qualité** : PNG 300 DPI minimum
- [ ] **Dimensions adaptées** : Max 1200px largeur pour LinkedIn
- [ ] **Nommage cohérent** : `article-{id}-graphique-{type}.png`
- [ ] **Alt text** : Description claire pour accessibilité
- [ ] **Intégration JSON** : Ajouter dans `visualizations.images`
- [ ] **Validation** : Vérifier correspondance chiffres vs article

---

## 🎨 Exemples Concrets

### Article 10 : "100% taux réussite enrichissement"

**Visualisations Nécessaires** :

1. **Graphique Barres** : Temps enrichissement
   - Napkin : Bar chart
   - Données : 82s (auto) vs 1200s (manuel)
   - Style : Minimalist, couleurs contrastées
   - Export : `article-10-graphique-temps.png`

2. **Graphique Camembert** : Taux réussite
   - Napkin : Pie chart
   - Données : 100% réussite, 0% échec
   - Style : Simple, 2 couleurs
   - Export : `article-10-graphique-taux.png`

3. **Tableau Métriques** : Détails performance
   - Napkin : Table chart
   - Données : 6-7 emails/recherche, 82s moyen, 15 entreprises
   - Style : Minimalist, lisible
   - Export : `article-10-tableau-metriques.png`

---

### Article 3 : "Algorithmes matching intelligents"

**Visualisations Nécessaires** :

1. **Diagramme Flux** : Processus matching
   - Excalidraw : Flowchart
   - Flux : CV → Analyse → Critères → Score → Output
   - Style : Technique mais accessible
   - Export : `article-3-diagramme-flux.png`

2. **Graphique Barres** : Pondération critères
   - Napkin : Bar chart horizontal
   - Données : 40% compétences, 25% mission, 15% expérience, etc.
   - Style : Minimalist, couleurs différenciées
   - Export : `article-3-graphique-ponderation.png`

---

## 📖 Documentation Référence

**Métriques Réelles** :
- `growth/data-driven-metrics.md` : Toutes les métriques business/techniques
- `communication_log.md` : Historique fonctionnalités

**Articles Exhaustifs** :
- `docs/ARTICLES_LISTE_EXHAUSTIVE.md` : Données disponibles par article

**Charte Éditoriale** :
- `docs/CHARTE_EDITORIALE_STRICTE.md` : Règles rédaction (pas d'hallucination)

---

**Dernière mise à jour** : 2026-01-05  
**Règle absolue** : Utiliser uniquement métriques réelles, visualisations de qualité professionnelle

