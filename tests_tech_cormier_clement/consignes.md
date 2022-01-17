# Tests techniques – traitements scriptés de flux structurés

## Conditions de tests

Le candidat devra réaliser un maximum d’exercices en 4 heures.

Toutes les ressources librement disponibles peuvent être utilisées.

La qualité du travail fournit sera à privilégier à la quantité.

## Description de la structure de données

### Sal.txt

Le fichier sal.txt est constitué de données structurées de la façon suivante.

Chaque client est représenté par un ensemble de ligne.

Chaque ligne commence par un identifiant d’enregistrement suivi par une liste de champs séparés par le charactère « ¿ ».

Les données d’un client commencent avec l’enregistrement « SAL_GEN » et se terminent avec la survenue d’un nouvel enregistrement « SAL_GEN » ou la fin du fichier.

### Ent.txt

Le fichier ent.txt contient des données structurées de la façon suivante.
Chaque entreprise est représentée par un ensemble de ligne.

Chaque ligne commence par un identifiant d’enregistrement suivi par une liste de champs séparés par le caractère « ¿ ».

Les données d’une entreprise commencent avec l’enregistrement « ENT_GEN » et se terminent avec la survenue d’un nouvel enregistrement « ENT_GEN » ou la fin du fichier.

Pour retrouver les données entreprise d’un client, il faut que le second champ après l’enregistrement SAL_GEN soit égale au second champ après l’enregistrement ENT_GEN.

## Exercices de tri

### Exercice 1

Ecris un traitement dans le langage de ton choix permettant de trier les clients en fonction de la valeur contenue dans le 12ème champ après l’enregistrement SAL_GEN.

Il faudra être attentif à l’intégrité des données de chaque client.

### Exercice 2

Même exercice que l’exercice 1 mais en mettant en argument du traitement l’enregistrement et la position du champs devant servir de clé de tri.

### Exercice 3

Même exercice que l’exercice 2 mais permettant de soumettre un enregistrement contenu dans le fichier Ent.txt

## Exercices de filtre

### Exercice 1

Ecrit un traitement dans le langage de ton choix permettant de séparer les clients dans deux fichiers distincts en fonction de la valeur contenue dans le 14ème champ après l’enregistrement SAL_GEN.

Tous les clients avec la valeur M doivent être écartés dans un premier fichier et les autres dans un second fichier.

Il faudra être attentif à l’intégrité des données de chaque client.

### Exercice 2

Même exercice que l’exercice 1 mais en mettant en argument du traitement l’enregistrement, la position du champ et la valeur recherchée.

### Exercice 3

Même exercice que l’exercice 2 mais en pouvant soumettre une expression rationnelle à la place de la valeur recherchée.

### Exercice 4

Même exercice que l’exercice 2 mais permettant de soumettre un enregistrement contenu dans le fichier Ent.txt .

## Exercice rédaction

Décris une ou plusieurs évolutions qui permettrait d’améliorer ces traitements.

## Critères d’évaluation

Pour chacun des exercices de Scripting, il faudra fournir un dossier contenant :

- Le script permettant de réaliser les opérations demandées
- Un second script donnant un exemple d’appel
- Les fichiers utilisés en entrée
- Les fichiers résultant du traitement donné en exemple

Les éléments pris en compte pour évaluer la performance du candidat seront :

- La structuration des dossiers et sous dossier et la nomenclature des fichiers constituant le livrable
- La qualité du code (lisibilité, maintenabilité, fiabilité, …)
- La validité du résultat attendu

Pour l’exercice de rédaction, ce sont la force de proposition et la qualité de la rédaction qui seront prise en compte.
