Les erreurs font partie du fonctionnement normal d'un système : une API qui ne répond pas, un timeout réseau, une donnée invalide.

Le problème n'est pas l'erreur, mais la manière dont on la traite.

**Première règle appliquée dans SquidResearch :** attraper des exceptions spécifiques. Un `except Exception` masque trop de choses et complique toujours le diagnostic. Chaque domaine a ses propres exceptions, avec des messages explicites et du contexte utile.

Le **logging** est central. Lorsqu'une erreur survient, le système enregistre ce qui a été tenté, avec quels paramètres, et dans quel état. Pas pour pointer du doigt, mais pour comprendre rapidement.

Pour les erreurs temporaires, un mécanisme de **retry avec backoff** est utilisé. Pour les erreurs définitives, l'échec est volontairement rapide : attendre inutilement coûte plus cher que tomber proprement.

Les **générateurs** jouent un autre rôle important. Lorsqu'on traite de gros volumes, charger toutes les données en mémoire n'est pas une bonne idée. Un `yield` change complètement la donne : on traite élément par élément, sans explosion mémoire.

Ce sont des choix peu visibles, mais déterminants. Comme souvent, la robustesse vient de ce qu'on ne remarque pas tant que tout fonctionne.

#SquidResearch #Python #CleanCode #Robustesse #Backend