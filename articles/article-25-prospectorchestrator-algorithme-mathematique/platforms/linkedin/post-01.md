# LINKEDIN Post - ProspectOrchestrator : Algorithme mathématique

**Plateforme** : LINKEDIN  
**Généré le** : 2026-01-05 14:00:00 UTC  
**Statut** : draft  
**Format** : article

---

## Contenu

ProspectOrchestrator, c'est l'algorithme de matching qui calcule le score de compatibilité entre un CV et une offre d'emploi. Pas de machine learning opaque, juste une formule mathématique transparente avec des poids ajustables.

La formule analyse 6 critères principaux. Chaque critère a un poids : compétences techniques 40%, mission et contexte 25%, expérience 15%, puis localisation, langues, et autres critères pour le reste.

Le calcul est direct. Pour chaque critère, on note la correspondance de 0 à 100, on multiplie par le poids, et on somme. Résultat : un score final de 0 à 100 qui reflète la compatibilité.

La transparence est importante. Chaque score est explicable. Si un CV obtient 78, on sait exactement pourquoi : 85% en compétences techniques, 70% en mission, 90% en expérience, etc. Pas de boîte noire.

L'avantage, c'est qu'on peut ajuster les poids selon les besoins. Pour un poste très technique, on augmente le poids des compétences. Pour un poste orienté mission, on augmente le poids du contexte.

J'ai testé l'algorithme sur 24 candidatures. Résultat : 93% de gain de temps. De 30 minutes par candidature à 2 minutes avec l'algorithme qui fait le tri initial.

L'algorithme s'appelle ProspectOrchestrator parce qu'il orchestre la comparaison entre le prospect, le CV, et l'offre. Il fait la synthèse de tous les critères et retourne un score cohérent.

Contrairement aux systèmes de matching basés sur du machine learning, ici tout est explicable. On peut voir chaque critère, chaque poids, chaque calcul intermédiaire. C'est important pour comprendre pourquoi un CV correspond ou non à une offre.

La formule est implémentée en Python dans le module Applicator. Environ 200 lignes de code pour le calcul principal, testé avec plusieurs scénarios différents.

#SquidResearch #Algorithme #Matching #Mathématique #Transparence

---

## Métadonnées

- **Longueur** : ~750 caractères (adaptable pour article LinkedIn long)
- **Ton** : Professionnel mais détendu, personnel, authentique
- **Format** : Post LinkedIn (peut être étendu en article long)
- **Données utilisées** : 100% réelles depuis `growth/data-driven-metrics.md`

---

## SEO

**Mots-clés primaires** : algorithme, matching, scoring, mathématique, ProspectOrchestrator

**Long-tail keywords** :
- algorithme matching mathématique transparent
- scoring candidatures formule pondérée
- algorithme matching CV offres

**Hashtags** : #SquidResearch #Algorithme #Matching #Mathématique #Transparence

**Meta title** : ProspectOrchestrator : Algorithme mathématique matching CV/offres | SquidResearch

**Meta description** : Algorithme de matching transparent avec formule mathématique pondérée. 6 critères analysés, scoring 0-100 explicable. ProspectOrchestrator par SquidResearch.

---

## Visualisations Recommandées

**Napkin** (bar_chart) :
- Graphique barres horizontal : Pondération 6 critères (40%, 25%, 15%, etc.)
- Données : Poids par critère
- Style : Minimalist, couleurs différenciées
- Export : `assets/article-25-graphique-ponderation.png`

**Napkin** (flow_chart) :
- Diagramme : Processus calcul score (CV + Offre → 6 critères → Calcul pondéré → Score 0-100)
- Style : Technique mais accessible
- Export : `assets/article-25-diagramme-calcul.png`

---

## Notes Rédaction

- ✅ Données réelles uniquement (6 critères, 40%+25%+15%, 24 candidatures, 93% gain temps)
- ✅ Ton personnel ("j'ai testé", explications techniques)
- ✅ Pas de formules de cadrage
- ✅ Structure fluide (paragraphes courts)
- ✅ Pas de vocabulaire corporate excessif
- ✅ Pas d'emojis/symboles
- ✅ Pas de répétitions
- ✅ Conclusion naturelle

