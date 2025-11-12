# 📋 Workflow Complet - SquidCommunication

## Vue d'ensemble

Ce document décrit le workflow complet pour créer, valider et publier une campagne de communication SquidResearch.

## 🚀 Phase 1 : Création de la campagne

### 1.1 Créer la structure

```bash
cd squidCommunication/scripts
./create-campaign.sh "feature-matching" linkedin instagram
```

Cela crée :
- `campaigns/2025-11-feature-matching/`
- `campaign.json` pré-rempli
- Dossiers par plateforme
- Templates Markdown copiés
- README de campagne

### 1.2 Définir les objectifs

Éditer `campaigns/<id>/campaign.json` :

```json
{
  "objective": "Faire connaître l'algorithme de matching intelligent",
  "message_key": "SquidResearch = gain de temps pour recruteurs",
  "kpis": {
    "target": {
      "linkedin_impressions": 500,
      "linkedin_engagement": 30
    }
  }
}
```

### 1.3 Planifier avec Claude (MCP)

Utiliser Claude pour :
- Créer un événement Google Calendar
- Organiser un dossier Drive
- Générer un template Notion pour tracking
- Préparer des templates Canvas pour visuels

Noter les IDs dans `campaign.json` :

```json
{
  "mcp_collaboration": {
    "calendar_event_id": "abc123xyz",
    "drive_folder": "https://drive.google.com/...",
    "notion_template": "https://notion.so/..."
  }
}
```

## ✍️ Phase 2 : Création de contenu

### 2.1 Rédiger les posts

Pour chaque plateforme :

```bash
# LinkedIn
vim campaigns/<id>/linkedin/post-1.md

# Instagram
vim campaigns/<id>/instagram/story-1.md
```

Suivre les **guidelines éditoriales** (`templates/editorial-guidelines.md`) :

- **Ton** : Professionnel mais accessible
- **Structure LinkedIn** : 3-5 paragraphes courts
- **Structure Instagram** : Texte court (10-15 mots)
- **Hashtags** : 3-5 LinkedIn, 5-10 Instagram

### 2.2 Créer les assets visuels

1. **Captures d'écran** :
   - Capturer les écrans pertinents
   - Placer dans `assets/original/`

2. **Designs graphiques** :
   - Utiliser Canvas / Figma
   - Export PNG/JPG haute résolution
   - Placer dans `assets/original/`

3. **Vidéos** (optionnel) :
   - Max 2 min
   - Sous-titres obligatoires
   - Format MP4

### 2.3 Anonymiser les assets

Pour chaque asset dans `original/` :

1. Ouvrir avec éditeur d'image
2. **Flouter** :
   - Chemins complets (`/home/user/...`)
   - IPs (`192.168.*.*`)
   - Credentials
   - Données clients
3. Enregistrer dans `assets/sanitized/`

**Exemple de masquage** :
- IP : `192.168.1.10` → `192.***.***.***`
- Credential : `password123` → `pa****rd`
- Chemin : `/home/lucas/tools/` → `/workspace/`

## 🔒 Phase 3 : Validation sécurité

### 3.1 Validation automatique

```bash
./scripts/validate-campaign.sh campaigns/2025-11-feature-matching
```

Le script vérifie :
- ✅ Aucun credential/token/API key
- ✅ Aucune IP privée non masquée
- ✅ Structure campagne complète
- ✅ Assets sanitized présents

### 3.2 Correction des erreurs

Si des erreurs sont détectées :

```bash
❌ ERREUR: token trouvé dans campaigns/.../linkedin/post-1.md
```

1. Ouvrir le fichier concerné
2. Remplacer/supprimer la donnée sensible
3. Re-exécuter le script de validation

### 3.3 Validation manuelle

Checklist finale :

- [ ] Relire tous les posts (typos, ton)
- [ ] Vérifier tous les assets (qualité, contenu)
- [ ] Tester tous les liens (URLs, CTAs)
- [ ] Valider les hashtags (pertinence)
- [ ] Double-check sécurité (aucune fuite)

### 3.4 Marquer comme validé

Dans `campaign.json` :

```json
{
  "security_checklist": {
    "no_ip_visible": true,
    "credentials_masked": true,
    "no_tokens": true,
    "client_data_anonymized": true,
    "internal_urls_masked": true,
    "env_vars_hidden": true,
    "validation_script_run": true,
    "validated_by": "Lucas",
    "validated_at": "2025-11-12T17:00:00Z"
  }
}
```

## 📅 Phase 4 : Planification

### 4.1 Définir les dates de publication

Dans `campaign.json` :

```json
{
  "posts": [
    {
      "platform": "linkedin",
      "type": "post",
      "status": "scheduled",
      "scheduled_date": "2025-11-15T10:00:00Z",
      "title": "Feature matching intelligent",
      "file": "linkedin/post-1.md"
    }
  ]
}
```

### 4.2 Synchroniser avec calendrier

Utiliser Claude (MCP) pour :
- Créer événements dans Google Calendar
- Ajouter rappels (24h avant, 1h avant)
- Lier les assets depuis Drive

### 4.3 Préparer les publications

- Copier le contenu des .md dans un document de travail
- Préparer les assets sur le desktop
- Tester les uploads (LinkedIn/Instagram)

## 🚀 Phase 5 : Publication

### 5.1 Publier selon le planning

Pour chaque post :

1. **LinkedIn** :
   - Coller le texte depuis `linkedin/post-1.md`
   - Ajouter l'image/vidéo depuis `assets/sanitized/`
   - Vérifier la preview
   - Publier

