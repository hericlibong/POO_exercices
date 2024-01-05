class Eleve:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom


class Classe:
    pass


Classe.ajouter_eleve("John", "Smith")
print(Classe.eleves)