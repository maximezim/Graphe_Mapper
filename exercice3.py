from classes import *
import listes as li
import matrices as mt
import conversion as cv
from exercice2 import *

def excentricite(s:Sommet, S):
    liste = []
    for voisins in s:
        if voisins in S:
            liste.append(voisins) if voisins not in liste else None
    if liste == S.sommets:
        return 1
    cpt = 1
    while liste != S.sommets:
        for s in liste:
            for voisins in s.voisins:
                if voisins not in liste:
                    liste.append(voisins)
            cpt += 1
    return cpt
        
def centre(G):
    m = []
    for s in G.sommets:
        minimum = excentricite(s,G)
        m.append(minimum)
    liste = []
    for i in range(len(m)):
        if m[i] == min(m):
            liste.append(m[i])
    return liste

def rayon(G):
    r = []
    for c in centre(G):
        r.append(excentricite(c,G))
    return r

def diametre(G):
    return None