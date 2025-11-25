# LinkedIn Post - Épisode 2 : Architecture Docker & Module Enriched

> Campagne : `2025-11-episode-2-dockerisation-enriched`  
> Post n°1 - Format Carousel (9 slides)  
> Date publication (prévision) : 2025-11-15 10:00 UTC _(modifiable)_

## 📋 Informations
- **Objectif** : Notoriété technique + Engagement
- **CTA** : Découvrir l'architecture complète
- **Hashtags** : `#SquidResearch #Docker #Architecture #EnrichissementDonnées #B2B #DevOps #DataDriven #TechInnovation`

---

## ✍️ Texte principal du post (visible avant le carousel)

```
🚀 Épisode 2 : L'architecture Docker de SquidResearch dévoilée

Comment orchestrer 9 services Docker pour enrichir des millions de données B2B en temps réel ?

Swipez pour découvrir :
→ Architecture microservices complète
→ Module Enriched : enrichissement intelligent
→ Mappages et flux de données
→ Métriques de performance

#Docker #Architecture #EnrichissementDonnées #B2B
```

---

## 🎠 Structure Carousel (9 slides)

### Slide 1 : Accroche - Architecture Docker
**Texte sur slide :**
```
🐙 SquidResearch
Architecture Docker

9 services orchestrés
PostgreSQL • Django • React • Celery
n8n • Flowise • Redis • Tor • Mobile

Architecture scalable pour enrichissement B2B
```

**Visuel :** `assets/sanitized/post-01-slide-01-architecture-overview.png`

**Prompt Claude pour infographie :**
```
Crée une infographie moderne de l'architecture Docker SquidResearch dans la charte BOGOSS.

STYLE BOGOSS :
- Couleurs : #6366f1 (primary violet), #ec4899 (secondary rose), #10b981 (success vert), #06b6d4 (accent cyan)
- Gradient principal : linear-gradient(135deg, #667eea 0%, #764ba2 100%)
- Style : moderne, épuré, avec ombres douces et rayons arrondis
- Typographie : bold, moderne, hiérarchie claire

CONTENU :
- Titre : "SquidResearch - Architecture Docker" (grand, gradient violet)
- 9 services représentés comme des conteneurs Docker stylisés :
  1. PostgreSQL (db) - icône base de données, couleur bleu
  2. Django (web) - icône Python/Django, couleur vert
  3. React (frontend) - icône React, couleur cyan
  4. Celery Worker - icône tâches, couleur orange
  5. Celery Beat - icône horloge, couleur orange clair
  6. n8n - icône automation, couleur violet
  7. Flowise - icône IA, couleur rose
  8. Redis - icône cache, couleur rouge
  9. Tor - icône anonymat, couleur gris foncé
- Réseau Docker : représenter le réseau squidresearch_network connectant tous les services
- Flèches montrant les dépendances (db → web, redis → worker, etc.)
- Design : cartes avec ombres, badges colorés pour chaque service
- Format : 1080x1080px (carré), fond blanc/gris très clair
- Éléments décoratifs : lignes de connexion élégantes, icônes modernes

RÉSULTAT ATTENDU : Infographie professionnelle, data-driven, effet "whaou"
```

---

### Slide 2 : Problème - Complexité de l'enrichissement
**Texte sur slide :**
```
Le défi de l'enrichissement B2B

❌ Données dispersées
❌ Sources multiples non synchronisées
❌ Requêtes lentes et coûteuses
❌ Pas de cache partagé

→ Besoin d'une solution orchestrée
```

**Visuel :** `assets/sanitized/post-01-slide-02-probleme.png`

**Prompt Claude pour infographie :**
```
Crée une infographie illustrant les problèmes de l'enrichissement B2B non orchestré (charte BOGOSS).

STYLE BOGOSS : Même charte que slide 1

CONTENU :
- Titre : "Le défi de l'enrichissement B2B" (rouge/orange pour problème)
- 4 problèmes visuels :
  1. "Données dispersées" - icône fichiers éparpillés, flèches chaotiques
  2. "Sources multiples" - icônes multiples (LinkedIn, emails, domaines) non connectées
  3. "Requêtes lentes" - graphique de performance avec flèche vers le bas
  4. "Pas de cache" - icône cache barrée, symboles de répétition
- Design : cartes avec bordures rouges/orange, icônes X rouges
- Contraste : fond clair, éléments problématiques en rouge/orange
- Format : 1080x1080px

RÉSULTAT : Visualisation claire des problèmes, prépare la solution
```

