from classes import *
import listes as li
import matrices as mt
import conversion as cv
from exercice2 import *

def excentricite(s:Sommet, S):
    liste = []
    for voisins in s.voisins:
        if voisins in S.sommets:
            liste.append(voisins) if voisins not in liste else None
    if liste == S.sommets:
        return 1
    cpt = 1
    while liste != S.sommets:
        for i in range (len(liste)):
            for voisins in liste[i].voisins:
                if voisins not in liste:
                    liste.append(voisins)
        # tri de la liste
        cpt += 1
        liste.sort(key=lambda x: x.identifiant)
    return cpt

def calcul_distances(G):
    # calcule les plus courtes distances entre chaque couple de sommets
    listeDistances = []
    for s in G.sommets:
        # ajoute la liste des distances du sommet s
        liste = []
        cpt = 1
        for voisins in s.voisins:
            liste.append(voisins) if voisins not in liste else None
        for i in liste:
            listeDistances.append([s, i, cpt])
        while liste != G.sommets:
            for i in range (len(liste)):
                for voisins in liste[i].voisins:
                    if voisins not in liste:
                        liste.append(voisins)
            # tri de la liste
            cpt += 1
            liste.sort(key=lambda x: x.identifiant)
            for i in liste:
                listeDistances.append([s, i, cpt])
    # for i in listeDistances:
    #     for j in listeDistances:
    #         if i[0] == j[1] and i[1] == j[0]:
    #             listeDistances.remove(j)
    for i in listeDistances:
        if i[0] == i[1]:
            listeDistances.remove(i)
    shortest = []
    # copie de listeDistances dans shortest
    shortest = listeDistances.copy()
    for i in listeDistances:
        for j in shortest:
            if i[0] == j[0] and i[1] == j[1]:
                if i[2] < j[2]:
                    shortest.remove(j)    
    return shortest

def rayon(G):
    return excentricite(donne_centres(G)[0],G)

def donne_diametre(G, D):
    # on retourne la derniere valeur de la liste D puisque D est triee
    return D[-1][2]

def donne_centres(G):
    m = []
    for s in G.sommets:
        minimum = excentricite(s,G)
        m.append(minimum)
    liste = []
    for i in range(len(m)):
        if m[i] == min(m):
            liste.append(G.sommets[i])
    return liste

def calcul_degrees(G):
    liste = []
    for s in G.sommets:
        liste.append([s, len(s.voisins)])
    return liste

def donne_centredegre(G, D):
    listecentres = donne_centres(G)
    sommetmax = max(i[1] for i in D)
    maxi = []
    for d in D:
        if d[1] == sommetmax and d[0] in listecentres:
            maxi.append(d[0])
    return len(maxi)

# test
if __name__ == "__main__":
    graphe = li.graphe_vide()
    s1 = Sommet("A", 1)
    s2 = Sommet("B", 2)
    s3 = Sommet("C", 3)
    s4 = Sommet("D", 4)
    s5 = Sommet("E", 5)

    li.add_sommet(graphe, s1)
    li.add_sommet(graphe, s2)
    li.add_sommet(graphe, s3)
    li.add_sommet(graphe, s4)
    li.add_sommet(graphe, s5)

    li.add(graphe, s1, s2)
    li.add(graphe, s2, s3)
    li.add(graphe, s1, s4)
    li.add(graphe, s3, s5)

    # test rayon
    li.add(graphe, s1, s3)

    print(excentricite(s4,graphe))
    print(calcul_distances(graphe))
    print(rayon(graphe))

    donnees_dist = calcul_distances(graphe)
    print(donne_diametre(graphe, donnees_dist))

    print(donne_centres(graphe))

    print(calcul_degrees(graphe))
    print(donne_centredegre(graphe, calcul_degrees(graphe)))

