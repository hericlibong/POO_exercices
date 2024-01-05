class Personnage:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom


class Magicien(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom=prenom, nom=nom)
        self.puissance = 80


class Gobelin(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom=prenom, nom=nom)
        self.puissance = 20


class Chevalier(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom=prenom, nom=nom)
        self.puissance = 70