---

### Slide 3 : Solution - Module Enriched
**Texte sur slide :**
```
✅ Module Enriched

Orchestration intelligente
• Groupement par domaine
• Cache partagé automatique
• Rate limiting global
• Ordre optimal d'exécution

Enrichissement multi-sources unifié
```

**Visuel :** `assets/sanitized/post-01-slide-03-module-enriched.png`

**Prompt Claude pour infographie :**
```
Crée une infographie du module Enriched comme solution orchestrée (charte BOGOSS).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Module Enriched - Orchestration Intelligente" (gradient violet/rose)
- Centre : Module Enriched représenté comme un hub central (icône engrenage/cercles concentriques)
- 4 capacités autour du hub :
  1. "Groupement par domaine" - icône domaines groupés, couleur bleu
  2. "Cache partagé" - icône cache avec flèches, couleur vert
  3. "Rate limiting" - icône limiteur/contrôleur, couleur orange
  4. "Ordre optimal" - icône séquence/chronomètre, couleur cyan
- Sources d'enrichissement connectées au hub :
  - Email Enriched
  - Domain Enriched
  - Company Enriched
  - Social Media Enriched
  - Intelligence Tools
- Design : hub central avec rayons vers les sources, tout connecté harmonieusement
- Couleurs : verts pour succès, gradients pour modernité
- Format : 1080x1080px

RÉSULTAT : Visualisation claire de la solution orchestrée
```

---

### Slide 4 : Principes de fonctionnement - Module Enriched
**Texte sur slide :**
```
Principes de fonctionnement détaillés

1️⃣ Groupement par domaine
   → 100 entreprises → 20 domaines uniques
   → 1 requête par domaine au lieu de 100

2️⃣ Cache partagé Redis
   → Vérification avant chaque requête
   → TTL 24h, hit rate optimisé
   → Cache hit : < 0.1s

3️⃣ Cascade intelligente
   → INSEE (gratuit) → Pappers (API) → Registrar (fallback)
   → Données complémentaires, pas redondantes

4️⃣ Rate limiting humanisé
   → 5-8s entre requêtes (Tor)
   → Max 10-12 req/min
   → Protection anti-ban
```

**Visuel :** `assets/sanitized/post-01-slide-04-principes-fonctionnement.png`

**Prompt Claude pour infographie :**
```
Crée une infographie détaillée des principes de fonctionnement du Module Enriched (charte BOGOSS, style data-driven).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Principes de fonctionnement - Module Enriched" (gradient)
- 4 principes organisés en grille 2x2 :

1. GROUPEMENT PAR DOMAINE (haut-gauche) :
   - Visualisation : 100 entreprises → 20 domaines uniques
   - Graphique : Avant (100 requêtes) vs Après (20 requêtes)
   - Gain : "80% réduction requêtes" (badge vert)
   - Icône : domaines groupés, couleur bleu (#3b82f6)

2. CACHE PARTAGÉ REDIS (haut-droite) :
   - Visualisation : Flux "Requête → Cache check → Hit/Miss"
   - Métrique : "Cache hit : < 0.1s" (badge vert)
   - Métrique : "TTL 24h" (badge cyan)
   - Icône : cache Redis, couleur vert (#10b981)

3. CASCADE INTELLIGENTE (bas-gauche) :
   - Visualisation : Flux vertical INSEE → Pappers → Registrar
   - Données complémentaires : INSEE (SIREN) → Pappers (financier) → Registrar (domaine)
   - Flèches pointillées montrant la cascade
   - Icônes : INSEE (gouvernement), Pappers (entreprise), Registrar (domaine)
   - Couleur : violet (#6366f1)

4. RATE LIMITING HUMANISÉ (bas-droite) :
   - Visualisation : Timeline avec délais 5-8s entre requêtes
   - Métrique : "Max 10-12 req/min" (badge orange)
   - Protection : "Anti-ban activé" (badge rouge)
   - Icône : limiteur/contrôleur, couleur orange (#f59e0b)

- Design : grille 2x2 avec cartes, flèches pointillées pour cascade, graphiques de performance
- Format : 1080x1080px
- Éléments data-driven : graphiques comparatifs, badges métriques, timeline

RÉSULTAT : Visualisation claire des 4 principes avec métriques réelles
```

