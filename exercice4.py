from classes import *
import listes as li
import matrices as mt
import conversion as cv
from exercice2 import *
from exercice3 import *
import random

def G_liste(n,p):
    # génère un graphe aléatoire de n sommets et de probabilité p
    graphe = li.graphe_vide()
    for i in range(n):
        li.add_sommet(graphe, Sommet("s"+str(i), i))
    for i in graphe.sommets:
        for j in graphe.sommets:
            if i != j:
                if random.random() < p:
                    li.add(graphe, i, j)
    # sauvegarde texte
    li.save(graphe, "grapheListe")
    return graphe

def G_matrice(n,p):
    # génère un graphe aléatoire de n sommets et de probabilité p
    graphe = mt.graphe_vide()
    for i in range(n):
        mt.add_sommet(graphe, Sommet("s"+str(i), i))
    for i in graphe.sommets:
        for j in graphe.sommets:
            if i != j:
                if random.random() < p:
                    mt.add(graphe, i, j)
    # sauvegarde texte
    mt.save(graphe, "grapheMat")
    return graphe

# test
if __name__ == "__main__":
    print(G_liste(5, 0.2))
    print(G_matrice(5, 0.6))