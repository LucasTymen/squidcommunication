# 📝 Charte Éditoriale SquidResearch

## 🎯 Positionnement

**SquidResearch** est une plateforme d'enrichissement de contacts B2B et d'optimisation de candidatures par IA.

### Valeurs
- **Innovation** : Technologies de pointe (IA, scraping intelligent, matching)
- **Transparence** : Méthodologie ouverte, dogfooding
- **Efficacité** : Gain de temps mesurable pour les utilisateurs
- **Qualité** : Données enrichies, scoring intelligent

### Ton
- **Professionnel mais accessible** : Éviter le jargon technique excessif
- **Pédagogique** : Expliquer les concepts complexes simplement
- **Enthousiaste** : Montrer la passion pour le produit sans tomber dans l'exagération
- **Humble** : Reconnaître les limites, partager les apprentissages

## ✍️ Style d'écriture

### LinkedIn
- **Format** : 3-5 paragraphes courts (2-3 lignes chacun)
- **Longueur** : 150-300 mots
- **Structure** :
  1. Accroche (problème ou chiffre marquant)
  2. Contexte / Solution
  3. Bénéfice / Résultat
  4. Call-to-Action
- **Hashtags** : 3-5 max, pertinents (#SquidResearch toujours inclus)
- **Emojis** : Utilisés avec parcimonie (1-2 par post max)

### Instagram
- **Stories** : Texte court (10-15 mots max), très visuel
- **Posts** : Caption 1-2 phrases + call-to-action clair
- **Carousel** : 5-8 slides, 1 idée par slide
- **Hashtags** : 5-10, mix popularité/niche

### Newsletter
- **Sujet** : 6-10 mots, personnalisé, éviter spam triggers
- **Intro** : 2-3 phrases, résumer la valeur
- **Corps** : Sections courtes, sous-titres clairs
- **CTA** : 1 bouton principal, clair et actionnable

### Blog / Articles techniques
- **Titre** : Clair, SEO-friendly (50-60 caractères)
- **Introduction** : Problème → Solution → Valeur (3 paragraphes)
- **Structure** : H2, H3, listes à puces, code blocks
- **Longueur** : 800-1500 mots (articles techniques), 400-600 mots (news)
- **Images** : 1 image tous les 300 mots, captures d'écran annotées

## 🎨 Visuels

### Couleurs principales
- **Bleu SquidResearch** : #[À définir]
- **Noir/Gris** : Textes et backgrounds
- **Accents** : Vert (succès), Orange (warning), Rouge (urgent)

### Typographie
- **Titres** : Sans-serif, bold
- **Corps** : Sans-serif, regular
- **Code** : Monospace

### Assets
- **Captures d'écran** : Toujours floutées pour sécurité
- **Logos** : Haute résolution, fond transparent
- **Vidéos** : Max 2min, sous-titres obligatoires

## 🔑 Mots-clés récurrents

### Techniques
- Enrichissement de contacts
- Matching intelligent
- Scraping éthique
- IA générative
- Score de qualité

### Business
- Gain de temps
- Automatisation
- B2B
- Recrutement
- Productivité

### Éviter
- "Révolutionnaire" (sauf si vraiment justifié)
- "Magique" (préférer "intelligent")
- Jargon technique non expliqué (LLM → expliquer "IA")
- Superlatifs excessifs ("le meilleur", "unique au monde")

## 📅 Fréquence de publication

### LinkedIn
- **Posts** : 2-3 par semaine
- **Articles** : 1 par mois

### Instagram
- **Posts** : 2 par semaine
- **Stories** : 3-5 par semaine (séries, behind-the-scenes)

### Newsletter
- **Fréquence** : Bimensuelle (2 fois/mois)
- **Jour** : Mardi ou mercredi matin

### Blog
- **Articles techniques** : 1 par mois
- **Updates produit** : Au fil des releases

## 🤖 Exemples de posts types

### Showcase Feature
```
🚀 Nouvelle feature : Matching intelligent CV/Offre

On a travaillé sur un système de scoring qui analyse :
→ Compétences techniques (40%)
→ Mission & contexte (25%)
→ Expérience (15%)
→ Localisation (10%)
→ Langues (10%)

Résultat : 76% de précision sur les premiers tests.

Le plus ? Warnings explicites quand il manque des données critiques.
Fini les scores "neutres" qui ne veulent rien dire.

Plus d'infos en commentaire 👇

#SquidResearch #IA #Recrutement #MatchingAlgorithm
```

### Behind-the-scenes
```
📊 Dogfooding : On communique sur notre hub de communication

Meta alert 🤯

On vient de créer un système pour gérer toute notre communication :
- Repo séparé (landing + docs)
- Templates réutilisables
- Checklist sécurité automatique
- Intégration Claude (MCP) pour planif

Et on va communiquer... sur la création de ce système.

Pourquoi ? Parce que c'est le meilleur moyen de prouver qu'on sait construire des workflows intelligents.

La première campagne ? Ce post 😄

#SquidResearch #Dogfooding #ProductManagement
```

### Pédagogique
```
💡 Comment on enrichit 10 000 contacts sans se faire bloquer ?

3 règles d'or :

1️⃣ Rotation intelligente (Tor + fallback)
2️⃣ Whitelist/Blacklist par site
3️⃣ Délais randomisés (4-7s)

Le secret : ne JAMAIS paraître mécanique.

Un bot fait toujours la même chose.
Un humain... varie, hésite, se trompe.

Thread complet dans les commentaires 👇

#WebScraping #DataEnrichment #AntiBot
```

## 🔒 Règles de sécurité

### Toujours
- Masquer IPs : `192.***.***.***`
- Masquer credentials : `pa****rd`
- Flouter dashboards sensibles
- Anonymiser données clients

### Jamais
- Montrer tokens/API keys
- Exposer variables d'environnement
- Partager URLs internes complètes
- Publier emails/noms réels dans démos

### Process
1. Créer contenu avec données réelles
2. Passer le script `validate-campaign.sh`
3. Remplacer par données anonymisées
4. Double check manuel
5. Publication

## 📊 Analytics & Optimisation

### Métriques à tracker
- **Impressions** : Reach organique
- **Engagement rate** : Likes + Comments / Impressions
- **CTR** : Clics CTA / Impressions
- **Conversions** : Inscriptions / Clics

### A/B Testing
- Tester 2 accroches différentes
- Tester avec/sans emojis
- Tester horaires publication
- Tester formats (texte seul vs image vs vidéo)

### Learnings
- Noter dans `campaigns/<slug>/analytics.json`
- Synthèse mensuelle dans `communication_projet.md`
- Ajuster guidelines selon résultats

---

**Version** : 1.0
**Dernière mise à jour** : 2025-11-12
**Responsable** : Lucas
