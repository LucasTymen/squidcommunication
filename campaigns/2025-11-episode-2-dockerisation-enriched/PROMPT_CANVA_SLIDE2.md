# Prompt Canva - Slide 2 : Le défi de l'enrichissement B2B

## 📐 Format
- **Dimensions** : 1080 x 1080 pixels (carré)
- **Orientation** : Portrait carré
- **Usage** : LinkedIn Carousel (slide 2/9)

---

## 🎨 Style & Charte Graphique BOGOSS

### Couleurs principales
- **Fond principal** : Dégradé sombre violet-rouge
  - `linear-gradient(140deg, #1a0a1a 0%, #2d0f2d 40%, #3d1a3d 70%, #4a1f4a 100%)`
- **Couleur d'accent** : Rouge/Orange pour les problèmes
  - `#ef4444` (rouge) ou `rgba(239, 68, 68, 0.95)`
- **Texte principal** : Blanc cassé
  - `rgba(226, 232, 240, 0.88)`
- **Cartes problèmes** : Fond semi-transparent rouge
  - `rgba(239, 68, 68, 0.1)` avec bordure `rgba(239, 68, 68, 0.4)`

### Typographie
- **Police** : Poppins (ou équivalent moderne sans-serif)
- **Titre principal** : 64px, bold, couleur rouge `#ef4444`
- **Sous-titre/Intro** : 26px, couleur blanc cassé
- **Titres de cartes** : 28px, bold, couleur rouge
- **Texte descriptif** : 18px, couleur gris clair
- **Texte résultat** : 22px, bold, couleur rouge

### Style visuel
- **Effet glassmorphism** : Cartes avec `backdrop-filter: blur(8px)`
- **Ombres** : Douces, `box-shadow: 0 40px 90px -30px rgba(15, 15, 40, 0.75)`
- **Coins arrondis** : `border-radius: 20px` pour les cartes, `48px` pour le container
- **Bordure** : Fine, rouge semi-transparente

---

## 📋 Contenu à créer

### Structure de la slide

#### 1. **Titre principal** (en haut)
```
Le défi de l'enrichissement B2B
```
- Taille : 64px
- Couleur : Rouge `#ef4444`
- Position : Centré en haut
- Style : Bold, légèrement animé (effet "shake" subtil)

#### 2. **Texte d'introduction** (sous le titre)
```
Avant le module Enriched : chaque enrichissement prenait 30-60 secondes, 
avec des coûts API qui explosaient et des données incohérentes.
```
- Taille : 26px
- Couleur : Blanc cassé `rgba(226, 232, 240, 0.88)`
- Position : Centré, sous le titre
- Largeur : ~80% de la largeur

#### 3. **Grille de 4 problèmes** (2 colonnes x 2 lignes)

**Carte 1 - Données dispersées** (haut gauche)
- **Icône** : 📁 (dossier) - 32px, rouge
- **Titre** : "Données dispersées" - 28px, bold, rouge
- **Contenu** :
  - **Problème :** Email dans une API, domaine dans une autre, entreprise ailleurs.
  - **Impact :** 5-10 requêtes séquentielles par entreprise, temps cumulé : 45s en moyenne.
- **Graphique** : Petit graphique en coin supérieur droit (100x60px)
  - Ligne descendante rouge montrant la dégradation
  - Style : Graphique de performance négative
- **Style carte** : Fond rouge semi-transparent, bordure rouge, coins arrondis

**Carte 2 - Sources multiples** (haut droite)
- **Icône** : 🔀 (flèches croisées) - 32px, rouge
- **Titre** : "Sources multiples" - 28px, bold, rouge
- **Contenu** :
  - **Problème :** Sources multiples non synchronisées, pas d'orchestration.
  - **Impact :** Données contradictoires, nécessité de fusion manuelle.
- **Style carte** : Fond rouge semi-transparent, bordure rouge, coins arrondis

**Carte 3 - Requêtes lentes** (bas gauche)
- **Icône** : 🐌 (escargot) - 32px, rouge
- **Titre** : "Requêtes lentes" - 28px, bold, rouge
- **Contenu** :
  - **Problème :** Appels API séquentiels, pas de parallélisation.
  - **Impact :** 30-60s par entreprise, impossible de traiter en masse.
- **Graphique** : Petit graphique en coin supérieur droit (100x60px)
  - Ligne descendante rouge montrant la lenteur
- **Style carte** : Fond rouge semi-transparent, bordure rouge, coins arrondis

**Carte 4 - Pas de cache** (bas droite)
- **Icône** : 💾 (disquette barrée) - 32px, rouge
- **Titre** : "Pas de cache" - 28px, bold, rouge
- **Contenu** :
  - **Problème :** Même entreprise enrichie 10 fois = 10x le coût API.
  - **Impact :** Coûts multipliés par 5-10, budgets explosés rapidement.
- **Style carte** : Fond rouge semi-transparent, bordure rouge, coins arrondis

