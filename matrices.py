from classes import *

class graphe:
    # constructeur de la classe graphe
    def __init__(self):
        self.sommets = []
        self.arretes = []
        self.matrice = []

    # méthode pour retourner une représentation en chaîne de caractères du graphe
    def __str__(self):
        s = ""
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                s += str(self.matrice[i][j]) + " "
            s += "\n"
        return str(s)
    
    # méthode pour comparer deux graphes
    def __eq__(self, other):
        return self.matrice == other.matrice
    
# fonction pour créer un graphe vide
def graphe_vide():
    return graphe()

# fonction pour ajouter un sommet à un graphe
def add_sommet(G:graphe, sommet:Sommet):
    if sommet not in G.sommets:
        G.sommets.append(sommet)
        for i in range(len(G.matrice)):
            G.matrice[i].append(0)
        G.matrice.append([0] * (len(G.sommets)))

# fonction pour ajouter une arête entre deux sommets
def add(G:graphe, i:Sommet, j:Sommet):
    if i not in G.sommets:
        add_sommet(G, i)
    if j not in G.sommets:
        add_sommet(G, j)
    G.matrice[G.sommets.index(i)][G.sommets.index(j)] = 1
    G.matrice[G.sommets.index(j)][G.sommets.index(i)] = 1

# fonction pour supprimer une arête entre deux sommets
def supp(G:graphe, i:Sommet, j:Sommet):
    if i in G.sommets and j in G.sommets:
        G.matrice[G.sommets.index(i)][G.sommets.index(j)] = 0
        G.matrice[G.sommets.index(j)][G.sommets.index(i)] = 0

# fonction pour vérifier si deux sommets sont voisins
def est_voisin(G, i:Sommet, j:Sommet):
    if i in G.sommets and j in G.sommets:
        return G.matrice[G.sommets.index(i)][G.sommets.index(j)] == 1
    else:
        return False
    
# fonction pour créer un graphe à partir d'un fichier
def load(nom:str):
    G = graphe_vide()
    f = open(nom+".txt", "r")
    n = int(f.readline())
    for i in range(n):
        identifiant, nom = f.readline().split()
        sommet = Sommet(nom, int(identifiant))
        add_sommet(G, sommet)
    for line in f:
        nom1, nom2 = line.split()
        for sommet in G.sommets:
            if sommet.nom == nom1:
                i = sommet
            if sommet.nom == nom2:
                j = sommet
        add(G, i, j)
    f.close()
    return G

# fonction pour sauvegarder un graphe dans un fichier
def save(G:graphe, nom:str):
    f = open(nom+".txt", "w")
    f.write(str(len(G.sommets))+"\n")
    for i in range(len(G.sommets)):
        f.write(str(G.sommets[i].identifiant) + " " + G.sommets[i].nom + "\n")

    for i in range(len(G.sommets)):
        for j in range(len(G.sommets)):
            if G.matrice[i][j] == 1:
                f.write(G.sommets[i].nom + " " + G.sommets[j].nom + "\n")

    f.close()

if __name__ == "__main__":
    G = graphe_vide()
    s1 = Sommet("A", 0)
    s2 = Sommet("B", 1)
    s3 = Sommet("C", 2)
    s4 = Sommet("D", 3)
    add_sommet(G, s1)
    add_sommet(G, s2)
    add_sommet(G, s3)
    add_sommet(G, s4)
    add(G, s1, s2)
    add(G, s1, s3)
    add(G, s2, s3)
    add(G, s3, s4)
    print(G)
    supp(G, s1, s2)
    print(G)
    print(est_voisin(G, s1, s2))
    print(est_voisin(G, s1, s3))
    print(G)
    print("SAVE")
    save(G, "graphe2")
    print(G)
    print("LOAD")
    G2 = load("graphe2")
    print(G2)