2. **Instagram** :
   - Depuis mobile : ajouter l'image depuis `assets/sanitized/`
   - Coller le texte depuis `instagram/story-1.md`
   - Ajouter stickers (lien, hashtag, sondage)
   - Publier story

### 5.2 Archiver les posts publiés

Pour chaque post publié :

1. Prendre capture d'écran du post final
2. Sauvegarder dans `archive/`
3. Noter l'URL du post dans `campaign.json`

```json
{
  "posts": [
    {
      "platform": "linkedin",
      "status": "published",
      "published_date": "2025-11-15T10:05:00Z",
      "url": "https://linkedin.com/posts/...",
      "archive_screenshot": "archive/linkedin-post-1.png"
    }
  ]
}
```

## 📊 Phase 6 : Analytics & Suivi

### 6.1 Collecter les métriques

**LinkedIn** (après 24h, 7j, 30j) :
- Impressions
- Clics
- Likes
- Commentaires
- Partages
- Visites profil

**Instagram** (après 24h, 7j) :
- Vues stories
- Réponses
- Clics lien
- Partages
- Nouveaux followers

### 6.2 Enregistrer dans analytics.json

Créer `archive/analytics.json` :

```json
{
  "campaign_id": "2025-11-feature-matching",
  "collected_at": "2025-11-16T10:00:00Z",
  "platforms": {
    "linkedin": {
      "post_url": "https://linkedin.com/posts/...",
      "impressions": 543,
      "engagement": 34,
      "clicks": 18,
      "likes": 28,
      "comments": 6,
      "shares": 2
    },
    "instagram": {
      "story_views": 210,
      "responses": 12,
      "link_clicks": 15,
      "shares": 5
    }
  },
  "totals": {
    "total_reach": 753,
    "total_engagement": 97,
    "engagement_rate": 12.9
  }
}
```

### 6.3 Mettre à jour campaign.json

Remplir la section `kpis.actual` :

```json
{
  "kpis": {
    "target": {
      "linkedin_impressions": 500
    },
    "actual": {
      "linkedin_impressions": 543
    }
  }
}
```

### 6.4 Logger dans communication_projet.md

Ajouter une entrée dans `squidResearch/communication_projet.md` :

```markdown
## [2025-11-16 10:00] Campagne "Feature Matching" - Résultats

- **Statut** : ✅ Publiée + Analytics collectées
- **Performance** :
  - LinkedIn : 543 impressions (objectif : 500) ✅
  - Engagement : 34 (objectif : 30) ✅
  - Taux engagement : 6.3%
- **Learnings** :
  - Format "pédagogique" > format "meta"
  - Publication 10h = meilleur reach
  - Vidéos > images statiques
- **Actions** :
  - Reproduire format pédagogique pour prochaine campagne
  - Privilégier vidéos courtes (<60s)
```

## 🔄 Phase 7 : Apprentissage & Optimisation

### 7.1 Analyser les résultats

Questions à se poser :
- Quels posts ont le mieux performé ? Pourquoi ?
- Quel format (texte seul, image, vidéo) marche le mieux ?
- Quel horaire de publication est optimal ?
- Quels hashtags ont généré le plus d'engagement ?

### 7.2 Mettre à jour les guidelines

Si un pattern émerge, mettre à jour `templates/editorial-guidelines.md` :

```markdown
### Learnings (2025-11-16)
- Posts pédagogiques (how-to) : +40% engagement vs posts "meta"
- Horaire optimal LinkedIn : 10h-11h (jours de semaine)
- Format préféré : Carrousel 5-7 slides > image unique
```

### 7.3 Planifier la prochaine campagne

Utiliser les learnings :
- Reproduire ce qui a marché
- Tester de nouvelles hypothèses (A/B testing)
- Ajuster les KPIs selon les résultats précédents

## 🛠️ Outils & Ressources

### Scripts disponibles

```bash
# Créer une campagne
./scripts/create-campaign.sh <slug> <platforms...>

# Valider la sécurité
./scripts/validate-campaign.sh campaigns/<id>
```

### Templates disponibles

- `templates/linkedin-post.md` : Structure post LinkedIn
- `templates/instagram-story.md` : Structure story Instagram
- `templates/campaign-brief.md` : Brief complet de campagne
- `templates/editorial-guidelines.md` : Charte éditoriale

### MCP (Claude)

Claude peut aider à :
- Planifier (GCal, Drive, Notion)
- Générer du contenu (drafts, variantes)
- Créer des visuels (templates Canvas)
- Déployer (push Vercel pour landing page)

## ❓ FAQ

### Comment gérer plusieurs versions d'un post ?

Créer plusieurs fichiers :
- `linkedin/post-1-version-meta.md`
- `linkedin/post-1-version-pedagogique.md`

Tester les 2 (différents jours ou A/B test).

### Puis-je réutiliser des assets d'une campagne à l'autre ?

Oui ! Créer un dossier `assets/shared/` à la racine :
```
squidCommunication/assets/shared/
├── logo.png
├── brand-colors.png
└── screenshots/
```

### Comment gérer les campagnes multi-langues ?

Créer des sous-dossiers par langue :
```
campaigns/2025-11-feature/
├── en/
│   ├── linkedin/
│   └── instagram/
└── fr/
    ├── linkedin/
    └── instagram/
```

### Que faire si la validation échoue juste avant publication ?

1. Ne PAS publier
2. Corriger les erreurs détectées
3. Re-valider
4. Décaler la publication si nécessaire

La sécurité est prioritaire sur le planning.

---

**Dernière mise à jour** : 2025-11-12
**Version** : 1.0