#### 4. **Texte résultat** (sous la grille)
```
Résultat : Enrichir 1000 entreprises = 8-15 minutes + 50-100€ de coûts API
```
- Taille : 22px
- Couleur : Rouge `rgba(239, 68, 68, 0.9)`
- Position : Centré
- Style : Bold, mis en évidence

#### 5. **Footer** (en bas)
```
Problématique enrichissement · état des lieux
```
- Taille : 24px
- Couleur : Gris clair `rgba(148, 163, 184, 0.8)`
- Position : Centré en bas

---

## 🎯 Instructions de design Canva

### Layout général
1. **Container principal** : Carte centrale avec fond semi-transparent, effet glassmorphism
   - Padding : 80px haut/bas, 100px gauche/droite
   - Coins arrondis : 48px
   - Bordure : 1px, rouge semi-transparent

2. **Grille des problèmes** :
   - 2 colonnes égales
   - Gap entre les cartes : 30px
   - Chaque carte : padding 28px, coins arrondis 20px
   - Hauteur des cartes : ~200px

3. **Graphiques** :
   - Position : Coin supérieur droit de chaque carte concernée
   - Taille : 100px x 60px
   - Style : Graphique linéaire avec ligne rouge descendante
   - Fond : Semi-transparent sombre

### Éléments visuels à ajouter
- **Icônes** : Utiliser des icônes modernes et colorées (emojis ou icônes vectorielles)
- **Graphiques** : Petits graphiques de performance négative (lignes descendantes)
- **Effets** : Légères ombres portées sur les cartes
- **Animations suggérées** : Légers effets de "shake" ou "pulse" sur les icônes (optionnel)

### Hiérarchie visuelle
1. **Titre** : Le plus visible, rouge vif
2. **Cartes problèmes** : Mise en évidence avec bordures rouges
3. **Texte résultat** : Mis en évidence, rouge
4. **Footer** : Discret, gris clair

---

## 📝 Prompt texte pour Canva

```
Crée une slide LinkedIn carousel (1080x1080px) sur le thème "Le défi de l'enrichissement B2B".

STYLE :
- Fond : Dégradé sombre violet-rouge (#1a0a1a → #4a1f4a)
- Carte centrale : Fond semi-transparent avec effet glassmorphism, bordure rouge fine
- Couleur principale : Rouge #ef4444 pour les accents et titres
- Typographie : Poppins, moderne, hiérarchie claire

CONTENU :
1. Titre en haut : "Le défi de l'enrichissement B2B" (64px, rouge, bold)
2. Texte intro : "Avant le module Enriched : chaque enrichissement prenait 30-60 secondes, avec des coûts API qui explosaient et des données incohérentes." (26px, blanc cassé)
3. Grille 2x2 avec 4 cartes problèmes :
   - Carte 1 (haut gauche) : 📁 "Données dispersées" - Email dans une API, domaine dans une autre. Impact : 5-10 requêtes séquentielles, 45s en moyenne. + Petit graphique ligne descendante en coin
   - Carte 2 (haut droite) : 🔀 "Sources multiples" - Sources non synchronisées, pas d'orchestration. Impact : Données contradictoires, fusion manuelle.
   - Carte 3 (bas gauche) : 🐌 "Requêtes lentes" - Appels API séquentiels, pas de parallélisation. Impact : 30-60s par entreprise. + Petit graphique ligne descendante en coin
   - Carte 4 (bas droite) : 💾 "Pas de cache" - Même entreprise enrichie 10 fois = 10x le coût. Impact : Coûts x5-10.
4. Texte résultat : "Résultat : Enrichir 1000 entreprises = 8-15 minutes + 50-100€ de coûts API" (22px, rouge, bold, centré)
5. Footer : "Problématique enrichissement · état des lieux" (24px, gris clair)

STYLE DES CARTES :
- Fond : Rouge semi-transparent (rgba(239, 68, 68, 0.1))
- Bordure : 2px, rouge (rgba(239, 68, 68, 0.4))
- Coins arrondis : 20px
- Icônes : 32px, rouge, à gauche du titre
- Graphiques : 100x60px, coin supérieur droit, ligne rouge descendante

EFFETS :
- Ombres douces sur les cartes
- Effet glassmorphism (flou d'arrière-plan)
- Légers effets de profondeur

RÉSULTAT : Slide moderne, impactante, mettant en évidence les problèmes de l'enrichissement B2B non orchestré.
```

---

## ✅ Checklist de validation

- [ ] Format 1080x1080px respecté
- [ ] Titre rouge bien visible
- [ ] 4 cartes problèmes en grille 2x2
- [ ] Graphiques présents sur cartes 1 et 3
- [ ] Texte résultat mis en évidence
- [ ] Footer discret en bas
- [ ] Style BOGOSS respecté (couleurs, typographie)
- [ ] Effet glassmorphism sur la carte principale
- [ ] Tous les textes lisibles et bien hiérarchisés


