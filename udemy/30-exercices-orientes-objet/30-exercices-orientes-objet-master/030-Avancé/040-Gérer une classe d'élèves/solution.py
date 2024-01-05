class Eleve:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def __repr__(self):
        return "{} {}".format(self.prenom, self.nom)


class Classe:
    eleves = []

    @staticmethod
    def ajouter_eleve(prenom, nom):
        eleve = Eleve(prenom=prenom, nom=nom)
        Classe.eleves.append(eleve)


Classe.ajouter_eleve("John", "Smith")
print(Classe.eleves)