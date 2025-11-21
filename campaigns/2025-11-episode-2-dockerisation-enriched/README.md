# 🎬 Épisode 2 : Architecture Docker & Module Enriched

> Campagne LinkedIn Carousel - 9 slides  
> Date prévue : 2025-11-15 10:00 UTC

## 📋 Vue d'ensemble

**Objectif** : Démontrer l'architecture Docker de SquidResearch et les capacités du module Enriched pour l'enrichissement intelligent de données B2B.

**Format** : Post LinkedIn Carousel (9 slides)

**Approche** : **VRAIMENT data-driven** - Uniquement métriques réelles vérifiables (voir `AVERTISSEMENT_METRIQUES.md`)

---

## 📁 Structure de la campagne

```
2025-11-episode-2-dockerisation-enriched/
├── campaign.json                    # Configuration complète
├── linkedin/
│   └── post-01-dockerisation-enriched.md  # Post avec prompts infographies
├── assets/
│   ├── original/                    # Assets bruts (gitignored)
│   └── sanitized/                   # Assets prêts pour publication
│       ├── post-01-slide-01-architecture-overview.png
│       ├── post-01-slide-02-probleme.png
│       ├── post-01-slide-03-module-enriched.png
│       ├── post-01-slide-04-principes-fonctionnement.png
│       ├── post-01-slide-05-services-detaille.png
│       ├── post-01-slide-06-flux-donnees.png
│       ├── post-01-slide-07-reseaux-mappages.png
│       ├── post-01-slide-08-volumes-mappages.png
│       └── post-01-slide-09-resultats-cta.png
├── archive/                         # Analytics et exports après publication
└── README.md                         # Ce fichier
```

---

## 🎨 Charte graphique BOGOSS

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

### Style
- Moderne, épuré
- Ombres douces et rayons arrondis
- Typographie bold, hiérarchie claire
- Effet "whaou" recherché

---

## 🖼️ Création des infographies

### Instructions pour Claude

1. **⚠️ LIRE EN PREMIER** : `AVERTISSEMENT_METRIQUES.md` - **CRITIQUE** : Aucun chiffre inventé
2. **Lire les prompts** dans `PROMPTS_INFOGRAFIES_CLAUDE.md`
3. **Créer chaque infographie** selon les spécifications
4. **Respecter la charte BOGOSS** (couleurs, gradients, style)
5. **Format** : PNG 1080x1080px, 300 DPI
6. **Sauvegarder** dans `assets/sanitized/`
7. **⚠️ VÉRIFIER** : Toutes les métriques sont réelles et vérifiables

### Slides à créer

| Slide | Fichier | Description |
|-------|---------|-------------|
| 1 | `post-01-slide-01-architecture-overview.png` | Vue d'ensemble architecture Docker |
| 2 | `post-01-slide-02-probleme.png` | Problèmes enrichissement B2B |
| 3 | `post-01-slide-03-module-enriched.png` | Module Enriched solution |
| 4 | `post-01-slide-04-principes-fonctionnement.png` | Principes de fonctionnement détaillés |
| 5 | `post-01-slide-05-services-detaille.png` | Services Docker détaillés |
| 6 | `post-01-slide-06-flux-donnees.png` | Flux de données Enriched |
| 7 | `post-01-slide-07-reseaux-mappages.png` | Réseaux, APIs & Webhooks |
| 8 | `post-01-slide-08-volumes-mappages.png` | Volumes & Mappages Docker |
| 9 | `post-01-slide-09-resultats-cta.png` | Résultats & CTA |

---

## ✅ Checklist avant publication

### Contenu
- [ ] Texte du post finalisé
- [ ] Tous les slides rédigés
- [ ] Hashtags vérifiés
- [ ] CTA clair et actionnable

### Visuels
- [ ] 9 infographies créées par Claude
- [ ] Format 1080x1080px respecté
- [ ] Charte BOGOSS appliquée
- [ ] Qualité optimale (300 DPI)

### Sécurité
- [ ] Aucune IP visible
- [ ] Credentials masqués
- [ ] Pas de tokens/API keys
- [ ] Données anonymisées
- [ ] URLs internes remplacées
- [ ] Script `validate-campaign.sh` exécuté

### MCP Actions (Claude)
- [ ] Événement Google Calendar créé
- [ ] Dossier Drive organisé pour assets
- [ ] Template Notion pour tracking KPIs
- [ ] Infographies créées et validées

---

## 📊 KPIs cibles

| Métrique | Cible |
|----------|-------|
| Impressions | 1000+ |
| Engagement | 80+ |
| Taux completion carousel | 60%+ |
| Clics CTA | 50+ |
| Visites site | 100+ |
| Commentaires | 15+ |

---

## 🚀 Workflow de publication

1. **Création infographies** : Claude génère les 9 slides selon prompts
2. **Validation sécurité** : Exécuter `validate-campaign.sh`
3. **Review finale** : Vérifier tous les éléments
4. **Planification** : Créer événement GCal (Claude)
5. **Publication** : Poster sur LinkedIn à la date prévue
6. **Suivi** : Remplir analytics dans `archive/analytics.json`

---

## 📝 Notes importantes

### Terminologie
- ✅ **Utiliser** : "Module Enriched", "Enrichissement intelligent", "Intelligence enrichie"
- ❌ **Éviter** : "Kali", "OSINT", termes techniques sensibles

### Approche
- **Data-driven** : Métriques et chiffres concrets
- **Technique mais accessible** : Expliquer sans jargon excessif
- **Effet "whaou"** : Infographies impactantes, design moderne

### Références techniques
- Architecture : `squidResearch/docker-compose.yml`
- Module Enriched : `squidResearch/apps/scrapper/enriched/`
- Documentation : `squidResearch/docs/TECHNICAL.md`
- **Benchmarks réels** : `squidResearch/docs/archive/2025-10/BENCHMARK_RESULTS.md`
- **⚠️ Avertissement métriques** : `AVERTISSEMENT_METRIQUES.md` (à lire en premier)

---

## 🔗 Liens utiles

- **Log communication** : `squidResearch/communication_projet.md`
- **Templates** : `squidCommunication/templates/`
- **Scripts** : `squidCommunication/scripts/`
- **Documentation collaboration** : `squidCommunication/docs/collaboration-cursor-claude.md`

---

## 📅 Timeline

- **Création campagne** : 2025-11-13
- **Création infographies** : À faire (Claude)
- **Validation sécurité** : À faire
- **Publication prévue** : 2025-11-15 10:00 UTC
- **Suivi analytics** : Après publication

---

**Status** : 📋 Draft - En attente création infographies

