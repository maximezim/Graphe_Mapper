from classes import *

#Représentation d'un graphe sous forme de liste d'adjacence

class Graphe:
    def __init__(self):
        self.sommets = []
        self.aretes = []

    def __str__(self):
        # qffiche chaque sommet et ses voisins
        s = ""
        for sommet in self.sommets:
            s += str(sommet) + " : "
            for voisin in sommet.voisins:
                s += str(voisin) + " "
            s += "\n"

        return s


def graphe_vide():
    return Graphe()

def add_sommet(G, i:Sommet):
    if i not in G.sommets:
        G.sommets.append(i)

def add(G, i, j):
    arete = Arete(i, j)
    if arete not in G.aretes and i in G.sommets and j in G.sommets:
        G.aretes.append(arete)
        i.ajouter_voisin(j) if j not in i.voisins else None
        j.ajouter_voisin(i) if i not in j.voisins else None

def supp(G, i, j):
    arete = Arete(i, j)
    if arete in G.aretes:
        G.aretes.remove(arete)

def est_voisin(G, i, j):
    arete = Arete(i, j)
    return arete in G.aretes

def load(nom):
    with open (nom+".txt", "r") as f:
        n = int(f.readline())
        graphe = graphe_vide()

        for i in range(n):
            # ajoute sommet à graphe, la ligne contient l'identifiant et le nom
            identifiant, nom = f.readline().split()
            sommet = Sommet(nom, int(identifiant))
            add_sommet(graphe, sommet)
        for line in f:
            nom1, nom2 = line.split()
            for sommet in graphe.sommets:
                if sommet.nom == nom1:
                    i = sommet
                if sommet.nom == nom2:
                    j = sommet
            add(graphe, i, j)
        return graphe

def save(G, nom):
    with open(nom+".txt", "w") as f:
        m = []
        m.append(str(len(G.sommets))+ "\n")
        for sommet in G.sommets:
            m.append(str(sommet.identifiant) + " " + str(sommet.nom) + "\n")
        for arete in G.aretes:
            m.append(str(arete.sommet1.nom) + " " + str(arete.sommet2.nom) + "\n")
        f.writelines(m)
    f.close()


if __name__ == "__main__":
    G = graphe_vide()
    a = Sommet('A', 1)
    b = Sommet('B', 2)
    c = Sommet('C', 3)

    add_sommet(G, a)
    add_sommet(G, b)
    add_sommet(G, c)

    add(G, a, b)
    add(G, a, c)
    save(G, "test")

    print(G)

    load("test")

    print(G)
    