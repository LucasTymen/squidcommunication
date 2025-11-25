# 🗞️ Communication Log - SquidCommunication

> **Note** : Ce fichier est synchronisé depuis `squidResearch/communication_projet.md`  
> **Dernière sync** : 2025-11-22 14:06:15 UTC  
> **Source** : `../squidResearch/communication_projet.md`

---


> Journal horodaté des campagnes de communication SquidResearch.  
> Chaque entrée reprend plateformes, statut, nombre de contenus, assets, sécurité et actions MCP (Claude).

---

## 🔧 Workflow & Structure

- **Campagne** → `data/communication/<slug>/campaign.json`
- **Plateforme** → `data/communication/<slug>/<platform>/post.json`
- **Assets** → `data/communication/<slug>/assets/{original|sanitized}/`
- **Archive** → `data/communication/<slug>/archive/` (messages finaux, exports, analytics)
- **Collaboration MCP (Claude)** : planification GCal/Drive, templates Notion/Canvas, publication Vercel, consignée dans “MCP Actions”.

### 🔒 Checklist Sécurité (à valider avant diffusion)

- [ ] Aucune IP visible (`192.***.***.***`)
- [ ] Credentials masqués (`pa****rd`)
- [ ] Pas de tokens/API keys dans les captures
- [ ] Données clients anonymisées ou floutées
- [ ] URLs internes remplacées par `https://app.example.com`
- [ ] Variables d’environnement non exposées
- [ ] Pas de noms/emails réels dans les démos
- [ ] Validation script `scripts/validate_campaign.sh` exécutée (si applicable)

---

## [2025-11-25 23:45] 📁 Structure Standardisée des Articles

- **Action** : Organisation standardisée des articles avec structure `article-X-nom/Presentation/`
- **Statut** : ✅ Structure créée et articles préparés
- **Localisation** : `articles/`

### 📋 Structure Standardisée

**Format obligatoire** :
```
articles/
└── article-X-nom-de-l-article/
    ├── Presentation/              # Slides HTML générées (OBLIGATOIRE)
    │   ├── slide1.html
    │   ├── slide2.html
    │   └── ...
    ├── linkedin/                 # Posts LinkedIn
    ├── assets/                   # Assets (images, vidéos)
    ├── PROMPTS_INFOGRAFIES_CLAUDE.md
    ├── campaign.json
    └── README.md
```

### ✅ Actions Réalisées

**Réorganisation** :
- ✅ Épisode 2 réorganisé : `articles/article-2-architecture-docker-enriched/`
- ✅ Slides déplacées vers `Presentation/` (9 slides HTML)
- ✅ Contenu existant préservé (linkedin/, assets/, prompts, etc.)

**Préparation articles** :
- ✅ Article 3 : `article-3-algorithmes-matching-intelligents/` (README créé)
- ✅ Article 4 : `article-4-import-csv-intelligent/` (README créé)
- ✅ Article 5 : `article-5-15-job-boards-francais/` (README créé)

