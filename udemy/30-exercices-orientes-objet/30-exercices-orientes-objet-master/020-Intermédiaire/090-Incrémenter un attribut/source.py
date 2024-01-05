class Etudiant:
    repertoire = []

    def __init__(self, nom, prenom):
        self.prenom = prenom
        self.nom = nom


john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")
print(Etudiant.repertoire)
print(marc.uid)