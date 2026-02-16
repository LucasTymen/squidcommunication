Dès qu'un produit fait autre chose que répondre à une requête HTTP, l'asynchrone devient indispensable. Scraping, enrichissement, matching, relances… certaines opérations prennent du temps.

Les exécuter en synchrone bloquerait l'interface. Ce n'était pas une option. Celery gère donc les tâches en arrière-plan : une tâche envoyée, un worker la traite. Si la charge augmente, on ajoute des workers.

La persistance est essentielle. Les tâches passent par un broker, ce qui évite de perdre du travail si un service tombe. On apprécie surtout ce détail le jour où quelque chose casse.

Redis joue un autre rôle : éviter de refaire inutilement le même travail. Un enrichissement coûteux est mis en cache avec une durée de vie adaptée à la stabilité de la donnée. Si Redis n'est pas disponible, le système continue, simplement plus lentement.

Le gain est concret. Un traitement qui prend plus d'une minute la première fois se résume ensuite à quelques millisecondes. Pas spectaculaire, juste efficace. Un peu comme déléguer des quêtes secondaires à des PNJ pendant qu'on continue l'histoire principale.

#SquidResearch #Python #Celery #Redis #Asynchrone