Tous les critères d'un matching n'ont pas le même poids.

Certains sont non négociables. S'ils ne sont pas remplis, le match n'a pas de sens. Ce sont les hard-fails.

D'autres critères sont importants, mais pas éliminatoires. Leur absence doit dégrader le score, pas l'annuler. Ce sont les soft-fails.

Dans SquidResearch, cette logique s'appuie sur des données réelles, pas sur des règles théoriques.

## Scoring positif

Le scoring positif repose sur des signaux observés sur plus de 200 offres analysées.

**Score élevé (0.7 à 1.0)** → forte clarté du poste :
- Mention explicite d'outils d'automatisation comme n8n, Zapier ou Make (+0.3)
- Stack technique détaillée (Python, APIs, webhooks) (+0.2)
- Missions d'automatisation clairement formulées (+0.3)
- Contexte growth ou marketing assumé (+0.2)

Exemple réel : « Growth Engineer – Automatisation workflows marketing avec n8n et intégration APIs » → score 0.85

**Score moyen (0.4 à 0.7)** → alignement partiel : L'automatisation est mentionnée sans précision technique, les missions sont globalement cohérentes mais vagues. Exemple : « Growth Marketing – Optimisation des processus » → score 0.55

**Score faible (0.0 à 0.4)** → offres trop générales, sans stack ni missions liées à l'automatisation. Exemple : « Marketing Manager – Gestion campagnes pub » → score 0.25

## Scoring négatif

Le score négatif repose sur une distinction stricte entre hard-fails et soft-fails, calibrée sur plus de 150 cas.

**Hard-fails** (pénalité forte, match non pertinent) :
- Poste senior ou lead avec 5+ ans requis (-0.8)
- Stack incompatible (Java/Spring vs Python/automation) (-0.7)
- Missions sans lien automation ou growth (-0.6)
- Présence physique obligatoire incompatible (-0.5)

Exemple : « Senior Growth Lead – Stack Java/Spring » → negative_score -0.8

**Soft-fails** (dégradation sans annulation) :
- Absence de stack détaillée (-0.2)
- Missions vagues (« participer à la croissance ») (-0.3)
- Buzzwords RH sans contenu (-0.1)
- Alternance ou stage mal positionné (-0.2)

Exemple : « Growth Engineer – Missions variées dans un environnement dynamique » → negative_score -0.3

## Décision finale

Basée sur des seuils validés sur plus de 100 décisions :

- **APPLY_NOW** si score ≥ 0.8 et aucun hard-fail
- **DRIP** entre 0.6 et 0.8
- **REJECT** en dessous de 0.6 ou en cas de hard-fail

Résultat après trois itérations : 87 % de concordance avec les décisions humaines, 65 % de rejet correctement détecté, 12 % d'offres très alignées.

Une seule règle trop stricte suffit à casser l'équilibre. La frontière hard/soft-fails est donc le point le plus critique du système.

#SquidResearch #Algorithmes #Matching #Data #RecrutementTech