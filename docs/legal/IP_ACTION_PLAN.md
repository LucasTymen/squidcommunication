# 🔒 Plan d'Action Protection IP - SquidResearch

> **Date de création** : 2025-11-12  
> **Statut** : 📋 En cours de préparation  
> **Objectif** : Protéger complètement SquidResearch avant communication publique

---

## 🎯 Vue d'Ensemble

Ce document détaille le plan d'action concret pour protéger SquidResearch selon les 7 piliers de protection IP pour un SaaS.

**⚠️ STRATÉGIE LOW-BUDGET** : Voir `docs/legal/IP_STRATEGY_LOW_BUDGET.md` pour approche progressive sans révéler le nom de marque immédiatement.

**Références** :
- Guide complet : `docs/legal/IP_PROTECTION_GUIDE.md`
- Stratégie low-budget : `docs/legal/IP_STRATEGY_LOW_BUDGET.md` ⭐ NOUVEAU
- Organismes : `docs/legal/ORGANISMES_RECOMMANDES.md`
- Roadmap : `private/ROADMAP.md` (section Protection IP)

---

## 📋 Checklist Complète

### ✅ 1. Dépôt Marque INPI ⭐ PRIORITÉ HAUTE

**Objectif** : Protéger le nom "SquidResearch" et le logo 🐙

#### Actions Immédiates

- [ ] **Vérifier disponibilité marque**
  - Recherche antériorité INPI : https://www.inpi.fr/
  - Vérifier domaines similaires
  - Vérifier marques déposées UE (EUIPO)
  - **Délai** : 1 jour
  - **Coût** : 0€ (recherche gratuite)

- [ ] **Préparer dossier de dépôt**
  - Logo haute résolution (format vectoriel SVG/PDF)
  - Description des produits/services
  - Classes à déposer :
    - **Classe 9** : Logiciels, applications SaaS
    - **Classe 35** : Services de gestion commerciale, publicité
    - **Classe 42** : Services informatiques, développement logiciel
  - **Délai** : 2-3 jours
  - **Coût** : 0€ (préparation)

- [ ] **Déposer marque INPI**
  - Dépôt en ligne : https://www.inpi.fr/fr/services-et-prestations/deposer-une-marque
  - Coût : **~250€** (1 classe) ou **~450€** (3 classes)
  - Délai de traitement : 4-6 mois
  - Protection : France uniquement
  - **Référence** : À noter dans `private/ROADMAP.md` après dépôt

- [ ] **Optionnel : Dépôt EUIPO (si expansion UE prévue)**
  - Coût : **~850€** (3 classes)
  - Délai : 4-12 mois
  - Protection : 27 pays UE
  - **Décision** : À prendre selon roadmap commerciale

#### Documents à Préparer

```markdown
# Dossier Marque INPI - SquidResearch

## Informations Déposant
- Nom : Lucas Tymen
- Email : lucas.tymen@gmail.com
- Adresse : [À compléter]

## Marque à Déposer
- Nom : SquidResearch
- Logo : [Fichier SVG/PDF]
- Description : Plateforme SaaS d'enrichissement de contacts B2B et optimisation de candidatures par IA

## Classes Demandées
- Classe 9 : Logiciels et applications SaaS
- Classe 35 : Services de gestion commerciale et publicité
- Classe 42 : Services informatiques et développement logiciel

## Justificatifs d'Usage (si déjà utilisé)
- Capture écran site web
- Preuve première utilisation (Git commits, emails)
```

**Timeline** :
- Semaine 1 : Recherche antériorité + préparation dossier
- Semaine 2 : Dépôt INPI
- Mois 4-6 : Réception certificat d'enregistrement

---

### ✅ 2. Protection Code Source par Droit d'Auteur ⭐ PRIORITÉ CRITIQUE

**Objectif** : Établir la propriété exclusive du code source

#### Actions Immédiates (Gratuit)

- [ ] **Ajouter copyright headers dans TOUS les fichiers**
  - Python : En-tête avec copyright
  - JavaScript/TypeScript : Copyright dans chaque fichier
  - HTML : Commentaire copyright
  - CSS : Commentaire copyright
  - **Script automatique** : À créer pour ajouter en masse
  - **Délai** : 2-3h
  - **Coût** : 0€

- [ ] **Créer LICENSE propriétaire**
  - Fichier `LICENSE` à la racine
  - Licence propriétaire (tous droits réservés)
  - Interdictions claires (reverse engineering, copie, etc.)
  - **Délai** : 30 min
  - **Coût** : 0€

