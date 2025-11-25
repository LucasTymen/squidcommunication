# 🎨 Prompts Infographies - Épisode 2

> Instructions complètes pour Claude pour créer les 9 infographies de l'épisode 2

## 📋 Charte graphique BOGOSS (à appliquer à toutes les infographies)

### Couleurs principales
- **Primary** : `#6366f1` (violet)
- **Secondary** : `#ec4899` (rose)
- **Success** : `#10b981` (vert)
- **Warning** : `#f59e0b` (orange)
- **Danger** : `#ef4444` (rouge)
- **Accent** : `#06b6d4` (cyan)

### Gradient principal
```css
linear-gradient(135deg, #667eea 0%, #764ba2 100%)
```

### Style général
- Moderne, épuré, professionnel
- Ombres douces : `0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)`
- Rayons arrondis : `12px` pour cartes, `1rem` pour éléments
- Typographie : Bold, moderne, hiérarchie claire
- Format : PNG 1080x1080px, 300 DPI
- Fond : Blanc ou gris très clair (#f8fafc)

---

## 🖼️ Slide 1 : Architecture Docker Overview

**Fichier à créer** : `assets/sanitized/post-01-slide-01-architecture-overview.png`

**Prompt pour Claude :**

```
Crée une infographie moderne de l'architecture Docker SquidResearch dans la charte BOGOSS.

STYLE BOGOSS :
- Couleurs : #6366f1 (primary violet), #ec4899 (secondary rose), #10b981 (success vert), #06b6d4 (accent cyan)
- Gradient principal : linear-gradient(135deg, #667eea 0%, #764ba2 100%)
- Style : moderne, épuré, avec ombres douces et rayons arrondis
- Typographie : bold, moderne, hiérarchie claire

CONTENU :
- Titre : "SquidResearch - Architecture Docker" (grand, gradient violet, en haut)
- 9 services représentés comme des conteneurs Docker stylisés :
  1. PostgreSQL (db) - icône base de données, couleur bleu (#3b82f6)
  2. Django (web) - icône Python/Django, couleur vert (#10b981)
  3. React (frontend) - icône React, couleur cyan (#06b6d4)
  4. Celery Worker - icône tâches, couleur orange (#f59e0b)
  5. Celery Beat - icône horloge, couleur orange clair (#fbbf24)
  6. n8n - icône automation, couleur violet (#6366f1)
  7. Flowise - icône IA, couleur rose (#ec4899)
  8. Redis - icône cache, couleur rouge (#ef4444)
  9. Tor - icône anonymat, couleur gris foncé (#64748b)
- ⚠️ SÉCURITÉ : Ne PAS afficher les numéros de ports (sécurité)
- Réseau Docker : représenter le réseau squidresearch_network comme un nuage/container réseau connectant tous les services
- Flèches montrant les dépendances :
  - db → web (flèche verte)
  - redis → worker (flèche orange)
  - web → frontend (flèche bleue)
  - db → worker (flèche verte)
- Design : cartes avec ombres, badges colorés pour chaque service
- ⚠️ SÉCURITÉ : Ne PAS afficher les ports (sécurité réseau)
- Layout : services organisés en 3 colonnes (Data, Application, Frontend/Tools)
- Format : 1080x1080px (carré), fond blanc/gris très clair (#f8fafc)
- Éléments décoratifs : lignes de connexion élégantes, icônes modernes, effet de profondeur
- ⚠️ IMPORTANT : Ne PAS inventer de métriques (pas de "2M entreprises", pas de "500 req/min"). Utiliser uniquement l'architecture réelle.

RÉSULTAT ATTENDU : Infographie professionnelle, basée sur la réalité technique, effet "whaou", claire et impactante
```

---

## 🖼️ Slide 2 : Problèmes enrichissement B2B

**Fichier à créer** : `assets/sanitized/post-01-slide-02-probleme.png`

**Prompt pour Claude :**

```
Crée une infographie illustrant les problèmes de l'enrichissement B2B non orchestré (charte BOGOSS).

STYLE BOGOSS : Même charte que slide 1

CONTENU :
- Titre : "Le défi de l'enrichissement B2B" (rouge/orange pour problème, #ef4444 ou #f59e0b)
- 4 problèmes visuels organisés en grille 2x2 :
  1. "Données dispersées" - icône fichiers éparpillés, flèches chaotiques, couleur rouge (#ef4444)
  2. "Sources multiples non synchronisées" - icônes multiples (LinkedIn, emails, domaines) non connectées, couleur orange (#f59e0b)
  3. "Requêtes lentes et coûteuses" - graphique de performance avec flèche vers le bas, couleur rouge foncé (#dc2626)
  4. "Pas de cache partagé" - icône cache barrée, symboles de répétition, couleur orange foncé (#d97706)
- Design : cartes avec bordures rouges/orange, icônes X rouges, fond légèrement rougeâtre pour ambiance problème
- Contraste : fond clair (#fef2f2), éléments problématiques en rouge/orange
- Format : 1080x1080px
- Éléments : flèches chaotiques, symboles d'erreur, graphiques de performance négative

RÉSULTAT : Visualisation claire des problèmes, prépare la solution, impact visuel fort
```

---

## 🖼️ Slide 3 : Module Enriched Solution

**Fichier à créer** : `assets/sanitized/post-01-slide-03-module-enriched.png`

**Prompt pour Claude :**

```
Crée une infographie du module Enriched comme solution orchestrée (charte BOGOSS).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Module Enriched - Orchestration Intelligente" (gradient violet/rose en haut)
- Centre : Module Enriched représenté comme un hub central (icône engrenage/cercles concentriques, gradient violet #6366f1)
- 4 capacités autour du hub (positionnées aux 4 coins) :
  1. "Groupement par domaine" - icône domaines groupés, couleur bleu (#3b82f6), badge vert
  2. "Cache partagé automatique" - icône cache avec flèches, couleur vert (#10b981), badge vert
  3. "Rate limiting global" - icône limiteur/contrôleur, couleur orange (#f59e0b), badge orange
  4. "Ordre optimal d'exécution" - icône séquence/chronomètre, couleur cyan (#06b6d4), badge cyan
- Sources d'enrichissement connectées au hub (autour du centre) :
  - Email Enriched (icône email, couleur bleu)
  - Domain Enriched (icône globe, couleur vert)
  - Company Enriched (icône entreprise, couleur violet)
  - Social Media Enriched (icône réseaux sociaux, couleur rose)
  - Intelligence Tools (icône IA, couleur cyan)
- Design : hub central avec rayons vers les sources, tout connecté harmonieusement, flèches élégantes
- Couleurs : verts pour succès, gradients pour modernité, fond clair (#f0fdf4)
- Format : 1080x1080px
- Éléments : connexions visuelles claires, badges de performance, effet de centralisation

RÉSULTAT : Visualisation claire de la solution orchestrée, hub central impactant, connexions harmonieuses
```

---

## 🖼️ Slide 4 : Principes de fonctionnement détaillés

**Fichier à créer** : `assets/sanitized/post-01-slide-04-principes-fonctionnement.png`

**Prompt pour Claude :**

```
Crée une infographie détaillée des principes de fonctionnement du Module Enriched (charte BOGOSS, style data-driven).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Principes de fonctionnement - Module Enriched" (gradient en haut)
- 4 principes organisés en grille 2x2 :

1. GROUPEMENT PAR DOMAINE (haut-gauche) :
   - Visualisation : 100 entreprises → 20 domaines uniques
   - Graphique : Avant (100 requêtes) vs Après (20 requêtes)
   - Gain : "80% réduction requêtes" (badge vert #10b981)
   - Icône : domaines groupés, couleur bleu (#3b82f6)
   - Exemple visuel : 100 boîtes → 20 boîtes groupées

2. CACHE PARTAGÉ REDIS (haut-droite) :
   - Visualisation : Flux "Requête → Cache check → Hit/Miss"
   - Métrique : "Cache hit : < 0.1s" (badge vert #10b981)
   - Métrique : "TTL 24h" (badge cyan #06b6d4)
   - Icône : cache Redis, couleur vert (#10b981)
   - Flux : Requête → Cache Redis → Hit (retour) / Miss (scraper)

3. CASCADE INTELLIGENTE (bas-gauche) :
   - Visualisation : Flux vertical INSEE → Pappers → Registrar
   - Données complémentaires : INSEE (SIREN) → Pappers (financier) → Registrar (domaine)
   - Flèches pointillées montrant la cascade
   - Icônes : INSEE (gouvernement), Pappers (entreprise), Registrar (domaine)
   - Couleur : violet (#6366f1)
   - Exemple : "INSEE trouve SIREN → Pappers enrichit → Registrar fallback si échec"

4. RATE LIMITING HUMANISÉ (bas-droite) :
   - Visualisation : Timeline avec délais 5-8s entre requêtes
   - Métrique : "Max 10-12 req/min" (badge orange #f59e0b)
   - Protection : "Anti-ban activé" (badge rouge #ef4444)
   - Icône : limiteur/contrôleur, couleur orange (#f59e0b)
   - Timeline : Requête 1 → 6.5s → Requête 2 → 6.5s → Requête 3

- Design : grille 2x2 avec cartes, flèches pointillées pour cascade, graphiques de performance
- Format : 1080x1080px
- Éléments data-driven : graphiques comparatifs, badges métriques, timeline
- ⚠️ IMPORTANT : Utiliser métriques réelles (5-8s, 10-12 req/min, cache hit < 0.1s)

RÉSULTAT : Visualisation claire des 4 principes avec métriques réelles, graphiques comparatifs, effet "whaou"
```

---

## 🖼️ Slide 5 : Services Docker détaillés

**Fichier à créer** : `assets/sanitized/post-01-slide-05-services-detaille.png`

**Prompt pour Claude :**

```
Crée une infographie détaillée des services Docker avec leurs rôles et connexions (charte BOGOSS).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Architecture Docker - Services détaillés" (gradient en haut)
- Layout : 3 colonnes verticales bien définies
  Colonne 1 (Data Layer - Gauche) :
    - PostgreSQL (db) - icône DB, couleur bleu (#3b82f6)
    - Redis (cache) - icône cache, couleur rouge (#ef4444)
    - Badge "Data Layer" en haut de la colonne
  Colonne 2 (Application Layer - Centre) :
    - Django (web) - icône Python, couleur vert (#10b981)
    - Celery Worker - icône worker, couleur orange (#f59e0b)
    - Celery Beat - icône scheduler, couleur orange clair (#fbbf24)
    - Badge "Application Layer" en haut de la colonne
  Colonne 3 (Frontend & Tools - Droite) :
    - React (frontend) - icône React, couleur cyan (#06b6d4)
    - React Native (mobile) - icône mobile, couleur cyan clair (#22d3ee)
    - n8n (automation) - icône workflow, couleur violet (#6366f1)
    - Flowise (IA) - icône chatbot, couleur rose (#ec4899)
    - Badge "Frontend & Tools" en haut de la colonne
- ⚠️ SÉCURITÉ : Ne PAS afficher les ports (sécurité réseau)
- Réseau : représenter squidresearch_network comme un nuage/container réseau en bas connectant tous les services
- Flèches de dépendances :
  - db → web (flèche verte épaisse)
  - redis → worker (flèche orange)
  - web → frontend (flèche bleue)
  - db → worker (flèche verte fine)
- ⚠️ SÉCURITÉ : Ne PAS afficher les ports
- Design : cartes empilées par colonne, connexions visuelles claires, légende en bas
- Format : 1080x1080px
- Éléments : séparation visuelle claire entre colonnes, flèches directionnelles
- ⚠️ SÉCURITÉ : Ne PAS afficher les ports (sécurité réseau)

RÉSULTAT : Vue d'ensemble technique claire et professionnelle, organisation logique, facile à comprendre
```

---

## 🖼️ Slide 6 : Flux de données Enriched

**Fichier à créer** : `assets/sanitized/post-01-slide-06-flux-donnees.png`

**Prompt pour Claude :**

```
Crée une infographie DÉTAILLÉE du flux de données du module Enriched (charte BOGOSS, style data-driven avec schémas dynamiques).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Flux de données Enriched - Pipeline détaillé" (gradient en haut)
- Flux horizontal de gauche à droite avec flèches pointillées animées (suggestion visuelle) :
  1. INPUT (gauche) : 
     - Icônes entreprise/email/domaine dans une carte bleue (#3b82f6)
     - Texte "Input : Entreprise/Email/Domaine"
     - Badge "1️⃣"
     - Détail : "Validation & normalisation"
  2. ORCHESTRATEUR (centre-gauche) : 
     - Hub avec cache représenté comme engrenage violet (#6366f1)
     - Texte "Orchestrateur : Groupement & Cache Redis"
     - Badge "2️⃣"
     - Détails techniques :
       * "Vérification cache Redis"
       * "Groupement par domaine"
       * "Planification requêtes"
     - Métrique : "Cache hit : < 0.1s" (si hit)
  3. ENRICHISSEMENT (centre) : 
     - Sources RÉELLES avec APIs documentées (icônes alignées verticalement) :
       * INSEE Sirene (API officielle, gratuite) - icône gouvernement, bleu
       * Pappers (API officielle, doc: pappers.fr/api) - icône entreprise, vert
       * Société.com (scraper) - icône web, violet
       * DNS/WHOIS (outils Python) - icône réseau, cyan
     - Texte "Enrichissement : Sources avec APIs officielles"
     - Badge "3️⃣"
     - Détails techniques :
       * "INSEE → Pappers → Registrar (cascade)"
       * "Rate limiting : 5-8s entre requêtes"
       * "Tor + humanisation activés"
     - Métrique : "Avec Tor : 5-8s/requête, max 10-12 req/min"
  4. CONSOLIDATION (centre-droite) : 
     - Fusion/merge représenté comme cercle orange (#f59e0b)
     - Texte "Consolidation : Fusion intelligente"
     - Badge "4️⃣"
     - Détails techniques :
       * "Résolution conflits"
       * "Priorisation sources (INSEE > Pappers > Registrar)"
       * "Scoring de confiance"
  5. OUTPUT (droite) : 
     - JSON enrichi représenté comme document cyan (#06b6d4)
     - Texte "Output : Données enrichies JSON"
     - Badge "5️⃣"
     - Détails techniques :
       * "Format UnifiedEnrichmentResult"
       * "Cache mis à jour (TTL 24h)"
       * "Prêt pour consommation API"
- Flèches entre chaque étape (grosses, élégantes, gradient) avec animation pointillée suggérée (style CSS animation)
- Métriques RÉELLES avec contexte :
  - "Cache hit : < 0.1s" (badge vert #10b981) - seulement si cache hit
  - "Avec Tor + humanisation : 5-8s entre requêtes" (badge orange #f59e0b) - réalité production
  - "Max 10-12 req/min" (badge violet #6366f1) - rate limiting réel
- Design : pipeline visuel horizontal, largeurs variables selon importance, progression claire
- Éléments data-driven : petits graphiques de performance, badges de temps avec contexte
- Format : 1080x1080px
- Fond : dégradé subtil de gauche (bleu clair) à droite (cyan clair)
- ⚠️ CRITIQUE : Performance réelle = lent avec Tor/humanisation (5-8s), rapide seulement avec cache hit

RÉSULTAT : Visualisation claire du pipeline d'enrichissement, progression évidente, métriques réelles avec contexte (Tor/humanisation), sources réelles avec APIs documentées
```

---

## 🖼️ Slide 7 : Réseaux et mappages

**Fichier à créer** : `assets/sanitized/post-01-slide-07-reseaux-mappages.png`

**Prompt pour Claude :**

```
Crée une infographie DÉTAILLÉE des structures réseau Docker, APIs et webhooks (charte BOGOSS, schémas dynamiques avec flèches pointillées).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Réseaux, APIs & Webhooks - Architecture détaillée" (gradient en haut)
- Réseau central : squidresearch_network représenté comme un nuage/container réseau au centre (grand cercle avec gradient violet/rose)
- Services connectés au réseau (organisés autour du réseau central) :
  - Services web (zone bleue, en haut) :
    * web (Django) - icône Python
      - API REST : /api/enriched/, /companies/search/, /api/n8n/
      - Webhooks : /webhooks/
    * frontend (React) - icône React
      - Communication : HTTP vers Django API
    * mobile (React Native) - icône mobile
      - Communication : HTTP vers Django API
  - Services data (zone verte, en bas-gauche) :
    * db (PostgreSQL) - icône DB
      - Connexion : Django ORM, Celery workers
    * redis - icône cache
      - Usage : Cache enrichissement, Queue Celery, Pub/Sub
  - Services automation (zone violette, en bas-droite) :
    * n8n - icône workflow
      - Webhooks : /api/n8n/webhooks/
      - API : /api/n8n/workflows/
    * flowise - icône IA
      - Communication : API REST interne
    * worker (Celery) - icône worker
      - Queue : Redis (tasks async)
    * beat (Celery Beat) - icône scheduler
      - Schedule : Redis (cron jobs)
- Types de connexions DÉTAILLÉES (légende en bas avec exemples) :
  - API REST : flèches bleues (#3b82f6) pointillées
    * Exemples : POST /api/enriched/company/, GET /companies/search/
  - Redis Pub/Sub : flèches orange (#f59e0b) pointillées
    * Exemples : Celery tasks, cache notifications
  - Database : flèches vertes (#10b981) pointillées
    * Exemples : Django ORM queries, migrations
  - Webhooks : flèches roses (#ec4899) pointillées
    * Exemples : /webhooks/, /api/n8n/webhooks/
- Volumes Docker : représenter les volumes persistants (postgres_data, redis_data, n8n_data, flowise_data) comme disques en bas avec labels
- Sécurité : badge "Réseau isolé" avec icône cadenas (#10b981) en haut-droite
- Design : schéma réseau professionnel avec flèches pointillées animées (suggestion visuelle), zones colorées, connexions détaillées, légende complète avec exemples d'endpoints
- Format : 1080x1080px
- Éléments : flèches directionnelles pointillées (style animation), zones colorées, badges de sécurité, icônes de volumes, exemples d'endpoints réels
- ⚠️ SÉCURITÉ : Ne PAS afficher les ports, seulement les chemins d'APIs

RÉSULTAT : Visualisation technique détaillée des structures réseau avec APIs et webhooks réels, organisation claire, sécurité mise en avant
```

---

## 🖼️ Slide 8 : Volumes & Mappages Docker

**Fichier à créer** : `assets/sanitized/post-01-slide-08-volumes-mappages.png`

**Prompt pour Claude :**

```
Crée une infographie des volumes et mappages Docker (charte BOGOSS, style technique).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Volumes & Mappages Docker - Persistance" (gradient en haut)
- Layout : 2 sections principales

SECTION 1 - VOLUMES PERSISTANTS (gauche) :
  - 4 volumes représentés comme disques/containers stylisés :
    1. postgres_data - icône DB, couleur bleu (#3b82f6)
       - Label : "Données PostgreSQL"
       - Taille : "Persistant"
       - Flèche pointillée depuis service "db"
    2. redis_data - icône cache, couleur rouge (#ef4444)
       - Label : "Cache Redis"
       - Taille : "Persistant"
       - Flèche pointillée depuis service "redis"
    3. n8n_data - icône workflow, couleur violet (#6366f1)
       - Label : "Workflows n8n"
       - Taille : "Persistant"
       - Flèche pointillée depuis service "n8n"
    4. flowise_data - icône IA, couleur rose (#ec4899)
       - Label : "Modèles Flowise"
       - Taille : "Persistant"
       - Flèche pointillée depuis service "flowise"
  - Flèches pointillées des services vers leurs volumes (style animation suggérée)
  - Badge "Survit aux redémarrages" (vert #10b981) en haut de la section

SECTION 2 - BIND MOUNTS (droite) :
  - 3 mappages représentés comme liens stylisés :
    1. Code source → Hot reload dev
       - Icône : fichiers code, couleur cyan (#06b6d4)
       - Flèche bidirectionnelle pointillée
       - Label : "Synchronisation temps réel"
    2. Logs → Monitoring
       - Icône : fichiers logs, couleur orange (#f59e0b)
       - Flèche pointillée vers dossier logs
       - Label : "Monitoring continu"
    3. Config → Paramètres services
       - Icône : fichiers config, couleur vert (#10b981)
       - Flèche pointillée vers services
       - Label : "Configuration centralisée"
  - Badge "Synchronisation temps réel" (cyan #06b6d4) en haut de la section

- Design : disques/volumes stylisés avec ombres, flèches pointillées, badges de persistance
- Format : 1080x1080px
- Éléments : icônes volumes, flèches mappages, badges sécurité, séparation visuelle claire entre sections
- Légende en bas : "Volumes = Persistance | Bind mounts = Synchronisation"

RÉSULTAT : Visualisation claire de la persistance et des mappages Docker, organisation technique professionnelle
```

---

## 🖼️ Slide 9 : Résultats & CTA

**Fichier à créer** : `assets/sanitized/post-01-slide-09-resultats-cta.png`

**Prompt pour Claude :**

```
Crée une infographie de résultats et CTA (charte BOGOSS, style data-driven).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Performance & Résultats" (gradient violet/rose en haut)
- 4 métriques visuelles RÉELLES avec contexte (style dashboard moderne, organisées en grille 2x2) :
  1. "Cache hit : < 0.1s" 
     - Graphique barre horizontal vert (#10b981)
     - Icône chronomètre
     - Badge "⚡"
     - Texte "Temps mesuré (benchmark réel)"
     - Sous-texte : "Seulement si cache hit"
  2. "Avec Tor : 5-8s/requête" 
     - Graphique barre horizontal orange (#f59e0b)
     - Icône Tor + horloge
     - Badge "🛡️"
     - Texte "Performance réelle (Tor + humanisation)"
     - Sous-texte : "Max 10-12 req/min (rate limiting)"
  3. "Import CSV : 100%" 
     - Graphique pie chart vert (#10b981), 100% rempli
     - Icône fichier CSV avec checkmark
     - Badge "🔄"
     - Texte "Succès import (145 créés, 0 ignorés)"
     - Sous-texte : "🆕 Détection auto colonnes (IntelligentMapper)"
  4. "Gain cache : 98x" 
     - Graphique comparatif avant/après, couleur cyan (#06b6d4)
     - Icône cache avec flèche montante
     - Badge "📊"
     - Texte "Plus rapide (benchmark réel)"
     - Sous-texte : "Scénario : 100 contacts même entreprise"
- Design : cartes métriques modernes avec ombres, graphiques stylisés, badges colorés
- CTA : Bouton "Découvrir l'architecture" (gradient violet/rose, en bas, grand et visible)
- Éléments : badges de performance, icônes modernes, graphiques basés sur benchmarks réels
- Format : 1080x1080px
- Fond : dégradé subtil (#f8fafc vers blanc)
- ⚠️ CRITIQUE : Utiliser UNIQUEMENT les métriques réelles mesurées dans les benchmarks (docs/archive/2025-10/BENCHMARK_RESULTS.md). AUCUN chiffre inventé.
- 🆕 **Import CSV** : Ajouter métrique "Import CSV : 100%" avec détails refactorisation Nov 2025 (IntelligentMapper, détection auto colonnes)

RÉSULTAT : Slide final impactant avec métriques RÉELLES vérifiables, CTA clair et actionnable, effet "whaou" basé sur la réalité, incluant les dernières améliorations (import CSV intelligent)
```

---

## ✅ Checklist création infographies

Pour chaque infographie :
- [ ] Format : PNG 1080x1080px
- [ ] Résolution : 300 DPI
- [ ] Charte BOGOSS appliquée (couleurs, gradients)
- [ ] Style moderne et professionnel
- [ ] Effet "whaou" recherché
- [ ] Texte lisible et hiérarchie claire
- [ ] Sauvegardé dans `assets/sanitized/`
- [ ] ⚠️ **MÉTRIQUES RÉELLES UNIQUEMENT** : Aucun chiffre inventé

---

## 📝 Notes importantes

- **Cohérence** : Toutes les infographies doivent avoir le même style BOGOSS
- **Lisibilité** : Texte toujours lisible, contrastes respectés
- **Professionnalisme** : Style data-driven, moderne, impactant
- **Terminologie** : Utiliser "Module Enriched", éviter Kali/OSINT
- **⚠️ CRITIQUE - MÉTRIQUES RÉELLES** :
  - ✅ Utiliser : Benchmarks réels (docs/archive/2025-10/BENCHMARK_RESULTS.md)
  - ✅ Utiliser : Architecture réelle (docker-compose.yml)
  - ✅ Utiliser : Sources réellement implémentées (SIREN, Pappers, Société.com)
  - ❌ ÉVITER : Chiffres inventés (2M entreprises, 85% hit rate, 500 req/min)
  - ❌ ÉVITER : APIs non intégrées (Hunter.io, Clearbit)
  - ❌ ÉVITER : Métriques non mesurées en production

## 📊 Métriques réelles vérifiables (à utiliser)

**Benchmarks mesurés** (docs/archive/2025-10/BENCHMARK_RESULTS.md) :
- Cache hit : < 0.1s (mesuré)
- Gain cache : 98x plus rapide (benchmark réel)
- Cache WHOIS : 0.778s → 0.000s (5,703x plus rapide)
- Cache DNS : 2.153s → 0.000s (19,509x plus rapide)
- Enrichissement E2E : 0.057s (cache froid), 0.046s (cache chaud)

**Architecture réelle** :
- 9 services Docker (vérifié dans docker-compose.yml)
- Réseau : squidresearch_network
- Volumes : postgres_data, redis_data, n8n_data, flowise_data

**Sources réellement implémentées** :
- SIREN (find_siren_from_name)
- Pappers (API intégrée)
- Société.com (scraper fonctionnel)
- DNS/WHOIS (outils Python)

---

**Status** : 📋 À créer par Claude

