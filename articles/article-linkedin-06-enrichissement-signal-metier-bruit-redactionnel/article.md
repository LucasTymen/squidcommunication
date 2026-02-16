Les offres d'emploi sont aussi des objets marketing. Elles cherchent à séduire, rassurer, valoriser une entreprise. Ce qui est utile pour un candidat ne l'est pas toujours pour un algorithme.

L'enrichissement commence donc par une séparation claire entre signal métier et bruit rédactionnel. Les éléments réellement exploitables sont ceux qui influencent directement l'exécution : outils utilisés, type de missions, contraintes, niveau attendu. À l'inverse, des expressions comme « environnement dynamique », « projets innovants » ou « fort esprit d'équipe » n'aident pas à la décision.

Dans SquidResearch, ce bruit n'est pas pénalisé : il est simplement ignoré. Le supprimer évite qu'il n'influence indirectement le scoring ou les décisions.

## Fonctionnement concret

Le système détecte automatiquement les phrases marketing vagues — « missions variées », « missions diverses », « environnement dynamique » — et les marque comme soft-fail. Ces expressions génèrent une pénalité de -0,2 dans le score négatif, mais surtout, elles sont exclues du calcul du signal métier.

L'absence de stack technique détaillée est également pénalisée (-0,2), car il s'agit d'un signal métier manquant, non d'un bruit. Le système extrait les outils concrets — Python, React, PostgreSQL, n8n, Zapier — et ignore les qualificatifs marketing — « dynamique », « flexible », « jeune équipe ».

Cette étape améliore fortement la lisibilité du système : moins de variables, mais des variables plus pertinentes.

L'objectif reste une fiabilité de 95 %. Le suivi des faux positifs permet d'ajuster les filtres : si le taux dépasse 5 %, le système alerte et suggère de resserrer les critères. En pratique, le bruit rédactionnel est souvent responsable de ces faux positifs : il crée une impression de richesse là où l'information utile est faible.

#SquidResearch #Enrichissement #DataEngineering #Matching #Automation #DataDriven