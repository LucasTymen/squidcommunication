# 🗞️ SquidCommunication

> Centre éditorial et hub de communication pour SquidResearch

## 📁 Structure

```
squidCommunication/
├── landing/            # Site vitrine (Next.js/Astro)
├── docs/               # Centre de documentation
├── campaigns/          # Campagnes organisées par date
│   └── 2025-11-hub-communication/
│       ├── campaign.json
│       ├── linkedin/
│       ├── instagram/
│       └── assets/
├── templates/          # Templates réutilisables
│   ├── linkedin-post.md
│   ├── instagram-story.md
│   ├── campaign-brief.md
│   └── editorial-guidelines.md
└── scripts/           # Scripts d'automatisation
    └── validate-campaign.sh
```

## 🎯 Objectifs

1. **Séparer code produit et contenu marketing** : repos distincts pour sécurité et déploiements indépendants
2. **Automatiser la création de contenu** : templates + CLI + MCP (Claude)
3. **Assurer la sécurité** : checklist validation avant publication
4. **Tracer l'historique** : archive complète des campagnes
5. **Dogfooding** : utiliser la mise en place comme premier contenu de communication

## 🔗 Relation avec squidResearch

- **squidResearch** : Code source principal (privé)
- **squidCommunication** : Contenus marketing (public/semi-public)
- **Liaison** : Variables d'environnement, pas de chemins relatifs fragiles

## 🚀 Workflow

### 1. Créer une campagne

```bash
./scripts/create-campaign.sh "feature-matching"
```

### 2. Éditer le contenu

```json
{
  "campaign_id": "2025-11-feature-matching",
  "platforms": ["linkedin", "instagram"],
  "status": "draft"
}
```

### 3. Valider la sécurité

```bash
./scripts/validate-campaign.sh campaigns/2025-11-feature-matching
```

### 4. Publier

- Push sur Vercel (automatique via GitHub)
- Publication manuelle sur réseaux sociaux
- Archive dans `campaigns/<slug>/archive/`

## 🔒 Sécurité

Checklist obligatoire avant toute publication :

- [ ] Aucune IP visible (`192.***.***.***`)
- [ ] Credentials masqués (`pa****rd`)
- [ ] Pas de tokens/API keys
- [ ] Données clients floutées
- [ ] URLs internes remplacées
- [ ] Variables d'environnement non exposées
- [ ] Validation script exécutée

## 🤖 Collaboration MCP (Claude)

Claude peut :
- Créer des événements Google Calendar
- Organiser des dossiers Drive
- Générer des templates Notion/Canvas
- Déployer sur Vercel
- Planifier le contenu

Toutes les actions MCP sont consignées dans `squidResearch/communication_projet.md`

## 📊 Plateformes supportées

- LinkedIn (posts, articles)
- Instagram (posts, stories)
- Newsletter (emails)
- Blog (articles longs)

## 🛠️ Technologies

- **Landing** : Next.js / Astro (à décider)
- **Docs** : Markdown + générateur statique
- **Déploiement** : Vercel
- **Analytics** : LinkedIn Insights, Instagram Analytics

## 📝 Convention de nommage

- **Campagnes** : `YYYY-MM-slug` (ex: `2025-11-feature-matching`)
- **Assets** : `original/` (source) + `sanitized/` (version publique)
- **Archives** : `YYYY-MM-DD_final.zip`

## 🎓 Documentation

- [Workflow détaillé](./docs/workflow.md)
- [Guidelines éditoriales](./templates/editorial-guidelines.md)
- [Checklist sécurité](./docs/security-checklist.md)

---

**Créé le** : 2025-11-12
**Lié à** : [squidResearch](../squidResearch)
**Log principal** : `squidResearch/communication_projet.md`