- [ ] **Ajouter footer copyright sur site web**
  - Footer : "© 2024-2025 Lucas Tymen. SquidResearch™. Tous droits réservés."
  - Lien vers mentions légales
  - **Délai** : 15 min
  - **Coût** : 0€

- [ ] **Créer preuve d'antériorité**
  - Email horodaté à soi-même avec description projet
  - Export Git log avec timestamps
  - Screenshots architecture + features
  - **Délai** : 1h
  - **Coût** : 0€

#### Template Copyright Header

```python
"""
SquidResearch - Plateforme d'Enrichissement B2B & Optimisation Candidatures
Copyright (c) 2024-2025 Lucas Tymen. Tous droits réservés.

Ce code est la propriété exclusive de Lucas Tymen.
Toute reproduction, modification ou distribution non autorisée
est strictement interdite et constitue une violation du droit d'auteur.

For licensing inquiries: lucas.tymen@gmail.com
"""
```

**Timeline** :
- Aujourd'hui : Headers + LICENSE + Footer
- Cette semaine : Preuve antériorité (email + Git log)

---

### ✅ 3. CGU/CGV Solides avec Clauses PI ⭐ PRIORITÉ HAUTE

**Objectif** : Protéger légalement l'utilisation du service

#### Documents à Créer

- [ ] **CGU (Conditions Générales d'Utilisation)**
  - Section Propriété Intellectuelle (Article 5)
  - Section Licence d'Utilisation (Article 6)
  - Section Restrictions (Article 7)
  - Section Sanctions (Article 8)
  - Section Confidentialité Algorithmes (Article 9)
  - **Fichier** : `templates/legal/cgu.html`
  - **Délai** : 1 journée
  - **Coût** : 0€ (DIY) ou 150-500€ (avocat)

- [ ] **CGV (Conditions Générales de Vente)**
  - Section Prix et Paiement
  - Section Propriété Intellectuelle
  - Section Garanties et Responsabilité
  - Section Remboursements
  - **Fichier** : `templates/legal/cgv.html`
  - **Délai** : 1 journée
  - **Coût** : 0€ (DIY) ou 150-500€ (avocat)

- [ ] **Mentions Légales**
  - Éditeur du site
  - Directeur de publication
  - Hébergeur
  - Propriété intellectuelle
  - RGPD
  - **Fichier** : `templates/legal/mentions_legales.html`
  - **Délai** : 2h
  - **Coût** : 0€

- [ ] **Politique de Confidentialité (RGPD)**
  - Données collectées
  - Utilisation des données
  - Droits utilisateurs
  - Cookies
  - **Fichier** : `templates/legal/privacy_policy.html`
  - **Délai** : 3h
  - **Coût** : 0€

#### Clauses PI Critiques (CGU)

```markdown
## Article 5 - Propriété Intellectuelle

5.1. PROPRIÉTÉ EXCLUSIVE
Tous les éléments de SquidResearch (code source, algorithmes, base de données, 
design, interface, documentation) sont et restent la propriété exclusive 
de Lucas Tymen.

5.2. LICENCE D'UTILISATION
L'utilisateur reçoit une licence d'utilisation NON-EXCLUSIVE, NON-TRANSFÉRABLE, 
RÉVOCABLE pour utiliser le service SquidResearch via l'interface fournie.

Cette licence NE CONFÈRE AUCUN DROIT sur le code source ou les algorithmes.

5.3. RESTRICTIONS ABSOLUES
L'utilisateur s'interdit formellement de :
a) Décompiler, désassembler ou faire du reverse engineering
b) Copier, modifier ou distribuer le code
c) Créer des œuvres dérivées
d) Utiliser le service pour créer un service concurrent
e) Extraire les données par scraping ou autre moyen automatisé
f) Contourner les mesures de protection techniques

5.4. SANCTIONS
Toute violation entraînera :
- Résiliation immédiate du compte
- Interdiction d'accès définitive
- Poursuites judiciaires pour contrefaçon
- Dommages et intérêts
```

**Timeline** :
- Semaine 1 : CGU + Mentions légales
- Semaine 2 : CGV + Politique confidentialité
- Semaine 3 : Review avocat (optionnel)

---

### ✅ 4. Licences Open-Source Appropriées ⭐ PRIORITÉ MOYENNE

**Objectif** : Vérifier compatibilité licences dépendances avec licence propriétaire

#### Actions

- [ ] **Audit licences dépendances**
  - Lister toutes les dépendances Python (`requirements-*.txt`)
  - Lister toutes les dépendances JavaScript (`package.json`)
  - Vérifier compatibilité avec licence propriétaire
  - **Script** : À créer pour audit automatique
  - **Délai** : 1 journée
  - **Coût** : 0€

- [ ] **Créer fichier NOTICES**
  - Liste des composants open-source utilisés
  - Licences respectives
  - Crédits auteurs
  - **Fichier** : `NOTICES.txt` ou `docs/legal/THIRD_PARTY_LICENSES.md`
  - **Délai** : 2h
  - **Coût** : 0€

- [ ] **Vérifier licences copyleft (GPL)**
  - Si dépendance GPL → risque contamination
  - Évaluer alternatives (MIT, Apache, BSD)
  - **Délai** : 1 journée
  - **Coût** : 0€

#### Licences Compatibles avec Propriétaire

✅ **Compatibles** :
- MIT
- Apache 2.0
- BSD
- ISC
- Python Software Foundation License

⚠️ **Attention** :
- GPL v2/v3 (copyleft - peut contaminer)
- AGPL (copyleft fort - éviter)

**Timeline** :
- Semaine 1 : Audit complet
- Semaine 2 : Création NOTICES
- Si problème GPL : Semaine 3 : Remplacement dépendances

---

### ✅ 5. Contrats de Confidentialité (NDA) ⭐ PRIORITÉ MOYENNE

**Objectif** : Protéger informations sensibles avec collaborateurs/beta testers

#### Documents à Créer

- [ ] **NDA Beta Testers (One-Way)**
  - Confidentialité fonctionnalités non publiques
  - Interdiction reverse engineering
  - Durée : 2 ans après fin beta
  - **Fichier** : `docs/legal/nda_beta_tester.md`
  - **Délai** : 2h
  - **Coût** : 0€

- [ ] **NDA Collaborateurs (Two-Way)**
  - Confidentialité code source
  - Propriété IP sur contributions
  - Clause non-concurrence (optionnelle)
  - **Fichier** : `docs/legal/nda_collaborateur.md`
  - **Délai** : 3h
  - **Coût** : 0€

- [ ] **Contrat Prestation (Freelance)**
  - Cession droits d'auteur sur code créé
  - Confidentialité
  - Propriété IP
  - **Fichier** : `docs/legal/contrat_prestation.md`
  - **Délai** : 4h
  - **Coût** : 0€ (template) ou 200-500€ (avocat)

#### Template NDA Beta Tester

```markdown
# ACCORD DE CONFIDENTIALITÉ (NDA)
# SquidResearch - Beta Privée

Entre :
- Lucas Tymen, créateur de SquidResearch ("Le Divulgant")
- [Nom du beta tester], ("Le Destinataire")

## Informations Confidentielles

Le Destinataire s'engage à garder confidentielles toutes informations 
concernant SquidResearch, incluant mais non limité à :
- Code source et algorithmes
- Architecture technique
- Fonctionnalités non publiques
- Métriques business
- Roadmap produit
- Stratégies commerciales

## Obligations

Le Destinataire s'engage à :
1. NE PAS divulguer ces informations à des tiers
2. NE PAS utiliser ces informations à des fins personnelles
3. NE PAS créer de service concurrent basé sur ces informations
4. NE PAS faire de reverse engineering

## Durée

Cet accord reste en vigueur pendant 2 ans après la fin de la beta.

## Sanctions

Violation = dommages et intérêts + poursuites judiciaires

Date : _________
Signature Destinataire : _________
```

**Timeline** :
- Semaine 1 : NDA Beta Testers
- Si recrutement : NDA Collaborateurs + Contrat Prestation

---

### ✅ 6. Sécurisation Site Web & Infrastructure ⭐ PRIORITÉ HAUTE

**Objectif** : Protéger contre piratage et accès non autorisés

#### Actions Techniques

- [ ] **Audit sécurité infrastructure**
  - Vérifier configuration serveurs
  - Vérifier firewall
  - Vérifier SSL/TLS
  - Vérifier backups
  - **Délai** : 1 journée
  - **Coût** : 0€ (DIY) ou 500-2000€ (audit professionnel)

- [ ] **Protection anti-reverse engineering**
  - Code minifié en production
  - Obfuscation JavaScript (optionnel)
  - Détection debug/decompilation
  - **Délai** : 2 jours
  - **Coût** : 0€

- [ ] **Rate limiting & DDoS protection**
  - Limiter requêtes API
  - Protection DDoS (Cloudflare/Vercel)
  - Détection scraping automatique
  - **Délai** : 1 journée
  - **Coût** : 0€ (Cloudflare free) ou 20€/mois (pro)

- [ ] **Monitoring & Alertes**
  - Logs sécurité
  - Alertes tentatives accès non autorisés
  - Détection anomalies
  - **Délai** : 1 journée
  - **Coût** : 0€ (Sentry free tier)

#### Checklist Sécurité

- [ ] HTTPS activé partout
- [ ] Secrets dans variables d'environnement (jamais en code)
- [ ] Rate limiting sur toutes les APIs
- [ ] Authentification forte (2FA)
- [ ] Backups automatiques quotidiens
- [ ] Monitoring logs sécurité
- [ ] Protection CSRF/XSS
- [ ] SQL injection protection (ORM Django)
- [ ] Headers sécurité (CSP, HSTS, etc.)

**Timeline** :
- Semaine 1 : Audit + corrections critiques
- Semaine 2 : Protection anti-reverse engineering
- Semaine 3 : Monitoring & alertes

---

### ✅ 7. Brevet Innovations Technologiques ⭐ PRIORITÉ À ÉVALUER

**Objectif** : Protéger innovations techniques uniques (si brevetables)

#### Évaluation Brevetabilité

**⚠️ IMPORTANT** : Les algorithmes/logiciels sont généralement **NON BREVETABLES** en Europe.
En France/UE, seules les **inventions techniques** avec **effet technique** sont brevetables.

#### Innovations Potentielles à Évaluer

- [ ] **Algorithme de Matching Unifié**
  - Innovation : Système de scoring multi-critères avec hard-fail
  - Brevetable ? : ❌ Probablement NON (algorithme pur)
  - Alternative : Secret commercial + protection code source

- [ ] **Système d'Enrichissement Multi-Sources**
  - Innovation : Orchestration intelligente de scrapers avec fallback
  - Brevetable ? : ❌ Probablement NON (méthode business)
  - Alternative : Secret commercial

- [ ] **Système Anti-Détection Tor Intelligent**
  - Innovation : Whitelist/Blacklist automatique par site
  - Brevetable ? : ⚠️ À évaluer (peut avoir effet technique)
  - Coût évaluation : 500-1000€ (conseil en PI)

#### Alternatives au Brevet

✅ **Protection par Secret Commercial** :
- Code source non divulgué
- Algorithmes non documentés publiquement
- Protection par NDA avec collaborateurs
- **Coût** : 0€
- **Durée** : Indéfinie (tant que secret gardé)

✅ **Protection par Droit d'Auteur** :
- Code source protégé automatiquement
- **Coût** : 0€
- **Durée** : 70 ans après mort auteur

#### Décision Brevet

**Recommandation** : 
- ❌ **NE PAS breveter** les algorithmes (non brevetables en UE)
- ✅ **Protéger par secret commercial** + droit d'auteur
- ✅ **Déposer marque INPI** (plus efficace pour SaaS)

**Si vraiment innovation technique** :
- Consultation avocat PI spécialisé : 500-1000€
- Dépôt brevet INPI : 2000-5000€
- Dépôt brevet européen : 5000-15000€
- **ROI** : Très faible pour SaaS (brevets logiciels difficiles à défendre)

**Timeline** :
- Semaine 1 : Évaluation brevetabilité (DIY)
- Si innovation technique : Consultation avocat (optionnel)

---

## 📊 Budget Global Protection IP

### Phase 1 : Immédiat (Gratuit/Low-Cost)

| Action | Coût | Délai | Priorité |
|--------|------|-------|----------|
| Copyright headers | 0€ | 2h | ⭐⭐⭐ |
| LICENSE propriétaire | 0€ | 30min | ⭐⭐⭐ |
| Footer copyright | 0€ | 15min | ⭐⭐⭐ |
| Preuve antériorité | 0€ | 1h | ⭐⭐⭐ |
| CGU + Mentions légales | 0€ | 1 jour | ⭐⭐⭐ |
| Audit licences | 0€ | 1 jour | ⭐⭐ |
| NDA Beta Testers | 0€ | 2h | ⭐⭐ |
| **TOTAL** | **0€** | **~3 jours** | |

### Phase 2 : Avant Communication Publique (Low-Cost)

| Action | Coût | Délai | Priorité |
|--------|------|-------|----------|
| Domaines (.com, .fr) | 30€ | 1 jour | ⭐⭐⭐ |
| Enveloppe Soleau INPI | 15€ | 1 semaine | ⭐⭐ |
| CGV | 0€ (DIY) | 1 jour | ⭐⭐ |
| Politique confidentialité | 0€ | 3h | ⭐⭐ |
| Audit sécurité (DIY) | 0€ | 1 jour | ⭐⭐ |
| **TOTAL** | **45€** | **~2 semaines** | |

### Phase 3 : Avant Monétisation (Premium)

| Action | Coût | Délai | Priorité |
|--------|------|-------|----------|
| Marque INPI (3 classes) | 450€ | 4-6 mois | ⭐⭐⭐ |
| Dépôt APP (logiciel) | 60€ | 1-2 mois | ⭐⭐ |
| Audit juridique | 500-1000€ | 1 mois | ⭐⭐ |
| Assurance RC Pro | 300€/an | 1 semaine | ⭐ |
| **TOTAL** | **1310-1810€** | **4-6 mois** | |

### Phase 4 : Scale (Optionnel)

| Action | Coût | Délai | Priorité |
|--------|------|-------|----------|
| Marque EUIPO (UE) | 850€ | 4-12 mois | ⭐⭐ |
| Copyright US (DMCA) | 55 USD | 1-3 mois | ⭐⭐ |
| Avocat retainer | 200€/mois | Continu | ⭐ |
| **TOTAL** | **1000-2000€/an** | | |

---

## 🎯 Plan d'Action Priorisé

### ✅ Cette Semaine (Gratuit)

1. **Aujourd'hui** :
   - [ ] Ajouter copyright headers (script automatique)
   - [ ] Créer LICENSE propriétaire
   - [ ] Ajouter footer copyright site web
   - [ ] Créer preuve antériorité (email + Git log)

2. **Cette semaine** :
   - [ ] Rédiger CGU + Mentions légales
   - [ ] Audit licences dépendances
   - [ ] Créer NDA Beta Testers

### 💰 Semaine Prochaine (Low-Cost)

3. **Semaine 2** :
   - [ ] Réserver domaines (.com, .fr)
   - [ ] Rédiger CGV + Politique confidentialité
   - [ ] Audit sécurité infrastructure

4. **Semaine 3** :
   - [ ] Enveloppe Soleau INPI
   - [ ] Préparer dossier marque INPI
   - [ ] Protection anti-reverse engineering

### 🏆 Avant Monétisation (Premium)

5. **Mois 1-2** :
   - [ ] Dépôt marque INPI (450€)
   - [ ] Dépôt APP logiciel (60€)

6. **Mois 3-4** :
   - [ ] Audit juridique complet (500-1000€)
   - [ ] Assurance RC Pro (300€/an)

---

## 📝 Suivi & Documentation

### Fichiers à Créer/Mettre à Jour

- [ ] `LICENSE` (propriétaire)
- [ ] `templates/legal/cgu.html`
- [ ] `templates/legal/cgv.html`
- [ ] `templates/legal/mentions_legales.html`
- [ ] `templates/legal/privacy_policy.html`
- [ ] `docs/legal/nda_beta_tester.md`
- [ ] `docs/legal/nda_collaborateur.md`
- [ ] `docs/legal/THIRD_PARTY_LICENSES.md`
- [ ] `private/ROADMAP.md` (mettre à jour section Protection IP avec références)

### Références à Noter

Après chaque dépôt, noter dans `private/ROADMAP.md` :
- Numéro dépôt INPI (marque)
- Numéro enveloppe Soleau
- Numéro dépôt APP
- Dates de dépôt
- Dates de réception certificats

---

## 🔗 Ressources & Contacts

### Organismes Officiels

- **INPI** : https://www.inpi.fr/ - Tél : 01 53 04 53 04
- **APP** : https://www.app.asso.fr/ - Tél : 01 40 26 20 00
- **EUIPO** : https://euipo.europa.eu/
- **CNCPI** (Avocats PI) : https://www.cncpi.fr/

### Outils Gratuits

- Recherche marques INPI : https://www.inpi.fr/fr/services-et-prestations/rechercher-une-marque
- Génération CGU : https://fr.orson.io/1371/generateur-mentions-legales
- Audit licences : `license-checker` (npm) ou `pip-licenses` (Python)

---

## ⚡ Actions Immédiates (Aujourd'hui)

### Script Automatique Copyright Headers

```bash
# Script à créer : scripts/add_copyright_headers.sh
# Ajouter copyright dans tous les fichiers Python/JS/HTML
```

### Email Preuve Antériorité

```
À : lucas.tymen@gmail.com
Objet : [PROOF] SquidResearch - Propriété Intellectuelle 2025-11-12

Description projet SquidResearch :
- Plateforme SaaS d'enrichissement contacts B2B
- Optimisation candidatures par IA
- Features : ENRICHED, BotFriendly, idFinder
- Code source propriétaire
- Algorithmes : Matching Engine, Enrichment Multi-Sources
- [Screenshots attachés]
- [Architecture diagram attaché]

Horodatage : 2025-11-12
```

---

**Dernière mise à jour** : 2025-11-12  
**Prochaine review** : Après dépôt marque INPI

