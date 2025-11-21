# 🎨 Prompts Animations & Infographies - Épisode 2

> **Format** : Carousel LinkedIn (9 slides, 1080x1080px chacun)  
> **Charte** : BOGOSS (gradients violets/bleus, style moderne)  
> **Intégration** : Animations CSS/JS + Infographies SVG/Canvas directement dans HTML  
> **Illustrations** : PNG si nécessaire (ChatGPT)

---

## 📋 Instructions générales

### Pour Claude (Animations + Infographies HTML)
- Créer des animations CSS/JS légères et performantes
- Générer des infographies SVG ou Canvas directement dans le HTML
- Utiliser la charte BOGOSS : `#6366f1` (violet), `#ec4899` (rose), `#10b981` (vert), `#06b6d4` (cyan)
- Format : 1080x1080px (viewport fixe)
- Performance : Animations fluides 60fps, pas de lag
- Responsive : S'assurer que tout s'adapte au format carré

### Pour ChatGPT (Illustrations PNG)
- Créer des illustrations PNG 1080x1080px, 300 DPI
- Style : Moderne, épuré, data-driven
- Fond transparent ou blanc selon besoin
- Charte BOGOSS respectée

---

## 🎠 Slide 1 : Architecture Docker Overview

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée de l'architecture Docker SquidResearch directement dans le HTML.

