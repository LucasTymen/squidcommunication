# ⚠️ AVERTISSEMENT CRITIQUE - MÉTRIQUES RÉELLES UNIQUEMENT

## 🚨 RÈGLE ABSOLUE

**AUCUN CHIFFRE INVENTÉ - UNIQUEMENT DES DONNÉES RÉELLES VÉRIFIABLES**

Les slides AFAC contenaient des métriques **hallucinées** (inventées). Nous devons corriger cela pour une approche **vraiment data-driven**.

---

## ❌ À ÉVITER (Métriques inventées)

### Chiffres NON vérifiés à NE PAS utiliser :
- ❌ "+2M entreprises indexées" → **FAUX** (aucune donnée réelle)
- ❌ "85%+ hit rate" → **NON MESURÉ** (cache existe mais pas de métriques production)
- ❌ "~500 req/min" → **NON MESURÉ** (rate limiters configurés mais pas de stats)
- ❌ "500K+ enrichissements effectués" → **NON VÉRIFIÉ**
- ❌ "10+ workers parallèles" → **CONFIGURABLE** mais nombre réel non vérifié
- ❌ "Hunter.io, Clearbit" → **NON INTÉGRÉS** (TODOs dans le code)

---

## ✅ À UTILISER (Métriques réelles vérifiables)

### Benchmarks réels mesurés (docs/archive/2025-10/BENCHMARK_RESULTS.md) :
- Cache hit : < 0.1s (mesuré) - **SEULEMENT si cache hit**
- Gain cache : 98x plus rapide (benchmark réel : scénario 100 contacts)
- Cache WHOIS : 0.778s → 0.000s (5,703x plus rapide) - **si cache hit**
- Cache DNS : 2.153s → 0.000s (19,509x plus rapide) - **si cache hit**
- Enrichissement E2E : 0.057s (cache froid), 0.046s (cache chaud) - **sans Tor**

**Performance RÉELLE avec Tor + humanisation** (HUMAN_BEHAVIOR_CONFIG.md) :
- ⚠️ Delay moyen : **6.5s** (5-8s gaussien) entre requêtes
- ⚠️ Max requêtes/min : **10-12** (rate limiting humanisé)
- ⚠️ Avec Tor : **BEAUCOUP PLUS LENT** que les benchmarks optimaux
- ✅ Cache hit : < 0.1s (mais seulement si données déjà en cache)

**Architecture réelle** :
- ✅ **9 services Docker** (vérifié dans docker-compose.yml)
- ✅ Réseau : **squidresearch_network** (isolé)
- ✅ Volumes : **postgres_data, redis_data, n8n_data, flowise_data**

**Sources réellement implémentées avec APIs documentées** :
- ✅ **INSEE Sirene** : API officielle gratuite, documentation : https://api.insee.fr/catalogue/
- ✅ **Pappers** : API officielle, documentation : https://www.pappers.fr/api/documentation/v1
- ✅ **Entreprise.data.gouv.fr** : API officielle
- ✅ **Société.com** : Scraper fonctionnel
- ✅ **DNS/WHOIS** : Outils Python (dnspython, python-whois)

**Endpoints APIs réels** :
- `/api/enriched/` - Enrichissement
- `/companies/search/` - Recherche entreprises
- `/webhooks/` - Webhooks
- `/api/n8n/webhooks/` - Webhooks n8n

---

## 📝 Formulations recommandées

### Au lieu de métriques inventées, utiliser :

| ❌ Inventé | ✅ Réalité |
|------------|------------|
| "+2M entreprises indexées" | "Architecture scalable pour millions d'entreprises" |
| "85%+ hit rate" | "Cache Redis avec TTL intelligent (hit rate cible : 85%+)" |
| "~500 req/min" | "Rate limiting : max 10-12 req/min (humanisation)" |
| "500K+ enrichissements" | "Architecture testée et prête pour production" |
| "10+ workers parallèles" | "Workers Celery configurables (scalable horizontalement)" |
| "Hunter.io, Clearbit" | "Sources : INSEE (API gratuite), Pappers (API doc)" |
| "< 5s par entreprise" | "Cache hit : < 0.1s (si hit) | Avec Tor : 5-8s/requête" |
| "10+ sources simultanées" | "Max 10-12 req/min (rate limiting humanisé)" |

---

## 🎯 Principe : "Capacité" vs "Réalité mesurée"

### Formulations de capacité (OK) :
- "Architecture prête pour..."
- "Scalable à..."
- "Capable de traiter..."
- "Optimisé pour..."

### Formulations de réalité mesurée (OK) :
- "Mesuré : X secondes"
- "Benchmark réel : X"
- "Testé sur : X"
- "Gain mesuré : Xx"

### Formulations à éviter (NON) :
- "X millions de..." (sans preuve)
- "X% de..." (sans mesure)
- "X requêtes/min" (sans monitoring)

---

## 📊 Références pour métriques réelles

1. **Benchmarks** : `docs/archive/2025-10/BENCHMARK_RESULTS.md`
2. **Architecture** : `docker-compose.yml`
3. **Sources** : `apps/scrapper/enriched/`
4. **Tests** : `apps/scrapper/enriched/tests/`

---

## ✅ Checklist avant création infographie

- [ ] Tous les chiffres sont vérifiables dans le code/docs
- [ ] Aucune métrique inventée
- [ ] Sources mentionnées sont réellement implémentées avec APIs documentées
- [ ] Formulations utilisent "capacité" ou "mesuré"
- [ ] Références aux benchmarks réels si métriques de performance
- [ ] ⚠️ Performance avec contexte : mentionner Tor/humanisation si applicable
- [ ] ⚠️ Cache hit : préciser "seulement si cache hit"
- [ ] ⚠️ Ports Docker : NE PAS afficher (sécurité)
- [ ] ⚠️ APIs : Utiliser uniquement celles avec documentation officielle
- [ ] ⚠️ Schémas dynamiques : Flèches pointillées pour flux, détails techniques

---

**Rappel** : L'objectif est un effet "whaou" basé sur la **réalité technique**, pas sur des chiffres inventés. L'architecture est solide, montrons-la telle qu'elle est !

