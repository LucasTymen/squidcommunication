# Article 6 : Enrichissement Multi-Sources & Tor

> **Épisode 6** de la série SquidResearch  
> **Thème** : Anonymat et protection anti-ban  
> **Format** : Présentation Gamma (7 slides)

## 📋 Contenu

- **GAMMA_PRESENTATION.md** : Présentation complète pour Gamma
- **Presentation/** : Slides HTML (à générer)
- **linkedin/** : Posts LinkedIn (à créer)
- **assets/** : Assets visuels (à créer)

## 🎯 Objectifs

- Expliquer la protection anti-ban avec Tor
- Démontrer l'humanisation comportementale
- Montrer les résultats de performance

## 📊 Métriques clés

- Tor : 5-8s par requête
- Rate limiting : Max 10-12 req/min
- Whitelist : Sites compatibles Tor
- Blacklist : Sites bloquant Tor
- 0 ban depuis implémentation

## 🔗 Références

- `apps/scrapper/config/tor_config.py`
- `apps/scrapper/enriched/tools/secure_session.py`
- `squidresearch/settings.py` (TOR_WHITELIST, TOR_BLACKLIST)

