# Épisode 2 : Architecture Docker & Module Enriched

> **SquidResearch** - Présentation technique  
> Format : Présentation Gamma interactive  
> Identité visuelle : Iceberg numérique + Porte-conteneur Docker

---

## 🎨 Instructions d'identité visuelle

**Palette de couleurs :**
- Fond : Dégradé bleu foncé profond (#0a0e27 → #1a1f3a → #1e3a5f)
- Accents cyan : #06b6d4, #22d3ee, #67e8f9 (iceberg numérique)
- Bleu cargo : #1e3a5f, #2d4a6f (porte-conteneur)
- Violet/Indigo : #6366f1, #818cf8 (éléments techniques)
- Rose/Magenta : #ec4899, #f472b6 (highlights)
- Vert succès : #10b981, #34d399

**Éléments décoratifs récurrents :**
- **Iceberg numérique** : Structure géométrique cyan lumineuse (glow effect) - toujours présent en arrière-plan subtil ou décoration
- **Porte-conteneur numérique** : Cargo ship stylisé bleu foncé - élément décoratif discret (coin, filigrane)
- **Effets** : Glassmorphism sur les cartes, glow cyan sur les éléments importants

**Typographie :** Poppins (ou Inter) - Bold pour titres, Regular pour corps

---

# 🐙 SquidResearch - Architecture Docker

**9 services orchestrés**

PostgreSQL • Django • React • Celery  
n8n • Flowise • Redis • Tor • Mobile

Architecture scalable pour enrichissement B2B

---

**Instructions visuelles :**
- Fond : Dégradé bleu foncé avec iceberg cyan discret en arrière-plan (opacité 15%)
- Visuel principal : 9 services représentés comme des conteneurs Docker stylisés (style porte-conteneur)
- Services : PostgreSQL (bleu), Django (vert), React (cyan), Celery (orange), n8n (violet), Flowise (rose), Redis (rouge), Tor (gris foncé), Mobile (cyan)
- Réseau : squidresearch_network représenté par des lignes de connexion cyan lumineuses
- Décoration : Porte-conteneur miniature en coin (opacité 30%)
- Titre : Cyan #06b6d4, Poppins Bold 72px
- Texte : Blanc cassé rgba(226, 232, 240, 0.9), Poppins Regular 24px

---

# Le défi de l'enrichissement B2B

Avant le module Enriched : chaque enrichissement prenait 30-60 secondes, avec des coûts API qui explosaient et des données incohérentes.

## ❌ Données dispersées
**Problème :** Email dans une API, domaine dans une autre, entreprise ailleurs.  
**Impact :** 5-10 requêtes séquentielles par entreprise, temps cumulé : 45s en moyenne.

## ❌ Sources multiples
**Problème :** Sources multiples non synchronisées, pas d'orchestration.  
**Impact :** Données contradictoires, nécessité de fusion manuelle.

## ❌ Requêtes lentes
**Problème :** Appels API séquentiels, pas de parallélisation.  
**Impact :** 30-60s par entreprise, impossible de traiter en masse.

## ❌ Pas de cache
**Problème :** Même entreprise enrichie 10 fois = 10x le coût API.  
**Impact :** Coûts multipliés par 5-10, budgets explosés rapidement.

**Résultat :** Enrichir 1000 entreprises = 8-15 minutes + 50-100€ de coûts API

---

**Instructions visuelles :**
- Fond : Dégradé bleu foncé avec iceberg cyan discret
- Grille 2x2 : 4 cartes problèmes avec bordures rouges/orange
- Cartes : Glassmorphism (fond rgba(239, 68, 68, 0.1), bordure rgba(239, 68, 68, 0.4))
- Graphiques : Petits graphiques de performance négative (lignes descendantes) sur cartes 1 et 3
- Titre : Rouge #ef4444, Poppins Bold 64px
- Décoration : Porte-conteneur miniature en coin bas droit

---

# ✅ Module Enriched - Orchestration intelligente

## Groupement par domaine
→ 100 entreprises → 20 domaines uniques  
→ 1 requête par domaine au lieu de 100

## Cache partagé automatique
→ Vérification avant chaque requête  
→ TTL 24h, hit rate optimisé  
→ Cache hit : < 0.1s

## Rate limiting global
→ 5-8s entre requêtes (Tor)  
→ Max 10-12 req/min  
→ Protection anti-ban

## Ordre optimal d'exécution
→ Cascade intelligente : INSEE → Pappers → Registrar  
→ Données complémentaires, pas redondantes

**Enrichissement multi-sources unifié**

---

**Instructions visuelles :**
- Fond : Dégradé bleu avec iceberg cyan plus visible (opacité 25%)
- Centre : Module Enriched représenté comme un hub central (icône engrenage/cercles concentriques) avec glow cyan
- 4 capacités autour du hub : Groupement (bleu), Cache (vert), Rate limiting (orange), Ordre optimal (cyan)
- Sources connectées : Email Enriched, Domain Enriched, Company Enriched, Social Media Enriched, Intelligence Tools
- Design : Hub central avec rayons cyan vers les sources
- Titre : Gradient violet/rose, Poppins Bold 56px
- Décoration : Porte-conteneur miniature en coin

---

# Principes de fonctionnement détaillés

## 1️⃣ Groupement par domaine
**100 entreprises → 20 domaines uniques**  
1 requête par domaine au lieu de 100  
**Gain : 80% réduction requêtes**

## 2️⃣ Cache partagé Redis
**Flux :** Requête → Cache check → Hit/Miss  
**Cache hit : < 0.1s** (badge vert)  
**TTL 24h** (badge cyan)

## 3️⃣ Cascade intelligente
**Flux vertical :** INSEE → Pappers → Registrar  
**Données complémentaires :** INSEE (SIREN) → Pappers (financier) → Registrar (domaine)  
Flèches pointillées montrant la cascade

## 4️⃣ Rate limiting humanisé
**Timeline :** 5-8s entre requêtes  
**Max 10-12 req/min** (badge orange)  
**Protection :** Anti-ban activé (badge rouge)

---

**Instructions visuelles :**
- Fond : Dégradé bleu avec iceberg cyan discret
- Grille 2x2 : 4 cartes avec principes détaillés
- Graphiques : Comparatifs avant/après, timeline, flux vertical
- Badges : Métriques en badges colorés (vert, cyan, orange, rouge)
- Cartes : Glassmorphism avec bordures cyan subtiles
- Titre : Cyan #06b6d4, Poppins Bold 48px
- Décoration : Porte-conteneur miniature

---

# Architecture Docker détaillée

## 📊 Data Layer
- **PostgreSQL** : Base de données principale
- **Redis** : Cache & Queue

## ⚡ Application Layer
- **Django** : Backend web
- **Celery Worker** : Tâches asynchrones
- **Celery Beat** : Planification

## 🎨 Frontend & Tools
- **React** : Interface web
- **React Native** : Application mobile
- **n8n** : Automation workflows
- **Flowise** : IA & LLM

**Réseau isolé :** squidresearch_network

---

**Instructions visuelles :**
- Fond : Dégradé bleu foncé avec iceberg cyan en arrière-plan
- Layout : 3 colonnes verticales (Data Layer, Application Layer, Frontend & Tools)
- Services : Représentés comme des conteneurs stylisés (style cargo ship)
- Réseau : squidresearch_network comme nuage connectant tous les services
- Flèches : Dépendances en cyan lumineux (db → web, redis → worker, web → frontend)
- ⚠️ SÉCURITÉ : Ne PAS afficher les ports
- Titre : Violet #6366f1, Poppins Bold 56px
- Décoration : Porte-conteneur miniature

---

# Flux de données Enriched - Pipeline détaillé

## 1️⃣ Input
**Entreprise/Email/Domaine**  
→ Validation & normalisation

## 2️⃣ Orchestrateur
**Groupement & Cache Redis**  
→ Vérification cache, planification requêtes  
→ **Cache hit : < 0.1s** (si hit)

## 3️⃣ Enrichissement
**Sources avec APIs officielles**  
→ INSEE Sirene (API gratuite)  
→ Pappers (API documentée)  
→ Société.com (scraper)  
→ DNS/WHOIS (outils Python)  
→ **Avec Tor : 5-8s/requête, max 10-12 req/min**

## 4️⃣ Consolidation
**Fusion intelligente**  
→ Résolution conflits, priorisation sources

## 5️⃣ Output
**Données enrichies JSON**  
→ Format UnifiedEnrichmentResult  
→ Cache mis à jour (TTL 24h)

---

**Instructions visuelles :**
- Fond : Dégradé bleu avec iceberg cyan discret
- Flux horizontal : 5 étapes de gauche à droite avec flèches cyan lumineuses
- Pipeline : Largeurs variables selon importance, effet de profondeur
- Métriques : Badges de temps (vert pour cache hit, orange pour Tor)
- Design : Pipeline visuel moderne avec effets glow
- Titre : Cyan #06b6d4, Poppins Bold 48px
- Décoration : Porte-conteneur miniature

---

# Réseaux, APIs & Webhooks

## 🌐 Réseau Docker
**squidresearch_network** (isolé)

## 📡 Connexions détaillées
- **API REST** : `/api/enriched/`, `/companies/search/`
- **Webhooks** : `/webhooks/`, `/api/n8n/webhooks/`
- **Redis Pub/Sub** : Celery tasks, cache notifications
- **Database** : Django ORM, migrations

## 🔒 Sécurité
Réseau bridge isolé, pas de ports exposés

## 📊 Volumes
postgres_data, redis_data, n8n_data, flowise_data

## 🔄 Services
Django ↔ React ↔ Celery ↔ n8n ↔ Flowise

**Isolation + APIs documentées + Webhooks**

---

**Instructions visuelles :**
- Fond : Dégradé bleu foncé avec iceberg cyan discret
- Réseau central : squidresearch_network comme nuage/container réseau avec glow cyan
- Zones colorées : Web (bleu), Data (vert), Automation (violet)
- Types de connexions : API REST (flèches bleues), Redis Pub/Sub (orange), Database (vertes)
- Volumes : Représentés comme disques persistants
- Badge sécurité : "Réseau isolé" avec icône cadenas
- Titre : Violet #6366f1, Poppins Bold 48px
- Décoration : Porte-conteneur miniature

---

# Volumes & Mappages Docker - Persistance

## 📦 Volumes persistants
- **postgres_data** → Données PostgreSQL
- **redis_data** → Cache Redis
- **n8n_data** → Workflows n8n
- **flowise_data** → Modèles Flowise

**Survit aux redémarrages** (badge vert)

## 🔗 Bind mounts
- **Code source** → Hot reload dev
- **Logs** → Monitoring
- **Config** → Paramètres services

**Synchronisation temps réel** (badge cyan)

## 💾 Structures persistantes
→ Données survivent aux redémarrages  
→ Backup automatique possible  
→ Isolation complète des données

---

**Instructions visuelles :**
- Fond : Dégradé bleu avec iceberg cyan discret
- Layout : 2 sections (Volumes persistants gauche, Bind mounts droite)
- Volumes : Représentés comme disques/containers stylisés avec icônes colorées
- Flèches : Pointillées des services vers leurs volumes
- Badges : "Survit aux redémarrages" (vert), "Synchronisation temps réel" (cyan)
- Design : Disques stylisés, flèches mappages, badges sécurité
- Titre : Cyan #06b6d4, Poppins Bold 48px
- Décoration : Porte-conteneur miniature

---

# Résultats & Performance - Métriques réelles

## ⚡ Cache hit : < 0.1s
**Temps mesuré** (benchmark réel)  
*Seulement si cache hit*

## 🛡️ Avec Tor : 5-8s/requête
**Performance réelle** (Tor + humanisation)  
*Max 10-12 req/min (rate limiting)*

## 🔄 Import CSV : 100%
**Succès import** (145 créés, 0 ignorés)  
*🆕 Détection auto colonnes (IntelligentMapper)*

## 📊 Gain cache : 98x
**Plus rapide** (benchmark réel)  
*Scénario : 100 contacts même entreprise*

---

**Performance réelle :** Lent avec Tor/humanisation (5-8s), rapide seulement avec cache hit (< 0.1s)

**🆕 Import CSV :** Refactorisation complète Nov 2025

---

## 🚀 Découvrir l'architecture complète
→ Testez le module Enriched  
→ Documentation technique disponible

#SquidResearch #Docker #EnrichissementDonnées

---

**Instructions visuelles :**
- Fond : Dégradé bleu foncé avec iceberg cyan plus visible (opacité 30%)
- Grille 2x2 : 4 cartes métriques avec graphiques stylisés
- Graphiques : Barres horizontales (vert pour cache, orange pour Tor), Pie chart (vert 100%), Comparatif avant/après (cyan)
- Badges : Icônes colorées (⚡, 🛡️, 🔄, 📊)
- CTA : Bouton "Découvrir l'architecture" (gradient violet/rose, grand et visible)
- Design : Cartes modernes avec ombres, graphiques basés sur benchmarks réels
- Titre : Gradient violet/rose, Poppins Bold 56px
- Décoration : Porte-conteneur miniature + iceberg cyan plus visible

---

## 📝 Notes techniques

### Points clés
- Architecture microservices : 9 services Docker orchestrés
- Module Enriched : Orchestration intelligente
- Performance : Cache hit < 0.1s, Tor 5-8s/req (réalité production)
- 🆕 Import CSV intelligent : 100% succès avec détection auto colonnes (Nov 2025)
- 🆕 Normalisation : Refactorisation complète avec IntelligentMapper
- Scalabilité : Millions de données, parallélisation
- Sécurité : Réseau isolé, volumes persistants

### Ton et style
- Technique mais accessible
- Data-driven, professionnel, moderne
- Éducatif, démonstratif
- Effet recherché : "Whaou" avec infographies impactantes

---

**Instructions globales pour Gamma :**
- Appliquer l'identité visuelle (iceberg + porte-conteneur) sur toutes les slides
- Utiliser la palette cyan/bleu dominante
- Effets glassmorphism sur les cartes
- Glow cyan sur les éléments importants
- Typographie Poppins cohérente
- Logo SquidResearch (poulpe avec loupe) présent sur la couverture

