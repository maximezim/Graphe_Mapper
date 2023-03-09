<center>

<link href="style.css" rel="stylesheet"></link>

# Compte rendu

</center>

<br>

- [Compte rendu](#compte-rendu)
  - [Classes](#classes)
    - [Listes d'adjacence](#listes-dadjacence)
    - [Matrice d'adjacence](#matrice-dadjacence)
    - [Méthodes](#méthodes)
  - [Exercice 2](#exercice-2)
  - [Exercice 3](#exercice-3)
  - [Exercice 4](#exercice-4)
  - [Tests](#tests)


<br>

## Classes 

Pour simplifier la lecture ainsi que la réutilisation du code, nous avons décidé de créer des classes pour les sommets ainsi que pour les arêtes. Nous avons aussi créé une classe par type de graphes que nous avons implémenté.  
Chaque sommet a un identifiant unique, un nom et une liste de voisins.

```py
self.nom = nom
self.identifiant = identifiant
self.voisins = []
```

<br>

### Listes d'adjacence

Pour les listes d'adjacence noous avons donc une classe graphe qui est composé des éléments sommets et arêtes.

```py
self.sommets = []
self.aretes = []
```

<br>

### Matrice d'adjacence

Pour les matrices d'adjacence nous avons une classe graphe qui est composé des éléments sommets et arêtes ainsi que de sa matrice d'adjacence.

```py
self.sommets = []
self.arretes = []
self.matrice = []
```

<br>

### Méthodes 

Nous avons implémenté les méthodes suivantes pour les deux types de graphe:
- `graphe_vide()` : Créer un graphe vide
- `add_sommet()` : Ajouter un sommet au graphe
- `add` : Ajouter une arête au graphe
- `supp` : Supprimer une arête du graphe
- `est_voisin` : Vérifier si deux sommets sont voisins
- `load` : Charger un graphe depuis un fichier
- `save` : Sauvegarder un graphe dans un fichier


<br>
<br>

## Exercice 2

Dans l'exercice 2 nous avons implémenté les méthodes suivantes pour les deux types de graphe:
- `inclus_sommet` : Vérifier si les sommets d'un graphe sont inclus dans un autre graphe
- `inclus_aretes` : Vérifier si les arêtes d'un graphe sont inclus dans un autre graphe
- `est_partiel` : Vérifier si un graphe est partiel d'un autre graphe
- `est_sous_graphe` : Vérifier si un graphe est un sous-graphe d'un autre graphe
- `est_sous_graphe_partiel` : Vérifier si un graphe est un sous-graphe partiel d'un autre graphe
- `est_clique` : Vérifier si un graphe est une clique
- `est_stable` : Vérifier si un graphe est stable

<br>
<br>

## Exercice 3

Dans l'exercice 3 nous avons implémenté les méthodes suivantes pour les deux types de graphe:
- `excentricite` : Calculer l'excentricité d'un sommet
- `calcul_distance` : Calculer la pplus courte distance entre deux sommets
- `rayon` : Calculer le rayon d'un graphe
- `donne_diametre` : Calculer le diamètre d'un graphe
- `donne_centre` : Calculer le centre d'un graphe
- `calcul_degres` : Calculer le degré d'un graphe
- `donne_centredegres` : Calculer le centre à partir du degré d'un graphe

<br>
<br>

## Exercice 4

Dans l'exercice 4, nous avons implémenté les fonctions pour générer aléatoirement des graphes de taille n avec des probabilités `p`concernant la création d'arêtes.  
Ces graphes sont sauvegardés dans un fichier texte.

<br>
<br>

## Tests

Pour chaque fichier, nous avons testé des fonctions à la fin de ceux-ci.