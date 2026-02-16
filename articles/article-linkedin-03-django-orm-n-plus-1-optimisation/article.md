L'ORM de Django est confortable, mais il rend très facile l'écriture de code qui génère trop de requêtes SQL. Le cas classique, c'est le fameux N+1.

Les outils existent pour l'éviter. `select_related` pour charger les relations simples en une requête, `prefetch_related` pour les relations plus complexes. Les annotations permettent aussi de déplacer certains calculs vers la base de données.

Dans SquidResearch, ces méthodes sont systématiques dès qu'une vue manipule un volume un peu conséquent. `only()` et `defer()` servent à limiter les champs chargés quand ce n'est pas nécessaire.

Le résultat est mesurable. Là où une vue déclenchait des dizaines de requêtes, on en obtient une ou deux. Ce n'est pas glamour, mais c'est souvent ce genre de détail qui permet à un produit de tenir quand l'usage augmente.

#SquidResearch #Django #ORM #Performance #PostgreSQL