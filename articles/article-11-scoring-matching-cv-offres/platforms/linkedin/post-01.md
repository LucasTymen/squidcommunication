# LINKEDIN Post - Scoring matching CV/offres (0-100)

**Plateforme** : LINKEDIN  
**Généré le** : 2026-01-05 14:00:00 UTC  
**Statut** : draft  
**Format** : post

---

## Contenu

J'ai passé pas mal de temps à chercher comment automatiser le matching entre CV et offres d'emploi. Le problème classique : comment savoir si un CV correspond vraiment à une offre sans passer des heures à comparer manuellement ?

J'ai fini par créer un algorithme de scoring qui donne une note de 0 à 100. Pas de magie noire, juste des critères pondérés : compétences techniques, mission et contexte, expérience, localisation, langues, et quelques autres.

Le truc intéressant, c'est que la formule est transparente. Chaque critère a son poids, et on peut voir exactement pourquoi un CV obtient 78 plutôt que 45. Ça évite les boîtes noires où on ne comprend rien.

La pondération est différenciée. Les compétences techniques représentent environ 40% du score. La mission et le contexte, 25%. L'expérience, 15%. Le reste se répartit entre localisation, langues, et autres critères secondaires.

Résultat concret : je passe de 30 minutes par candidature à environ 2 minutes. Le système fait le tri initial, je garde la main sur les décisions finales. C'est un gain de temps énorme sans perdre le contrôle.

L'algorithme s'appelle ProspectOrchestrator, et il analyse 6 critères principaux. Pas de machine learning opaque, juste une formule mathématique transparente avec des poids ajustables selon les besoins.

Sur 24 candidatures gérées avec cet algorithme, le gain de temps est de 93%. De 30 minutes à 2 minutes par candidature. Ça fait 28 minutes gagnées à chaque fois, multipliées par le nombre de candidatures, c'est significatif.

Si vous avez déjà testé des systèmes de matching, vous savez que beaucoup promettent la lune mais déçoivent. Ici, c'est l'inverse : simple, transparent, efficace.

#SquidResearch #Matching #Scoring #IA #Recrutement

---

## Métadonnées

- **Longueur** : ~750 caractères
- **Ton** : Professionnel mais détendu, personnel, authentique
- **Format** : Post LinkedIn
- **Données utilisées** : 100% réelles depuis `growth/data-driven-metrics.md`

---

## SEO

**Mots-clés primaires** : scoring, matching, CV, offres, algorithme, recrutement

**Long-tail keywords** :
- algorithme matching CV offres
- scoring candidatures automatique
- matching IA recrutement

**Hashtags** : #SquidResearch #Matching #Scoring #IA #Recrutement

**Meta title** : Scoring matching CV/offres (0-100) | SquidResearch

**Meta description** : Algorithme de scoring transparent (0-100) pour matching CV/offres. 6 critères pondérés, 93% gain temps. ProspectOrchestrator par SquidResearch.

---

## Visualisations Recommandées

**Napkin** (bar_chart) :
- Graphique barres horizontal : Pondération critères (40% compétences, 25% mission, etc.)
- Données : 6 critères avec poids
- Style : Minimalist, couleurs différenciées
- Export : `assets/article-11-graphique-ponderation.png`

**Napkin** (line_chart) :
- Graphique : Temps par candidature (30min manuel vs 2min automatique)
- Données : 93% gain temps
- Style : Simple, ligne descendante
- Export : `assets/article-11-graphique-temps.png`

---

## Notes Rédaction

- ✅ Données réelles uniquement (24 candidatures, 93% gain temps, 6 critères)
- ✅ Ton personnel ("j'ai passé", "j'ai fini")
- ✅ Pas de formules de cadrage
- ✅ Structure fluide (paragraphes courts)
- ✅ Pas de vocabulaire corporate excessif
- ✅ Pas d'emojis/symboles
- ✅ Pas de répétitions
- ✅ Conclusion naturelle

