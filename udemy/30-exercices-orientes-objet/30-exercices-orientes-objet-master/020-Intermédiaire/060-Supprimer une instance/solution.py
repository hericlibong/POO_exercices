etudiants_partis = []


class Etudiant:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def __del__(self):
        etudiants_partis.append("{} {}".format(self.prenom, self.nom))


john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")

del marc