**Documentation** :
- ✅ Charte éditoriale mise à jour avec structure standardisée
- ✅ Règles de nommage documentées (kebab-case, pas d'espaces)
- ✅ Workflow de création documenté

### 📝 Règles de Nommage

- **Dossier article** : `article-X-nom-de-l-article` (kebab-case, pas d'espaces)
- **Slides** : Toujours dans `Presentation/` (avec majuscule)
- **Format slides** : `slide1.html`, `slide2.html`, etc.
- **Exemples** :
  - ✅ `article-2-architecture-docker-enriched/`
  - ✅ `article-3-algorithmes-matching-intelligents/`
  - ❌ `article 2 - architecture docker/` (espaces interdits)

### 🎯 Prochaines Étapes

- [ ] Générer slides pour articles 3, 4, 5
- [ ] Créer posts LinkedIn pour articles 3, 4, 5
- [ ] Préparer prompts infographies
- [ ] Créer assets (images, vidéos)

---

## [2025-11-22 15:00] 🎯 Algorithmes Matching Intelligents - Phase Finale Terminée

### 🏆 RÉSULTAT FINAL
**✅ PHASE FINALE TERMINÉE AVEC SUCCÈS**
- **26/26 tests passent** ✅
- **Coverage global : 62%** (modules critiques >85%) ✅
- **Toutes les features vérifiées et fonctionnelles** ✅
- **Système prêt pour production** 🚀

### 📊 Résultats Tests et Coverage

**Tests** : 26/26 PASSED ✅
- Phase 1 Algorithmes : 8/8 ✅
- Phase 2 CRUD/Variables/Use-cases : 13/13 ✅
- Intégration : 3/3 ✅
- Performance : 2/2 ✅

**Coverage** : 62% global
- Modules critiques >85% :
  - `algorithm_factory.py` : 96%
  - `base_matching_algorithm.py` : 86%
  - `skills_matching_algorithm.py` : 87%
  - `matching_service.py` : 85%

### 🎯 Fonctionnalités Validées

**Phase 1 - Algorithmes** :
- ✅ 5 algorithmes de matching avec modèles mathématiques
- ✅ JobSearch, TalentSourcing, SkillsMatching, CompanyOutreach, Networking
- ✅ Validation, normalisation, confiance, explications automatiques

**Phase 2 - Services** :
- ✅ CRUD workflows complets
- ✅ Variables configurables (poids, seuils, filtres)
- ✅ Use-cases pour tous les types de workflows
- ✅ Error cases avec 5 types d'erreurs gérées
- ✅ API complète (GET/POST/PUT/DELETE)
- ✅ Matching Engine avec enrichissement automatique

**Intégration** :
- ✅ Cycle de vie workflow complet
- ✅ Batch processing
- ✅ Gestion erreurs robuste

### 📝 Documentation Créée

- ✅ `PHASE_FINALE_RAPPORT_FINAL.md` : Rapport complet
- ✅ `PHASE_FINALE_TESTS_COVERAGE.md` : Guide tests
- ✅ Base de connaissances mise à jour
- ✅ Logs mis à jour

### 🔧 Corrections Appliquées

- ✅ `app_label` ajouté à tous les modèles
- ✅ Imports corrigés
- ✅ Migration appliquée
- ✅ Bugs assertions corrigés
- ✅ Logger ajouté

**Statut** : ✅ **Système de matching prêt pour production**

---

## [2025-11-21 12:30] 🔄 Routine Récurrente - Mise à Jour Landing Page Vercel

### 📋 Tâche Récurrente Ajoutée

**Objectif** : Maintenir la landing page Vercel (`landingpageCvPagePerso`) à jour avec les dernières fonctionnalités de SquidResearch.

**Fréquence** : Après chaque feature majeure ou mensuellement

**Fichiers concernés** :
- `/home/lucas/lucasTymenGraphx/landingpageCvPagePerso/public/squid-research.html`
- `/home/lucas/lucasTymenGraphx/landingpageCvPagePerso/public/assets/js/projects.js` (FR)
- `/home/lucas/lucasTymenGraphx/landingpageCvPagePerso/public/assets/js/projects-en.js` (EN)

**Checklist** :
- [ ] Vérifier nouvelles fonctionnalités depuis dernière mise à jour
- [ ] Mettre à jour sous-titre hero
- [ ] Ajouter nouvelles fonctionnalités dans section dédiée
- [ ] Mettre à jour tags techniques
- [ ] Mettre à jour architecture technique (sans ports pour sécurité)
- [ ] Mettre à jour état d'avancement (phases terminées)
- [ ] Mettre à jour technologies et outils
- [ ] Mettre à jour résultats actuels
- [ ] Mettre à jour apprentissages clés
- [ ] Mettre à jour cartes projets (FR et EN)
- [ ] Vérifier liens GitHub/GitLab

**Documentation** :
- ✅ Guide créé : `docs/BONNES_PRATIQUES_LANDING_PAGE.md`
- ✅ Référence ajoutée dans `.cursor/reminder_files.md`
- ✅ Checklist ajoutée pour chaque fin de feature majeure

**Règles de sécurité** :
- ⚠️ Ne jamais afficher les ports Docker
- ⚠️ Ne jamais afficher de secrets/API keys
- ⚠️ Ne jamais afficher d'URLs internes
- ✅ Afficher uniquement technologies publiques et fonctionnalités documentées

**Référence** : Voir `LANDING_PAGE_VERCEL_CONTENT.md` pour contenu structuré

---

## [2025-11-12 16:25] Initialisation Hub éditorial

- **Campagne** : `2025-11-hub-communication`
- **Objectif** : Mettre en place l'architecture éditoriale (repo sibling, log, templates JSON)
- **Plateformes** : LinkedIn (post lancement), Instagram (story teasing), Newsletter optionnelle
- **Statut** : 📋 Draft
- **Articles prévus** : 3 (1 LinkedIn, 1 Instagram, 1 Newsletter recap)
- **Assets** : `data/communication/2025-11-hub-communication/assets/`
- **Sécurité** : Checklist à compléter avant captures (screen dashboards floutés)
- **MCP Actions** :
  - Claude → Préparer planning éditorial (GCal + Drive) [à lancer]
  - Claude → Mapper templates Notion/Canva (landing, storytelling) [à lancer]
- **Notes** :
  - Créer repo sibling `squidCommunication/` (landing, docs, templates)
  - Générer script CLI + template JSON pour accélérer les futures campagnes
  - Prévoir archivage analytics (LinkedIn/Instagram Insights) dans `analytics.json`

---

## [2025-11-12 17:00] ✅ Hub éditorial créé - Structure complète

- **Action** : Création du repo sibling `squidCommunication/`
- **Statut** : ✅ Terminé
- **Localisation** : `/home/lucas/tools/squidCommunication/`

### 📁 Structure créée

```
squidCommunication/
├── README.md                      # Documentation complète
├── .gitignore                     # Sécurité (assets/original exclus)
├── landing/                       # Site vitrine (à venir)
├── docs/                          # Centre de documentation (à venir)
├── campaigns/                     # Campagnes organisées
│   └── 2025-11-hub-communication/
│       ├── campaign.json          # Config complète avec KPIs
│       ├── linkedin/
│       │   └── post-dogfooding.md (2 versions)
│       ├── instagram/
│       │   ├── story-setup.md
│       │   └── story-cta.md
│       └── assets/
│           ├── original/          # (gitignored)
│           └── sanitized/         # Pour publication
├── templates/                     # Templates réutilisables
│   ├── linkedin-post.md
│   ├── instagram-story.md
│   ├── campaign-brief.md
│   └── editorial-guidelines.md    # Charte complète
└── scripts/
    └── validate-campaign.sh       # Validation sécurité automatique
```

### ✅ Livrables

1. **README.md** : Documentation complète du workflow
2. **Templates Markdown** :
   - LinkedIn post (structure 3-5 paragraphes)
   - Instagram story (format vertical, texte court)
   - Brief campagne (objectifs, KPIs, MCP tasks)
   - Guidelines éditoriales (ton, style, fréquence, exemples)
3. **Script validation** : `validate-campaign.sh`
   - Détection credentials/tokens/API keys
   - Détection IPs privées
   - Vérification structure campagne
   - Output coloré (erreurs/warnings)
4. **Première campagne pilote** : `2025-11-hub-communication`
   - campaign.json avec KPIs définis
   - 1 post LinkedIn (2 versions : Meta + Pédagogique)
   - 2 stories Instagram (Setup + CTA)
   - Security checklist intégrée

### 🎯 Principes appliqués

- **Séparation des préoccupations** : Code produit (squidResearch) vs Contenu marketing (squidCommunication)
- **Sécurité by design** : assets/original gitignored, validation automatique
- **Dogfooding** : Utiliser la création du hub comme premier contenu
- **Traçabilité** : Tout versionné, tout documenté, tout horodaté

### 🚀 Git

- **Repo initialisé** : ✅
- **Branch** : `main` (convention moderne)
- **Premier commit** : `5d5ec74` (11 fichiers, 1185 lignes)
- **Message** : "🎉 Initial commit: Hub éditorial SquidResearch"

### 📋 Prochaines étapes

1. **Créer les assets** pour la campagne pilote :
   - Capture structure repo (floutée)
   - Schéma architecture hub
   - Visuel Instagram (design graphique)
2. **Exécuter validation** : `./scripts/validate-campaign.sh campaigns/2025-11-hub-communication`
3. **Intégration MCP** :
   - Créer événement Google Calendar (date publication)
   - Organiser dossier Drive pour assets
   - Template Notion pour tracking KPIs
4. **Landing page** (Next.js ou Astro) :
   - Déploiement Vercel
   - Présentation SquidResearch
   - Lien vers docs techniques
5. **Publication campagne pilote** :
   - LinkedIn : 2025-11-15 10:00
   - Instagram : 2025-11-15 10:30 + 18:00

### 🔗 Références & Synchronisation

- **Repo squidCommunication** : `/home/lucas/tools/squidCommunication/`
- **Log principal** : `squidResearch/communication_projet.md` (ce fichier)
- **Base de connaissance** : `private/IDEAS.md` + `private/ROADMAP.md`
- **Documentation IP** : `docs/legal/IP_*.md`
- **Synchronisation** : Utiliser `./scripts/sync_repos.sh` pour synchroniser avec squidCommunication

#### 🔄 Synchronisation Bidirectionnelle

**Scripts disponibles** :
- `./scripts/sync_communication_log.sh` : Synchronise uniquement le log
- `./scripts/sync_repos.sh` : Synchronisation complète (log + docs)

**Workflow recommandé** :
1. Modifier ce fichier (`communication_projet.md`)
2. Exécuter : `./scripts/sync_repos.sh all`
3. Le fichier est automatiquement copié vers `squidCommunication/communication_log.md`

---

## [2025-11-12 17:40] Plan d’automatisation LinkedIn (tokens limités)

- **Contexte** : Budget Claude < 100 €/semaine → anticiper contenus pour limiter les requêtes MCP.
- **Action prévue** : Script `scripts/create-linkedin-campaign.sh` + nouveaux templates (simple & carrousel).
- **Spécifications** :
  - Args : `slug`, `type (simple|carousel)`, `nb_messages` (3–5).
  - Génère : `campaign.json`, `linkedin/post-XX.md`, `schedule.json`, dossiers assets `original/` & `sanitized/`.
  - Templates : `templates/linkedin-post-simple.md`, `linkedin-post-carousel.md`, `linkedin-schedule.template.json`.
  - Rappels checklist sécurité intégrés dans chaque post.
- **Workflow cible** :
  1. Exécuter script → structure prête.
  2. Renseigner contenu, déposer assets (version floutée).
  3. `./scripts/validate-campaign.sh …` → check sécurité.
  4. Claude intervient uniquement pour planifier (GCal/Drive/Notion) et publier/monitorer.
- **Points de blocage & améliorations** :
  - ChatGPT → développement script & templates (ETA < 1h).
  - Claude → consigner dans log toute limite MCP (tokens restants, actions impossibles, besoins complémentaires).
  - Amélioration envisagée : append automatique dans ce log après exécution du script (à étudier).
- **Étapes suivantes** :
  - Implémenter script + templates.
  - Mettre à jour README/workflow pour inclure `create-linkedin-campaign.sh`.
  - Tester sur nouvelle campagne (ex. `2025-12-feature-X`).
  - Documenter procédure mutualisée de push (squidResearch + squidCommunication).

---

## [2025-11-12 19:45] ✅ Script LinkedIn automatisé - Implémentation terminée

- **Action** : Création du script `create-linkedin-campaign.sh` et templates associés
- **Statut** : ✅ Terminé
- **Localisation** : `/home/lucas/tools/squidCommunication/`

### ✅ Livrables créés

1. **Script `scripts/create-linkedin-campaign.sh`** :
   - Génère campagne LinkedIn complète (3-5 posts)
   - Support types : `simple` ou `carousel`
   - Crée automatiquement : `campaign.json`, `linkedin/post-XX.md`, `linkedin/schedule.json`, structure assets
   - Calcul automatique des dates (espacement 2 jours)
   - README.md par campagne avec checklist

2. **Templates** :
   - ✅ `templates/linkedin-post-simple.md` (déjà existant)
   - ✅ `templates/linkedin-post-carousel.md` (nouveau)
   - Structure carousel : 5 slides (Accroche → Problème → Solution → Résultat → CTA)

3. **Documentation collaboration** :
   - ✅ `docs/collaboration-cursor-claude.md`
   - Workflow mutualisé Cursor ↔ Claude
   - Points de blocage & améliorations documentés
   - Procédure push mutualisé

### 📋 Usage

```bash
cd /home/lucas/tools/squidCommunication/scripts
./create-linkedin-campaign.sh "feature-matching" simple 5
./create-linkedin-campaign.sh "tutorial-enrichment" carousel 3
```

### 🚨 Points de blocage & améliorations (Cursor)

#### ✅ Résolus
- Script fonctionnel avec validation arguments
- Génération automatique structure complète
- Templates simple & carousel disponibles
- Dates calculées automatiquement (Python)

#### 🔄 À améliorer (futures sessions)
- [ ] **Auto-update `communication_projet.md`** : Le script devrait automatiquement ajouter une entrée dans le log après génération
- [ ] **Génération dates intelligentes** : Prendre en compte weekends et heures optimales LinkedIn (8h-10h, 17h-19h)
- [ ] **Validation contenu** : Vérifier que les posts ne sont pas vides avant validation sécurité
- [ ] **Enrichissement `campaign.json`** : Ajouter métadonnées (tags, catégories, cibles)

### 📝 Notes techniques

- Dates générées : espacement de 2 jours, heure fixe 10:00 UTC (à affiner manuellement)
- Format JSON cohérent avec structure existante (`2025-11-hub-communication`)
- Script utilise Python3 pour manipulation JSON propre (évite problèmes de dates bash)

### 🎯 Prochaines étapes

1. **Tester le script** sur une nouvelle campagne :
   ```bash
   cd /home/lucas/tools/squidCommunication/scripts
   ./create-linkedin-campaign.sh "test-automation" simple 3
   ```

2. **Claude** : Consigner dans `docs/collaboration-cursor-claude.md` :
   - Tokens restants après cette session
   - Actions MCP possibles/impossibles
   - Besoins complémentaires si données manquantes

3. **Mettre à jour README/workflow.md** pour documenter le nouveau script

4. **Première campagne réelle** : Utiliser le script pour créer une vraie campagne LinkedIn

### 🔗 Références

- **Script** : `squidCommunication/scripts/create-linkedin-campaign.sh`
- **Templates** : `squidCommunication/templates/linkedin-post-{simple,carousel}.md`
- **Doc collaboration** : `squidCommunication/docs/collaboration-cursor-claude.md`
- **Log principal** : `squidResearch/communication_projet.md` (ce fichier)

---

## [2025-11-13 10:00] ✅ Épisode 2 : Architecture Docker & Module Enriched - Campagne créée

- **Action** : Création de la campagne "épisode-2-dockerisation-enriched"
- **Statut** : 📋 Draft - En attente création infographies
- **Localisation** : `/home/lucas/tools/squidCommunication/campaigns/2025-11-episode-2-dockerisation-enriched/`

### 📋 Contenu de l'épisode 2

**Format** : Post LinkedIn Carousel (9 slides)

**Thématiques** :
1. **Architecture Docker** : Vue d'ensemble des 9 services orchestrés
2. **Problème** : Complexité de l'enrichissement B2B non orchestré
3. **Solution** : Module Enriched - Orchestration intelligente
4. **Principes de fonctionnement** : Groupement, cache, cascade, rate limiting (NOUVEAU)
5. **Architecture détaillée** : Services Docker avec rôles et connexions
6. **Flux de données** : Pipeline d'enrichissement Enriched avec sources réelles
7. **Structures réseau** : Réseaux, APIs & Webhooks détaillés
8. **Volumes & Mappages** : Persistance Docker, bind mounts (NOUVEAU)
9. **Résultats & CTA** : Métriques réelles vérifiables et appel à l'action

**Approche** :
- ✅ Data-driven avec infographies créées par Claude
- ✅ Charte graphique BOGOSS (gradients violets/bleus, style moderne)
- ✅ Effet "whaou" recherché
- ✅ Terminologie : "Module Enriched" (éviter Kali/OSINT)
- ✅ Focus sur dockerisation, principes de fonctionnement, mappages

### ✅ Livrables créés

1. **`campaign.json`** : Configuration complète avec KPIs
2. **`linkedin/post-01-dockerisation-enriched.md`** :
   - Texte du post LinkedIn
   - Structure complète des 7 slides
   - **Prompts détaillés pour Claude** pour créer chaque infographie
   - Spécifications charte BOGOSS intégrées
3. **`README.md`** : Documentation complète de la campagne
4. **Structure assets** : Dossiers `original/` et `sanitized/` créés

### 🎨 Infographies à créer (Claude)

**9 infographies** avec prompts détaillés fournis :

1. **Architecture Docker overview** : 9 services, réseau, dépendances
2. **Problèmes enrichissement** : Visualisation des défis B2B
3. **Module Enriched solution** : Hub d'orchestration intelligent
4. **Principes de fonctionnement** : 4 principes (groupement, cache, cascade, rate limiting) (NOUVEAU)
5. **Services Docker détaillés** : Layout 3 colonnes, connexions (⚠️ ports supprimés - sécurité)
6. **Flux de données** : Pipeline horizontal 5 étapes avec sources réelles (INSEE, Pappers)
7. **Réseaux et mappages** : Structures réseau Docker, APIs/webhooks détaillés
8. **Volumes & Mappages** : Persistance Docker, bind mounts (NOUVEAU)
9. **Résultats & CTA** : Métriques réelles vérifiables, CTA clair

**Spécifications** :
- Format : PNG 1080x1080px, 300 DPI
- Charte : BOGOSS (couleurs #6366f1, #ec4899, gradients, style moderne)
- Style : Data-driven, professionnel, effet "whaou"
- ⚠️ **Métriques réelles uniquement** : Aucun chiffre inventé (voir `AVERTISSEMENT_METRIQUES.md`)
- ⚠️ **Sécurité** : Pas de ports Docker affichés

### ✅ Corrections appliquées (Session 10b)

**Métriques** :
- ❌ Métriques inventées supprimées (2M entreprises, 85%+ hit rate, 500 req/min)
- ✅ Métriques réelles utilisées (cache hit < 0.1s, Tor 5-8s/req, max 10-12 req/min)
- ✅ Contextes ajoutés (Tor/humanisation, cache hit uniquement si hit)

**Sécurité** :
- ✅ Tous les ports Docker supprimés des prompts
- ✅ Avertissements sécurité ajoutés partout

**Sources** :
- ❌ APIs non implémentées supprimées (Hunter.io, Clearbit)
- ✅ Sources réelles avec documentation (INSEE, Pappers, Société.com, DNS/WHOIS)

**Slides HTML (AFAC)** :
- ✅ `episode2-slide1.html` : Ports supprimés, métriques corrigées
- ✅ `episode2-slide2.html` : Références APIs non implémentées supprimées
- ✅ `episode2-slide3.html` : Hit rate corrigé, sources réelles
- ✅ `episode2-slide9.html` : Créée avec métriques réelles

### 📊 KPIs cibles

- Impressions : 1000+
- Engagement : 80+
- Taux completion carousel : 60%+
- Clics CTA : 50+
- Visites site : 100+
- Commentaires : 15+

### 🎯 Prochaines étapes

1. **Claude** : Créer les 9 infographies selon prompts fournis dans `PROMPTS_INFOGRAFIES_CLAUDE.md`
2. **Validation sécurité** : Exécuter `validate-campaign.sh`
3. **Review finale** : Vérifier tous les éléments (texte, visuels, métriques réelles)
4. **Planification MCP** :
   - Créer événement Google Calendar (date publication)
   - Organiser dossier Drive pour assets
   - Template Notion pour tracking KPIs
5. **Publication** : 2025-11-15 10:00 UTC (modifiable)

### 🔗 Références

- **Campagne** : `squidCommunication/campaigns/2025-11-episode-2-dockerisation-enriched/`
- **Post** : `linkedin/post-01-dockerisation-enriched.md`
- **Prompts infographies** : `PROMPTS_INFOGRAFIES_CLAUDE.md` (prompts détaillés pour les 9 slides)
- **Avertissement métriques** : `AVERTISSEMENT_METRIQUES.md` (⚠️ CRITIQUE - métriques réelles uniquement)
- **Charte BOGOSS** : Couleurs et gradients définis dans les prompts
- **Architecture technique** : `squidResearch/docker-compose.yml`
- **Module Enriched** : `squidResearch/apps/scrapper/enriched/`
- **Slides HTML** : `squidCommunication/AFAC/episode2-slide*.html` (9 slides corrigées)


---

## 🔗 Liens Croisés

- **Repo principal** : `../squidResearch/`
- **Log source** : `../squidResearch/communication_projet.md`
- **Base de connaissance** : `../squidResearch/private/{IDEAS,ROADMAP}.md`
- **Documentation IP** : `../squidResearch/docs/legal/IP_*.md`

**Pour modifier** : Éditer `squidResearch/communication_projet.md` puis relancer la sync.
