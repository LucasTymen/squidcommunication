# 🚀 Guide Rapide n8n - Publication Articles

**Serveur n8n utilisé** : Serveur n8n de SquidResearch (existant)  
**Pour utilisation avec prod instable : Déploiement manuel (copier-coller)**

---

## 📋 Étape 1 : Préparer le Workflow Local

Les workflows sont versionnés dans `workflows/n8n/` :

- `publish_article_simple.json` : Workflow simple pour LinkedIn (à étendre)
- `publish_article_social.json` : Workflow complet multi-plateformes

---

## 🔑 Étape 2 : Créer les Credentials dans n8n

### LinkedIn

1. **Créer une app LinkedIn** : https://www.linkedin.com/developers/apps
2. **OAuth 2.0 Settings** :
   - Redirect URLs : `[URL_N8N_SQUIDRESEARCH]/rest/oauth2-credential/callback` (ex: `http://localhost:5678/rest/oauth2-credential/callback`)
   - Scopes : `w_member_social` (pour poster)
3. **Dans n8n** :
   - Credentials → Add Credential → LinkedIn OAuth2 API
   - Client ID : [votre Client ID]
   - Client Secret : [votre Client Secret]
   - Nom : `LinkedIn OAuth2 API`
   - Cliquer sur "Connect my account" pour autoriser

### Facebook / Instagram / Threads

Ces plateformes utilisent Meta Graph API. Configuration similaire via https://developers.facebook.com/apps

---

## 📥 Étape 3 : Importer le Workflow dans n8n

### Option A : Import depuis fichier (Recommandé)

1. Ouvrir n8n : [URL du serveur n8n SquidResearch] (généralement http://localhost:5678 ou URL configurée dans SquidResearch)
2. **Workflows** → **Import from File**
3. Sélectionner : `workflows/n8n/publish_article_simple.json`
4. Le workflow s'importe automatiquement

### Option B : Copier-Coller (Si import ne fonctionne pas)

1. Ouvrir n8n : [URL du serveur n8n SquidResearch] (généralement http://localhost:5678 ou URL configurée dans SquidResearch)
2. **Workflows** → **+ New Workflow**
3. Cliquer sur **...** (menu) → **Import from JSON**
4. Copier le contenu de `workflows/n8n/publish_article_simple.json`
5. Coller dans le champ JSON

---

## ⚙️ Étape 4 : Configurer le Workflow

1. **Webhook** : Notez l'URL (ex: `http://localhost:5679/webhook/publish-article`)
2. **Read Post File** : Vérifier le chemin `/home/lucas/tools/squidCommunication/articles/...`
3. **LinkedIn Post** :
   - Cliquer sur le nœud
   - Credential → Sélectionner "LinkedIn OAuth2 API"
   - Si besoin, reconnecter pour autoriser à nouveau

---

## 🧪 Étape 5 : Tester le Workflow

### Activer le workflow

Toggle "Active" en haut à droite du workflow

### Tester avec curl

```bash
curl -X POST [URL_N8N_SQUIDRESEARCH]/webhook/publish-article \
  -H "Content-Type: application/json" \
  -d '{
    "article_slug": "article-3-algorithmes-matching-intelligents",
    "platform": "linkedin"
  }'
```

### Ou utiliser "Execute Workflow" dans n8n

1. Cliquer sur "Execute Workflow"
2. Entrer les données :
```json
{
  "article_slug": "article-3-algorithmes-matching-intelligents",
  "platform": "linkedin"
}
```

---

## 📝 Workflow Simple : Structure

```
Webhook → Read Post File → Extract Post Text → LinkedIn Post → Respond
```

**Input** :
```json
{
  "article_slug": "article-3-algorithmes-matching-intelligents",
  "platform": "linkedin"
}
```

**Output** :
```json
{
  "success": true,
  "article_slug": "article-3-algorithmes-matching-intelligents",
  "platform": "linkedin",
  "published_at": "2026-01-05T10:00:00.000Z"
}
```

---

## 🔄 Workflow Complet Multi-Plateformes

Pour publier sur plusieurs plateformes, utiliser `publish_article_social.json` qui inclut :

- LinkedIn
- Facebook  
- Threads
- Instagram

Même processus d'import et configuration des credentials pour chaque plateforme.

---

## ⚠️ Notes Importantes

1. **Credentials OAuth2** : Doivent être créées dans n8n (pas dans le JSON)
2. **Chemins locaux** : Les workflows lisent depuis `/home/lucas/tools/squidCommunication`
3. **Production instable** : Préférer import manuel (copier-coller) pour l'instant
4. **Test local d'abord** : Toujours tester en local avant de déployer en prod

---

## 📚 Références

- Documentation n8n : https://docs.n8n.io
- LinkedIn API : https://docs.microsoft.com/en-us/linkedin/
- Guide détaillé : `docs/N8N_WORKFLOWS_SETUP.md`

