etudiants_partis = []


class Etudiant:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom


john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")

del marc