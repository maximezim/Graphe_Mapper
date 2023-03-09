from classes import *
import listes
import matrices
import os

# on convertit d'un graphe à un autre en sauvegardant en fichier temporaire

def matrice_to_liste(G):
    matrices.save(G, "temp")
    L = listes.load("temp")
    os.remove("temp")
    return L

def liste_to_matrice(G):
    listes.save(G, "temp")
    M = matrices.load("temp")
    os.remove("temp")
    return M
