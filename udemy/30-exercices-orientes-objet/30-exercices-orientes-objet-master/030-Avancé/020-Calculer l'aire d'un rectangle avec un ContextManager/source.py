class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

with Rectangle(6, 12) as r:
    r.calcul_aire()