---

### Slide 5 : Architecture - Services Docker détaillés
**Texte sur slide :**
```
Architecture Docker détaillée

📊 Base de données : PostgreSQL
⚡ Cache & Queue : Redis
🐍 Backend : Django + Celery
⚛️ Frontend : React
📱 Mobile : React Native
🔄 Automation : n8n
🤖 IA : Flowise

Réseau isolé : squidresearch_network
```

**Visuel :** `assets/sanitized/post-01-slide-05-services-detaille.png`

**Prompt Claude pour infographie :**
```
Crée une infographie détaillée des services Docker avec leurs rôles et connexions (charte BOGOSS).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Architecture Docker - Services détaillés" (gradient)
- Layout : 3 colonnes verticales
  Colonne 1 (Data Layer) :
    - PostgreSQL (db) - icône DB
    - Redis (cache) - icône cache
  Colonne 2 (Application Layer) :
    - Django (web) - icône Python
    - Celery Worker - icône worker
    - Celery Beat - icône scheduler
  Colonne 3 (Frontend & Tools) :
    - React (frontend) - icône React
    - React Native (mobile) - icône mobile
    - n8n (automation) - icône workflow
    - Flowise (IA) - icône chatbot
- ⚠️ SÉCURITÉ : Ne PAS afficher les ports (sécurité réseau)
- Réseau : représenter squidresearch_network comme un nuage connectant tous les services
- Flèches de dépendances : db → web, redis → worker, web → frontend
- ⚠️ SÉCURITÉ : Ne PAS afficher les ports (sécurité réseau)
- Design : cartes empilées, connexions visuelles claires
- Format : 1080x1080px

RÉSULTAT : Vue d'ensemble technique claire et professionnelle
```

---

### Slide 6 : Mappages - Flux de données Enriched
**Texte sur slide :**
```
Flux de données Enriched - Pipeline détaillé

1️⃣ Input : Entreprise/Email/Domaine
   → Validation & normalisation

2️⃣ Orchestrateur : Groupement & Cache Redis
   → Vérification cache, planification requêtes
   → Cache hit : < 0.1s (si hit)

3️⃣ Enrichissement : Sources avec APIs officielles
   → INSEE Sirene (API gratuite)
   → Pappers (API documentée)
   → Société.com (scraper)
   → DNS/WHOIS (outils Python)
   → Avec Tor : 5-8s/requête, max 10-12 req/min

4️⃣ Consolidation : Fusion intelligente
   → Résolution conflits, priorisation sources

5️⃣ Output : Données enrichies JSON
   → Format UnifiedEnrichmentResult
   → Cache mis à jour (TTL 24h)
```

**Visuel :** `assets/sanitized/post-01-slide-06-flux-donnees.png`

**Prompt Claude pour infographie :**
```
Crée une infographie du flux de données du module Enriched (charte BOGOSS, style data-driven).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Flux de données Enriched" (gradient)
- Flux horizontal de gauche à droite :
  1. INPUT (gauche) : Icônes entreprise/email/domaine, couleur bleu
  2. ORCHESTRATEUR (centre-gauche) : Hub avec cache, couleur violet
  3. ENRICHISSEMENT (centre) : 5 sources en parallèle (icônes), couleur vert
  4. CONSOLIDATION (centre-droite) : Fusion/merge, couleur orange
  5. OUTPUT (droite) : JSON enrichi, couleur cyan
- Flèches entre chaque étape (grosses, élégantes)
- Métriques : "Temps moyen : < 5 secondes" en badge vert
- Design : pipeline visuel, largeurs variables selon importance
- Éléments data-driven : petits graphiques de performance, badges de temps
- Format : 1080x1080px

RÉSULTAT : Visualisation claire du pipeline d'enrichissement
```

---

