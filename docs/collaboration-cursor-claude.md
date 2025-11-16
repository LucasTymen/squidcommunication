# 🤝 Collaboration Cursor ↔ Claude (MCP)

> Document de coordination pour optimiser le workflow entre Cursor (développement) et Claude (MCP actions)

---

## 🎯 Objectif

**Anticiper et préparer** tous les contenus/structures en amont pour que Claude puisse :
- ✅ Push sur Vercel
- ✅ Planifier dans Google Calendar
- ✅ Organiser dans Google Drive
- ✅ Créer templates Notion/Canva
- ✅ Monitorer analytics

**Sans consommer trop de tokens** (budget < 100€/semaine).

---

## 📋 Workflow Mutualisé

### Phase 1 : Cursor (Préparation)
1. ✅ Créer campagne via `create-linkedin-campaign.sh`
2. ✅ Générer tous les posts (3-5 messages)
3. ✅ Préparer structure assets (original/sanitized)
4. ✅ Remplir contenu des posts
5. ✅ Valider sécurité (`validate-campaign.sh`)
6. ✅ Mettre à jour `communication_projet.md`

### Phase 2 : Claude (MCP Actions)
1. 📅 Créer événements Google Calendar (dates de publication)
2. 📁 Organiser dossier Google Drive (assets campagne)
3. 📝 Générer template Notion (suivi KPIs)
4. 🎨 Préparer templates Canva (visuels LinkedIn)
5. 🚀 Publier sur Vercel (si landing/docs)
6. 📊 Monitorer analytics (après publication)

---

## 🚨 Points de Blocage & Améliorations

### Cursor (Points à améliorer)

#### ✅ Résolus
- Script `create-linkedin-campaign.sh` créé
- Templates simple & carousel disponibles
- Structure assets organisée
- Validation sécurité automatisée

#### 🔄 À améliorer
- [ ] **Auto-update `communication_projet.md`** : Le script devrait automatiquement ajouter une entrée dans le log après génération
- [ ] **Génération de dates intelligentes** : Prendre en compte les weekends et heures optimales LinkedIn
- [ ] **Validation contenu** : Vérifier que les posts ne sont pas vides avant validation sécurité
- [ ] **Template schedule.json** : Ajouter suggestions d heures optimales par jour de la semaine

#### 📝 Notes techniques
- Les dates générées sont basiques (espacement de 2 jours) → à affiner manuellement ou via script Python
- Le format JSON des posts dans `campaign.json` est correct mais pourrait être enrichi (métadonnées, tags)

---

### Claude (Points de blocage)

#### ⚠️ Limitations actuelles
- **Tokens restants** : [À mettre à jour par Claude après chaque session]
- **Actions MCP impossibles** : [À lister si problème technique]
- **Besoins complémentaires** : [À documenter si données manquantes]

#### 📋 Checklist avant action MCP
- [ ] Vérifier tokens restants (limite hebdomadaire)
- [ ] S assurer que tous les fichiers sont commités dans squidCommunication
- [ ] Vérifier que `campaign.json` est complet (objectif, message_key, hashtags)
- [ ] Confirmer que les assets sanitized sont prêts

#### 🔧 Actions MCP disponibles
- ✅ Google Calendar : Créer événements récurrents ou ponctuels
- ✅ Google Drive : Créer dossiers, organiser fichiers
- ✅ Notion : Créer pages/templates depuis modèles
- ✅ Canva : Générer designs depuis templates
- ✅ Vercel : Déployer depuis GitHub

---

## 📊 Suivi des Sessions

### Session [DATE]
- **Cursor** : [Actions effectuées]
- **Claude** : [Actions MCP effectuées]
- **Tokens consommés** : [Si disponible]
- **Blocages** : [Problèmes rencontrés]
- **Améliorations suggérées** : [Idées pour optimiser]

---

## 🔄 Procédure de Push Mutualisé

### SquidResearch (Cursor)
```bash
cd /home/lucas/tools/squidResearch
git add communication_projet.md private/IDEAS.md private/ROADMAP.md
git commit -m "docs: Update communication log & knowledge base"
git push github HEAD
```

### SquidCommunication (Claude)
```bash
cd /home/lucas/tools/squidCommunication
git add campaigns/ docs/ scripts/ templates/
git commit -m "feat: Add campaign [ID]"
git push origin main  # ou github selon config
```

**⚠️ Important** : Synchroniser les deux repos après chaque campagne pour que `communication_projet.md` reste à jour.

---

## 💡 Améliorations Futures

### Court terme
- [ ] Script Python pour générer dates optimales (éviter weekends, heures creuses)
- [ ] Template Notion pré-rempli depuis `campaign.json`
- [ ] Checklist MCP intégrée dans `campaign.json`

### Moyen terme
- [ ] Intégration GitHub Actions pour auto-push squidCommunication → Vercel
- [ ] Webhook pour mettre à jour `communication_projet.md` automatiquement
- [ ] Dashboard analytics consolidé (LinkedIn + Instagram)

### Long terme
- [ ] Automatisation complète : Cursor génère → Claude publie → Analytics remontent
- [ ] IA pour suggérer contenu optimal selon historique performances
- [ ] A/B testing automatisé (variantes de posts)

---

## 📞 Contact & Coordination

- **Cursor** : Développement, scripts, structure
- **Claude** : MCP actions, planification, publication
- **Log principal** : `squidResearch/communication_projet.md`
- **Base de connaissance** : `squidResearch/private/{IDEAS,ROADMAP}.md`

---

**Dernière mise à jour** : [DATE] par [CURSOR/CLAUDE]
