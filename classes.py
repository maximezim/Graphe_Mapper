class Sommet:
    def __init__(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.voisins = []

    def ajouter_voisin(self, voisin):
        self.voisins.append(voisin)

    def __str__(self):
        return str(self.nom)

    def __repr__(self):
        return str(self.nom)
    
    def __eq__(self, other):
        return self.identifiant == other.identifiant and self.nom == other.nom

class Arete:
    def __init__(self, sommet1, sommet2):
        self.sommet1 = sommet1
        self.sommet2 = sommet2

    def __str__(self):
        return str(self.sommet1.nom) + " - " + str(self.sommet2.nom)

    def __repr__(self):
        return str(self.sommet1.nom) + " - " + str(self.sommet2.nom)

    def __eq__(self, other):
        return (self.sommet1 == other.sommet1 and self.sommet2 == other.sommet2) or (self.sommet1 == other.sommet2 and self.sommet2 == other.sommet1)

