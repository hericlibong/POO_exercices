class Personnage:
    def __init__(self, prenom, nom, puissance):
        self.prenom = prenom
        self.nom = nom
        self.puissance = puissance


class Magicien(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 80


class Gobelin(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 20


class Chevalier(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 70