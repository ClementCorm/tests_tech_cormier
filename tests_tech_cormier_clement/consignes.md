# Tests techniques � traitements script�s de flux structur�s

## Conditions de tests

Le candidat devra r�aliser un maximum d�exercices en 4 heures.

Toutes les ressources librement disponibles peuvent �tre utilis�es.

La qualit� du travail fournit sera � privil�gier � la quantit�.

## Description de la structure de donn�es

### Sal.txt

Le fichier sal.txt est constitu� de donn�es structur�es de la fa�on suivante.

Chaque client est repr�sent� par un ensemble de ligne.

Chaque ligne commence par un identifiant d�enregistrement suivi par une liste de champs s�par�s par le charact�re � � �.

Les donn�es d�un client commencent avec l�enregistrement � SAL_GEN � et se terminent avec la survenue d�un nouvel enregistrement � SAL_GEN � ou la fin du fichier.

### Ent.txt

Le fichier ent.txt contient des donn�es structur�es de la fa�on suivante.
Chaque entreprise est repr�sent�e par un ensemble de ligne.

Chaque ligne commence par un identifiant d�enregistrement suivi par une liste de champs s�par�s par le caract�re � � �.

Les donn�es d�une entreprise commencent avec l�enregistrement � ENT_GEN � et se terminent avec la survenue d�un nouvel enregistrement � ENT_GEN � ou la fin du fichier.

Pour retrouver les donn�es entreprise d�un client, il faut que le second champ apr�s l�enregistrement SAL_GEN soit �gale au second champ apr�s l�enregistrement ENT_GEN.

## Exercices de tri

### Exercice 1

Ecris un traitement dans le langage de ton choix permettant de trier les clients en fonction de la valeur contenue dans le 12�me champ apr�s l�enregistrement SAL_GEN.

Il faudra �tre attentif � l�int�grit� des donn�es de chaque client.

### Exercice 2

M�me exercice que l�exercice 1 mais en mettant en argument du traitement l�enregistrement et la position du champs devant servir de cl� de tri.

### Exercice 3

M�me exercice que l�exercice 2 mais permettant de soumettre un enregistrement contenu dans le fichier Ent.txt

## Exercices de filtre

### Exercice 1

Ecrit un traitement dans le langage de ton choix permettant de s�parer les clients dans deux fichiers distincts en fonction de la valeur contenue dans le 14�me champ apr�s l�enregistrement SAL_GEN.

Tous les clients avec la valeur M doivent �tre �cart�s dans un premier fichier et les autres dans un second fichier.

Il faudra �tre attentif � l�int�grit� des donn�es de chaque client.

### Exercice 2

M�me exercice que l�exercice 1 mais en mettant en argument du traitement l�enregistrement, la position du champ et la valeur recherch�e.

### Exercice 3

M�me exercice que l�exercice 2 mais en pouvant soumettre une expression rationnelle � la place de la valeur recherch�e.

### Exercice 4

M�me exercice que l�exercice 2 mais permettant de soumettre un enregistrement contenu dans le fichier Ent.txt .

## Exercice r�daction

D�cris une ou plusieurs �volutions qui permettrait d�am�liorer ces traitements.

## Crit�res d��valuation

Pour chacun des exercices de Scripting, il faudra fournir un dossier contenant :

- Le script permettant de r�aliser les op�rations demand�es
- Un second script donnant un exemple d�appel
- Les fichiers utilis�s en entr�e
- Les fichiers r�sultant du traitement donn� en exemple

Les �l�ments pris en compte pour �valuer la performance du candidat seront :

- La structuration des dossiers et sous dossier et la nomenclature des fichiers constituant le livrable
- La qualit� du code (lisibilit�, maintenabilit�, fiabilit�, �)
- La validit� du r�sultat attendu

Pour l�exercice de r�daction, ce sont la force de proposition et la qualit� de la r�daction qui seront prise en compte.