### Slide 7 : Structures - Réseaux, APIs & Webhooks
**Texte sur slide :**
```
Réseaux, APIs & Webhooks - Architecture détaillée

🌐 Réseau Docker : squidresearch_network (isolé)
📡 Connexions détaillées :
   • API REST : /api/enriched/, /companies/search/
   • Webhooks : /webhooks/, /api/n8n/webhooks/
   • Redis Pub/Sub : Celery tasks, cache notifications
   • Database : Django ORM, migrations

🔒 Sécurité : Réseau bridge isolé, pas de ports exposés
📊 Volumes : postgres_data, redis_data, n8n_data, flowise_data
🔄 Services : Django ↔ React ↔ Celery ↔ n8n ↔ Flowise

Isolation + APIs documentées + Webhooks
```

**Visuel :** `assets/sanitized/post-01-slide-07-reseaux-mappages.png`

**Prompt Claude pour infographie :**
```
Crée une infographie des structures réseau Docker et mappages (charte BOGOSS).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Structures réseau & mappages Docker" (gradient)
- Réseau central : squidresearch_network représenté comme un nuage/container réseau
- Services connectés au réseau :
  - Services web (web, frontend, mobile) - zone bleue
  - Services data (db, redis) - zone verte
  - Services automation (n8n, flowise, worker, beat) - zone violette
- Types de connexions :
  - API REST : flèches bleues
  - Redis Pub/Sub : flèches orange
  - Database : flèches vertes
- Volumes Docker : représenter les volumes persistants (postgres_data, redis_data, etc.)
- Sécurité : badge "Réseau isolé" avec icône cadenas
- Design : schéma réseau professionnel, zones colorées, légende
- Format : 1080x1080px

RÉSULTAT : Visualisation technique des structures réseau
```

---

### Slide 8 : Volumes & Mappages Docker
**Texte sur slide :**
```
Volumes & Mappages Docker - Persistance

📦 Volumes persistants :
   • postgres_data → Données PostgreSQL
   • redis_data → Cache Redis
   • n8n_data → Workflows n8n
   • flowise_data → Modèles Flowise

🔗 Bind mounts :
   • Code source → Hot reload dev
   • Logs → Monitoring
   • Config → Paramètres services

💾 Structures persistantes :
   → Données survivent aux redémarrages
   → Backup automatique possible
   → Isolation complète des données
```

**Visuel :** `assets/sanitized/post-01-slide-08-volumes-mappages.png`

**Prompt Claude pour infographie :**
```
Crée une infographie des volumes et mappages Docker (charte BOGOSS, style technique).

STYLE BOGOSS : Même charte

CONTENU :
- Titre : "Volumes & Mappages Docker - Persistance" (gradient)
- Layout : 2 sections principales

SECTION 1 - VOLUMES PERSISTANTS (gauche) :
  - 4 volumes représentés comme disques/containers :
    1. postgres_data - icône DB, couleur bleu (#3b82f6)
       - Label : "Données PostgreSQL"
       - Taille : "Persistant"
    2. redis_data - icône cache, couleur rouge (#ef4444)
       - Label : "Cache Redis"
       - Taille : "Persistant"
    3. n8n_data - icône workflow, couleur violet (#6366f1)
       - Label : "Workflows n8n"
       - Taille : "Persistant"
    4. flowise_data - icône IA, couleur rose (#ec4899)
       - Label : "Modèles Flowise"
       - Taille : "Persistant"
  - Flèches pointillées des services vers leurs volumes
  - Badge "Survit aux redémarrages" (vert)

SECTION 2 - BIND MOUNTS (droite) :
  - 3 mappages représentés comme liens :
    1. Code source → Hot reload dev
       - Icône : fichiers code, couleur cyan (#06b6d4)
    2. Logs → Monitoring
       - Icône : fichiers logs, couleur orange (#f59e0b)
    3. Config → Paramètres services
       - Icône : fichiers config, couleur vert (#10b981)
  - Flèches pointillées montrant les mappages
  - Badge "Synchronisation temps réel" (cyan)

- Design : disques/volumes stylisés, flèches pointillées, badges de persistance
- Format : 1080x1080px
- Éléments : icônes volumes, flèches mappages, badges sécurité

RÉSULTAT : Visualisation claire de la persistance et des mappages Docker
```

---

