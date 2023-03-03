from classes import *
import listes as li
import matrices as mt
import conversion as cv

# Renvoie 1 si G est inclus dans G_prime, 0 sinon
def inclus_sommet(G, G_prime, strict):
    for s in G.sommets:
        if s not in G_prime.sommets:
            return 0
    if strict == 1:
        if len(G.sommets) >= len(G_prime.sommets):
            return 0
    return 1

# Renvoie 1 si les arêtes du graphe G sont incluses (strictement) dans les arêtes du graphe G_prime, 0 sinon
def inclus_arete(G, G_prime):
    # inclusion stricte des arêtes
    for a in G.aretes:
        if a not in G_prime.aretes:
            return 0
    if len(G.aretes) >= len(G_prime.aretes):
        return 0
    return 1

# Renvoie 1 si G est partiel de G_prime, 0 sinon
def est_partiel(G, G_prime):
    if inclus_arete(G, G_prime) == 1 and inclus_sommet(G, G_prime, 0) == 1 and len(G.sommets) == len(G_prime.sommets):
        return 1
    return 0

# Renvoie 1 si G est un sous-graphe de G_prime, 0 sinon
def est_sous_graphe(G, G_prime):
    if inclus_sommet(G, G_prime, 0) == 1 and inclus_arete(G, G_prime) == 1:
        return 1
    return 0

def est_sous_graphe_partiel(G, G_prime):
    if inclus_sommet(G, G_prime, 1) == 1 and inclus_arete(G, G_prime) == 1:
        return 1

def est_clique(G, G_prime):
    if est_sous_graphe(G, G_prime) == 1:
        for s in G.sommets:
            if len(s.voisins) != (len(G.sommets) - 1):
                return 0
        return 1
    return 0

def est_stable(G, G_prime):
    for s in G.sommets:
        if len(s.voisins) != 0:
            return 0
        if est_sous_graphe(G, G_prime) == 1:
            return 1
    return 0

# test
if __name__ == "__main__":
    graphe = li.graphe_vide()
    s1 = Sommet("A", 1)
    s2 = Sommet("B", 2)
    s3 = Sommet("C", 3)

    s4 = Sommet("A", 1)
    s5 = Sommet("B", 2)
    s6 = Sommet("C", 3)

    li.add_sommet(graphe, s1)
    li.add_sommet(graphe, s2)
    li.add_sommet(graphe, s3)

    li.add(graphe, s1, s2)
    li.add(graphe, s1, s3)

    g = li.graphe_vide()
    li.add_sommet(g, s4)
    li.add_sommet(g, s5)
    # li.add_sommet(g, s6)

    # li.add(g, s4, s5)
    print("Inclu Sommet:",bool(inclus_sommet(g, graphe, 0)))
    print("Inclu Arete:",bool(inclus_arete(g, graphe)))
    print("Partiel :",bool(est_partiel(g, graphe)))
    print("Sous-Graphe :",bool(est_sous_graphe(g, graphe)))
    print("Sous-Graphe partiel:",bool(est_sous_graphe_partiel(g, graphe)))
    print("Clique :",bool(est_clique(g, graphe)))
    print("Stable :" , bool(est_stable(g, graphe)))
