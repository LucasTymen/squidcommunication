# 🔗 Intégration avec n8n SquidResearch

**Dernière mise à jour** : 2026-01-05  
**Objectif** : Utiliser le serveur n8n existant de SquidResearch pour publier les articles

---

## ✅ Avantages d'utiliser le serveur n8n SquidResearch

- ✅ Pas besoin de créer un nouveau serveur
- ✅ Credentials déjà configurées (si existantes)
- ✅ Infrastructure existante et maintenue
- ✅ Accès centralisé aux workflows

---

## 🔍 Configuration du serveur n8n SquidResearch

D'après la configuration SquidResearch (`docker-compose.yml`) :

- **Port** : 5678 (port par défaut n8n)
- **Container** : `n8n` (production) ou `n8n_dev` (développement)
- **URL locale** : `http://localhost:5678`
- **URL interne Docker** : `http://n8n:5678` (depuis autres conteneurs)

Pour vérifier si n8n est en cours d'exécution :

```bash
cd /home/lucas/tools/squidResearch
docker-compose ps n8n
# ou
docker ps | grep n8n
```

---

## 📝 Adapter les Workflows

Les workflows dans `workflows/n8n/` sont conçus pour être utilisés avec n8n. Ils doivent simplement être importés dans le serveur n8n SquidResearch.

### Chemins dans les workflows

Les workflows utilisent des chemins absolus pour lire les fichiers :

```bash
/home/lucas/tools/squidCommunication/articles/<article-slug>/platforms/<platform>/post-01.md
```

**Important** : Ces chemins doivent être accessibles depuis le conteneur/serveur n8n. Options :

1. **Volume Docker** : Monter `/home/lucas/tools/squidCommunication` dans le conteneur n8n
2. **Chemins partagés** : Utiliser un chemin partagé accessible depuis n8n
3. **Script intermédiaire** : Créer un script qui copie les fichiers dans un dossier accessible

---

## 🔄 Options de Déploiement

### Option 1 : Import Manuel (Recommandé)

1. Ouvrir n8n SquidResearch
2. Workflows → Import from File
3. Sélectionner `workflows/n8n/publish_article_simple.json`
4. Adapter les chemins si nécessaire

### Option 2 : Montage Volume Docker

Si n8n est dans Docker, ajouter dans `docker-compose.yml` :

```yaml
services:
  n8n:
    volumes:
      - /home/lucas/tools/squidCommunication:/data/squidCommunication:ro
```

Puis adapter les chemins dans les workflows : `/data/squidCommunication/articles/...`

### Option 3 : Script de Synchronisation

Créer un script qui copie les fichiers nécessaires dans un dossier partagé accessible depuis n8n.

---

## 🔑 Credentials Existantes

Si des credentials OAuth2 sont déjà configurées dans n8n SquidResearch pour LinkedIn, Facebook, etc., elles peuvent être réutilisées directement dans les workflows importés.

---

## 📚 Références

- Guide rapide : `docs/N8N_QUICK_START.md`
- Guide détaillé : `docs/N8N_WORKFLOWS_SETUP.md`
- Configuration SquidResearch : Vérifier dans le repo SquidResearch

