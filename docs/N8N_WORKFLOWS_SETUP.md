# 🔄 Configuration Workflows n8n - SquidCommunication

**Dernière mise à jour** : 2026-01-05  
**Objectif** : Publier automatiquement les articles sur les réseaux sociaux via n8n  
**Serveur n8n** : Utilisation du serveur n8n existant de SquidResearch

---

## 📋 Workflows Disponibles

### 1. Publish Article to Social Media

**Fichier** : `workflows/n8n/publish_article_social.json`

**Description** : Publie un article sur une plateforme sociale (LinkedIn, Facebook, Threads, Instagram)

**Usage** :
```bash
# Option 1 : Import manuel dans n8n (recommandé pour prod instable)
# Voir section "Déploiement Manuel" ci-dessous

# Option 2 : Déployer via script (si n8n API accessible)
python scripts/deploy_n8n_workflows.py workflows/n8n/publish_article_social.json

# Appeler le workflow via webhook (après activation dans n8n)
curl -X POST [URL_N8N_SQUIDRESEARCH]/webhook/publish-article \
  -H "Content-Type: application/json" \
  -d '{"article_slug": "article-3-algorithmes-matching-intelligents", "platform": "linkedin"}'
```

---

## 🔑 Création des Credentials dans n8n

### LinkedIn

1. **Créer une app LinkedIn** : https://www.linkedin.com/developers/apps
2. **Configurer OAuth 2.0** :
   - Redirect URLs : `[URL_N8N_SQUIDRESEARCH]/rest/oauth2-credential/callback`
   - Scopes requis : `w_member_social` (pour poster)
3. **Dans n8n** :
   - Credentials → OAuth2 API → LinkedIn OAuth2 API
   - Client ID : [votre Client ID]
   - Client Secret : [votre Client Secret]
   - Nom : `LinkedIn OAuth2 API`

### Facebook

1. **Créer une app Facebook** : https://developers.facebook.com/apps
2. **Configurer Facebook Login** :
   - Redirect URLs : `[URL_N8N_SQUIDRESEARCH]/rest/oauth2-credential/callback`
   - Scopes requis : `pages_manage_posts`, `pages_read_engagement`
3. **Dans n8n** :
   - Credentials → OAuth2 API → Facebook Graph API
   - Client ID : [votre App ID]
   - Client Secret : [votre App Secret]
   - Nom : `Facebook Graph API`

### Threads (Meta)

1. **Utiliser l'app Facebook** (Threads utilise Meta)
2. **Dans n8n** :
   - Credentials → OAuth2 API → Meta Threads OAuth2 API
   - Mêmes credentials que Facebook
   - Nom : `Meta Threads OAuth2 API`

### Instagram

1. **Utiliser l'app Facebook** (Instagram utilise Meta Graph API)
2. **Configurer Instagram Basic Display** :
   - Redirect URLs : `[URL_N8N_SQUIDRESEARCH]/rest/oauth2-credential/callback`
   - Scopes requis : `instagram_basic`, `instagram_content_publish`
3. **Dans n8n** :
   - Credentials → OAuth2 API → Instagram Basic Display OAuth2 API
   - Mêmes credentials que Facebook
   - Nom : `Instagram Basic Display OAuth2 API`

---

## 🚀 Déploiement Manuel (Copier-Coller)

Comme la prod n8n est instable, voici comment déployer manuellement :

### Étape 1 : Exporter le Workflow Local

```bash
# Le workflow est déjà dans workflows/n8n/publish_article_social.json
cat workflows/n8n/publish_article_social.json
```

### Étape 2 : Importer dans n8n

1. Ouvrir n8n SquidResearch : [URL du serveur n8n] (vérifier dans la config SquidResearch)
2. Aller dans **Workflows** → **Import from File**
3. Sélectionner `workflows/n8n/publish_article_social.json`
4. Le workflow s'importe avec tous les nœuds

### Étape 3 : Configurer les Credentials

1. Pour chaque nœud de publication (LinkedIn, Facebook, etc.) :
   - Cliquer sur le nœud
   - Dans "Credential for [Platform]", sélectionner ou créer la credential
   - Suivre le flux OAuth2 pour autoriser

### Étape 4 : Tester le Workflow

1. Activer le workflow (toggle en haut à droite)
2. Cliquer sur "Execute Workflow" ou utiliser le webhook
3. Vérifier les logs dans n8n

---

## 📝 Script de Génération de Workflow Personnalisé

Pour générer un workflow avec les données d'un article spécifique :

```python
# scripts/generate_n8n_workflow.py
# À créer si nécessaire pour personnaliser les workflows
```

---

## 🔍 Workflow Détaillé : Publish Article to Social Media

### Nodes

1. **Webhook Trigger** : Reçoit `{article_slug, platform}`
2. **Validate Input** : Valide les paramètres
3. **Read Post Content** : Lit le fichier `platforms/<platform>/post-01.md`
4. **Parse Content** : Extrait le texte du post depuis le Markdown
5. **Check Platform: [Platform]** : Route vers la bonne plateforme
6. **Post to [Platform]** : Publie sur la plateforme
7. **Update Publication Log** : Met à jour `PUBLICATION_LOG.md`
8. **Webhook Response** : Retourne le résultat

### Paramètres d'Entrée

```json
{
  "article_slug": "article-3-algorithmes-matching-intelligents",
  "platform": "linkedin"
}
```

### Réponse

```json
{
  "success": true,
  "article_slug": "article-3-algorithmes-matching-intelligents",
  "platform": "linkedin",
  "published_at": "2026-01-05T10:00:00.000Z"
}
```

---

## ⚠️ Notes Importantes

1. **Credentials OAuth2** : Doivent être créées dans n8n (pas dans le JSON)
2. **Chemins locaux** : Le workflow lit depuis `/home/lucas/tools/squidCommunication`
3. **Webhook URL** : `http://localhost:5679/webhook/publish-article` (si workflow activé)
4. **Logs** : Le workflow met à jour automatiquement `PUBLICATION_LOG.md`
5. **Production instable** : Préférer déploiement manuel (copier-coller) pour l'instant

---

## 🔄 Workflow Alternatif : Publication Multi-Plateformes

Pour publier sur plusieurs plateformes en une fois :

```json
{
  "article_slug": "article-3-algorithmes-matching-intelligents",
  "platforms": ["linkedin", "facebook", "threads", "instagram"]
}
```

**Workflow à créer** : `workflows/n8n/publish_article_multi_platform.json` (à venir)

---

## 📚 Références

- Documentation n8n : https://docs.n8n.io
- LinkedIn API : https://docs.microsoft.com/en-us/linkedin/
- Facebook Graph API : https://developers.facebook.com/docs/graph-api
- Meta Threads API : https://developers.facebook.com/docs/threads
- Instagram Basic Display API : https://developers.facebook.com/docs/instagram-basic-display-api