### Slide 9 : Résultats & CTA
**Texte sur slide :**
```
Résultats & Performance - Métriques réelles

⚡ Cache hit : < 0.1s (mesuré, si cache hit)
🛡️ Avec Tor : 5-8s/requête (réalité production)
📊 Gain cache : 98x plus rapide (benchmark : 100 contacts)
🔄 Import CSV : 100% succès (145 créés, 0 ignorés)
🆕 Normalisation : Détection auto colonnes (IntelligentMapper)

Performance réelle : Lent avec Tor/humanisation (5-8s),
rapide seulement avec cache hit (< 0.1s)
🆕 Import CSV : Refactorisation complète Nov 2025

🚀 Découvrir l'architecture complète
→ Testez le module Enriched
→ Documentation technique disponible

#SquidResearch #Docker #EnrichissementDonnées
```

**Visuel :** `assets/sanitized/post-01-slide-09-resultats-cta.png`

**Prompt Claude pour infographie :**
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

RÉSULTAT : Slide final impactant avec métriques RÉELLES vérifiables, CTA clair et actionnable, effet "whaou" basé sur la réalité
```

---

## 🖼️ Visuels à créer

### Checklist des infographies
- [ ] Slide 1 : Architecture Docker overview
- [ ] Slide 2 : Problèmes enrichissement
- [ ] Slide 3 : Module Enriched solution
- [ ] Slide 4 : Principes de fonctionnement détaillés
- [ ] Slide 5 : Services Docker détaillés
- [ ] Slide 6 : Flux de données
- [ ] Slide 7 : Réseaux, APIs & Webhooks
- [ ] Slide 8 : Volumes & Mappages Docker
- [ ] Slide 9 : Résultats & CTA

### Format des visuels
- **Dimensions** : 1080x1080px (carré pour LinkedIn carousel)
- **Format** : PNG (fond transparent ou blanc)
- **Résolution** : 300 DPI pour qualité optimale
- **Emplacement** : `assets/sanitized/post-01-slide-XX.png`

### Instructions pour Claude (création infographies)
1. Utiliser les prompts fournis ci-dessus pour chaque slide
2. Respecter la charte BOGOSS (couleurs, gradients, style)
3. Créer des infographies modernes, data-driven, avec effet "whaou"
4. Exporter en PNG 1080x1080px
5. Sauvegarder dans `assets/sanitized/`

---

## ✅ Checklist sécurité
- [ ] Aucun identifiant/mot de passe non masqué
- [ ] Aucune IP/URL interne visible (utiliser localhost ou exemples)
- [ ] Données clients anonymisées
- [ ] Captures floutées si nécessaire
- [ ] Script `validate-campaign.sh` exécuté
- [ ] Tous les slides vérifiés individuellement
- [ ] Pas de tokens/API keys dans les visuels
- [ ] Variables d'environnement non exposées

---

## 📊 Suivi (à remplir après publication)
- **Date publication réelle** : 
- **Impressions** : 
- **Engagement (likes / comments / shares)** : 
- **Taux de completion carousel** : 
- **Slide le plus vu** : 
- **Slide le plus engagé** : 
- **Leads ou réponses** : 
- **Clics CTA** : 
- **Leçon / Next step** : 

---

## 📝 Notes techniques

### Points clés à mettre en avant
1. **Architecture microservices** : 9 services Docker orchestrés
2. **Module Enriched** : Orchestration intelligente (éviter termes Kali/OSINT)
3. **Performance** : Cache hit < 0.1s, Tor 5-8s/req (réalité production)
4. **🆕 Import CSV intelligent** : 100% succès avec détection auto colonnes (Nov 2025)
5. **🆕 Normalisation** : Refactorisation complète avec IntelligentMapper
6. **Scalabilité** : Millions de données, parallélisation
7. **Sécurité** : Réseau isolé, volumes persistants

### Ton et style
- **Ton** : Technique mais accessible
- **Style** : Data-driven, professionnel, moderne
- **Approche** : Éducatif, démonstratif
- **Effet recherché** : "Whaou" avec infographies impactantes

### Références techniques
- Architecture Docker : `docker-compose.yml`
- Module Enriched : `apps/scrapper/enriched/`
- Orchestrateur : `enrichment_orchestrator.py`
- Documentation : `docs/TECHNICAL.md`