CONTEXTE :
- Format carousel LinkedIn : 1080x1080px
- Charte BOGOSS : #6366f1 (violet), #ec4899 (rose), #10b981 (vert), #06b6d4 (cyan)
- Gradient principal : linear-gradient(135deg, #667eea 0%, #764ba2 100%)

CONTENU À CRÉER :
1. **Infographie SVG** (intégrée dans HTML) :
   - 9 services représentés comme des conteneurs Docker stylisés avec icônes
   - Services : PostgreSQL, Django, React, Celery Worker, Celery Beat, n8n, Flowise, Redis, Tor
   - Réseau squidresearch_network représenté par des lignes de connexion
   - Flèches animées montrant les dépendances (db → web, redis → worker, etc.)

2. **Animations CSS** :
   - Apparition progressive des services (fade-in + slide-up avec délais échelonnés)
   - Pulsation douce des conteneurs actifs
   - Lignes de connexion qui s'animent (stroke-dasharray animation)
   - Flèches qui "pulsent" pour montrer le flux de données

3. **Effets visuels** :
   - Ombres portées animées (box-shadow avec animation)
   - Gradient animé sur le titre
   - Badges colorés avec hover effects

INTÉGRATION :
- Tout doit être dans un seul fichier HTML
- Utiliser SVG inline pour les infographies
- CSS animations dans <style>
- Pas de dépendances externes
- Performance optimisée (will-change, transform, opacity)

RÉSULTAT : HTML complet avec infographie SVG animée, prêt pour carousel LinkedIn
```

### Prompt ChatGPT (Illustration PNG - Optionnel)

```
Crée une illustration PNG 1080x1080px de l'architecture Docker SquidResearch.

STYLE :
- Moderne, épuré, data-driven
- Charte BOGOSS : gradients violets/bleus
- 9 conteneurs Docker stylisés avec icônes
- Réseau de connexions élégant
- Fond transparent ou dégradé subtil

CONTENU :
- 9 services : PostgreSQL, Django, React, Celery Worker, Celery Beat, n8n, Flowise, Redis, Tor
- Réseau squidresearch_network connectant tout
- Flèches de dépendances
- Design professionnel, effet "whaou"

Format : PNG 1080x1080px, 300 DPI, fond transparent
```

---

## 🎠 Slide 2 : Problèmes enrichissement B2B

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée illustrant les problèmes de l'enrichissement B2B non orchestré.

CONTEXTE :
- Format : 1080x1080px carousel LinkedIn
- Charte BOGOSS avec accents rouges/orange pour les problèmes

CONTENU À CRÉER :
1. **Infographie SVG** :
   - 4 problèmes visuels en grille 2x2 :
     * Données dispersées (fichiers éparpillés, flèches chaotiques)
     * Sources multiples (icônes non connectées)
     * Requêtes lentes (graphique performance vers le bas)
     * Pas de cache (icône cache barrée, symboles répétition)
   - Design : Cartes avec bordures rouges/orange, icônes X rouges

2. **Animations CSS** :
   - Apparition des problèmes avec shake effect (problème = mouvement)
   - Graphique de performance qui descend progressivement
   - Icônes qui "clignotent" pour montrer l'instabilité
   - Flèches chaotiques qui bougent de manière erratique

3. **Effets visuels** :
   - Contraste : fond clair, éléments problématiques en rouge/orange
   - Badges "❌" animés (rotation subtile)
   - Ombres rouges pour renforcer l'aspect négatif

INTÉGRATION :
- HTML complet avec SVG inline
- Animations CSS performantes
- Effet "chaos" contrôlé pour montrer les problèmes

RÉSULTAT : HTML avec infographie animée montrant les problèmes B2B
```

---

## 🎠 Slide 3 : Module Enriched Solution

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée du module Enriched comme solution orchestrée.

CONTEXTE :
- Format : 1080x1080px carousel LinkedIn
- Charte BOGOSS : gradients violets/roses pour la solution

CONTENU À CRÉER :
1. **Infographie SVG** :
   - Hub central "Enriched" (cercle avec engrenage/cercles concentriques)
   - 4 capacités autour du hub :
     * Groupement par domaine (bleu)
     * Cache partagé (vert)
     * Rate limiting (orange)
     * Ordre optimal (cyan)
   - 4 sources d'enrichissement connectées :
     * INSEE Sirene (API gratuite)
     * Pappers (API documentée)
     * Société.com (Scraper)
     * DNS/WHOIS (Outils Python)
   - Lignes de connexion harmonieuses du hub vers les sources

2. **Animations CSS** :
   - Hub central qui pulse (scale animation)
   - Rayons qui partent du hub vers les capacités (stroke-dasharray)
   - Capacités qui apparaissent en séquence (fade-in + slide)
   - Sources qui se connectent progressivement au hub
   - Flèches de données qui "coulent" vers le hub

3. **Effets visuels** :
   - Gradient animé sur le hub
   - Ombres portées qui pulsent
   - Badges verts pour succès
   - Design harmonieux montrant l'orchestration

INTÉGRATION :
- HTML avec SVG inline
- Animations fluides montrant l'orchestration
- Effet "hub intelligent" avec connexions dynamiques

RÉSULTAT : HTML avec infographie animée du module Enriched
```

---

## 🎠 Slide 4 : Principes de fonctionnement détaillés

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée des 4 principes de fonctionnement du Module Enriched.

CONTEXTE :
- Format : 1080x1080px carousel LinkedIn
- Charte BOGOSS : 4 couleurs différentes pour chaque principe

CONTENU À CRÉER :
1. **Infographie SVG** :
   - Grille 2x2 avec 4 principes :
     * Groupement par domaine (haut-gauche, bleu) : 100 entreprises → 20 domaines
     * Cache partagé Redis (haut-droite, vert) : Flux cache check → hit/miss
     * Cascade intelligente (bas-gauche, violet) : INSEE → Pappers → Registrar
     * Rate limiting humanisé (bas-droite, orange) : Timeline avec délais 5-8s

2. **Animations CSS** :
   - Apparition séquentielle des 4 principes (1 → 2 → 3 → 4)
   - Graphique comparatif "Avant/Après" animé (100 requêtes → 20 requêtes)
   - Flux cache qui s'anime (requête → check → hit/miss)
   - Cascade qui se remplit progressivement (INSEE → Pappers → Registrar)
   - Timeline rate limiting avec barres qui se remplissent

3. **Effets visuels** :
   - Badges métriques animés ("80% réduction", "TTL 24h", etc.)
   - Graphiques de performance avec animations
   - Flèches pointillées pour cascade
   - Timeline interactive

INTÉGRATION :
- HTML avec SVG inline
- Graphiques animés avec données réelles
- Effet data-driven avec métriques visuelles

RÉSULTAT : HTML avec infographie animée des 4 principes
```

---

## 🎠 Slide 5 : Services Docker détaillés

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée des services Docker détaillés.

CONTEXTE :
- Format : 1080x1080px carousel LinkedIn
- Charte BOGOSS : 3 colonnes (Data, Application, Tools)

CONTENU À CRÉER :
1. **Infographie SVG** :
   - Layout 3 colonnes verticales :
     * Colonne 1 (Data Layer, bleu) : PostgreSQL, Redis
     * Colonne 2 (Application Layer, vert) : Django, Celery Worker, Celery Beat
     * Colonne 3 (Frontend & Tools, violet) : React, n8n, Flowise
   - Services représentés comme des cartes empilées
   - Connexions visuelles entre services (flèches pointillées)
   - ⚠️ PAS de ports affichés (sécurité)

2. **Animations CSS** :
   - Apparition colonne par colonne (Data → App → Tools)
   - Services qui apparaissent en cascade dans chaque colonne
   - Connexions qui s'animent progressivement
   - Hover effects sur chaque service (scale + shadow)
   - Badges de catégorie qui pulsent

3. **Effets visuels** :
   - Ombres portées par colonne
   - Icônes modernes pour chaque service
   - Design épuré et professionnel
   - Hiérarchie visuelle claire

INTÉGRATION :
- HTML avec SVG inline
- Animations séquentielles par colonne
- Design technique mais accessible

RÉSULTAT : HTML avec infographie animée des services Docker
```

---

## 🎠 Slide 6 : Flux de données Enriched

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée du flux de données du module Enriched.

CONTEXTE :
- Format : 1080x1080px carousel LinkedIn
- Charte BOGOSS : Pipeline horizontal de gauche à droite

CONTENU À CRÉER :
1. **Infographie SVG** :
   - Pipeline horizontal 5 étapes :
     1. INPUT (gauche, bleu) : Icônes entreprise/email/domaine
     2. ORCHESTRATEUR (centre-gauche, violet) : Hub avec cache
     3. ENRICHISSEMENT (centre, vert) : 4 sources en parallèle (INSEE, Pappers, Société.com, DNS/WHOIS)
     4. CONSOLIDATION (centre-droite, orange) : Fusion/merge
     5. OUTPUT (droite, cyan) : JSON enrichi
   - Flèches grosses et élégantes entre chaque étape
   - Métrique "Avec Tor : 5-8s/req" en badge

2. **Animations CSS** :
   - Flux de données qui "coule" de gauche à droite (particles animation)
   - Chaque étape qui s'illumine séquentiellement
   - Sources d'enrichissement qui s'activent en parallèle (simultanément)
   - Flèches qui pulsent pour montrer le flux
   - Badge métrique qui apparaît à la fin

3. **Effets visuels** :
   - Pipeline visuel avec largeurs variables selon importance
   - Particules animées pour montrer le flux
   - Badges de temps/performance
   - Design fluide et dynamique

INTÉGRATION :
- HTML avec SVG inline + Canvas pour particules (optionnel)
- Animation de flux continue
- Effet "données qui circulent"

RÉSULTAT : HTML avec pipeline animé du flux de données
```

---

## 🎠 Slide 7 : Réseaux, APIs & Webhooks

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée des structures réseau Docker et APIs/webhooks.

CONTEXTE :
- Format : 1080x1080px carousel LinkedIn
- Charte BOGOSS : Schéma réseau professionnel

CONTENU À CRÉER :
1. **Infographie SVG** :
   - Réseau central squidresearch_network (nuage/container réseau)
   - 3 zones connectées :
     * Zone Web (bleue) : Django, React
     * Zone Data (verte) : PostgreSQL, Redis
     * Zone Automation (violette) : n8n, Flowise, Celery
   - Types de connexions :
     * API REST : flèches bleues (/api/enriched/, /companies/search/)
     * Redis Pub/Sub : flèches orange
     * Database : flèches vertes
   - Badge "Réseau isolé" avec icône cadenas

2. **Animations CSS** :
   - Réseau central qui pulse (scale animation)
   - Zones qui apparaissent progressivement
   - Connexions qui s'animent (stroke-dasharray)
   - Flèches qui montrent le flux de données
   - Badge sécurité qui clignote doucement
   - Endpoints API qui apparaissent au hover

3. **Effets visuels** :
   - Zones colorées avec transparence
   - Légende interactive
   - Design schéma réseau professionnel
   - Effet "réseau vivant"

INTÉGRATION :
- HTML avec SVG inline
- Animations de connexions réseau
- Design technique et sécurisé

RÉSULTAT : HTML avec schéma réseau animé
```

---

## 🎠 Slide 8 : Volumes & Mappages Docker

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée des volumes et mappages Docker.

CONTEXTE :
- Format : 1080x1080px carousel LinkedIn
- Charte BOGOSS : 2 sections (Volumes persistants + Bind mounts)

CONTENU À CRÉER :
1. **Infographie SVG** :
   - Layout 2 sections :
     * Section 1 (gauche) : 4 volumes persistants (disques/containers stylisés)
       - postgres_data (bleu)
       - redis_data (rouge)
       - n8n_data (violet)
       - flowise_data (rose)
     * Section 2 (droite) : 3 bind mounts (liens)
       - Code source → Hot reload
       - Logs → Monitoring
       - Config → Paramètres
   - Flèches pointillées des services vers leurs volumes
   - Badges "Survit aux redémarrages" et "Synchronisation temps réel"

2. **Animations CSS** :
   - Volumes qui apparaissent en séquence
   - Flèches qui se dessinent progressivement
   - Disques qui "pulsent" pour montrer la persistance
   - Bind mounts qui "clignotent" pour montrer la synchronisation
   - Badges qui apparaissent avec fade-in

3. **Effets visuels** :
   - Disques/volumes stylisés avec ombres
   - Flèches pointillées animées
   - Badges de persistance
   - Design technique et clair

INTÉGRATION :
- HTML avec SVG inline
- Animations montrant la persistance
- Effet "données qui survivent"

RÉSULTAT : HTML avec infographie animée des volumes Docker
```

---

## 🎠 Slide 9 : Résultats & CTA

### Prompt Claude (Animations + Infographie SVG)

```
Crée une infographie animée de résultats et CTA avec métriques réelles.

CONTEXTE :
- Format : 1080x1080px carousel LinkedIn
- Charte BOGOSS : Dashboard style avec métriques

CONTENU À CRÉER :
1. **Infographie SVG** :
   - Grille 2x2 avec 4 métriques :
     * Cache hit : < 0.1s (vert, graphique barre)
     * Avec Tor : 5-8s (orange, timeline)
     * Sources : APIs officielles (violet, icônes)
     * Gain cache : 98x (cyan, graphique croissance)
   - Box d'avertissement "Performance réelle" (orange)
   - Bouton CTA "Découvrir l'architecture" (gradient violet/rose)

2. **Animations CSS** :
   - Métriques qui apparaissent séquentiellement
   - Graphiques qui se remplissent progressivement
   - Badges qui pulsent
   - Box d'avertissement qui apparaît avec slide-in
   - Bouton CTA avec hover effect (scale + shadow)
   - Graphiques animés (barres, timeline, croissance)

3. **Effets visuels** :
   - Cartes métriques modernes
   - Graphiques stylisés animés
   - Badges de performance
   - Design dashboard professionnel
   - CTA impactant

INTÉGRATION :
- HTML avec SVG inline
- Animations de graphiques
- Effet dashboard data-driven

RÉSULTAT : HTML avec dashboard animé et CTA
```

---

## 📝 Checklist d'intégration

### Pour chaque slide HTML généré par Claude :

- [ ] Format exact : 1080x1080px (viewport fixe)
- [ ] Charte BOGOSS respectée (couleurs, gradients)
- [ ] Animations CSS performantes (60fps, pas de lag)
- [ ] SVG inline (pas d'images externes)
- [ ] Pas de dépendances externes (tout dans un fichier)
- [ ] Responsive au format carré
- [ ] Métriques réelles uniquement (pas inventées)
- [ ] Pas de ports Docker affichés (sécurité)
- [ ] Sources réelles (INSEE, Pappers, Société.com, DNS/WHOIS)
- [ ] Performance optimisée (will-change, transform, opacity)

### Pour les illustrations PNG (ChatGPT) :

- [ ] Format : PNG 1080x1080px, 300 DPI
- [ ] Fond transparent ou blanc selon besoin
- [ ] Charte BOGOSS respectée
- [ ] Style moderne, épuré, data-driven
- [ ] Pas de ports Docker
- [ ] Sources réelles uniquement

---

## 🎯 Priorités

1. **Slide 1** : Architecture Docker (priorité haute - slide d'accroche)
2. **Slide 3** : Module Enriched (priorité haute - solution clé)
3. **Slide 6** : Flux de données (priorité moyenne - technique)
4. **Slide 9** : Résultats & CTA (priorité haute - conversion)
5. Autres slides : Priorité normale

---

## 📊 Références techniques

- **Charte BOGOSS** : `#6366f1`, `#ec4899`, `#10b981`, `#06b6d4`
- **Gradient** : `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Format** : 1080x1080px (carré LinkedIn carousel)
- **Performance** : Animations CSS uniquement (pas de JS lourd)
- **Métriques réelles** : Voir `AVERTISSEMENT_METRIQUES.md`

