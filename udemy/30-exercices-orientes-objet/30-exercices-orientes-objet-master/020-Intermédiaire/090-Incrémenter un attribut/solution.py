class Etudiant:
    repertoire = []

    def __init__(self, nom, prenom):
        self.prenom = prenom
        self.nom = nom
        self.uid = len(Etudiant.repertoire) + 1
        Etudiant.repertoire.append(self)


john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")
print(Etudiant.repertoire)
print(marc.uid)