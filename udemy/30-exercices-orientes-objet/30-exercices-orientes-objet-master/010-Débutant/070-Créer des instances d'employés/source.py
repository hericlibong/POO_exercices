class Entreprise:
    
    name = 'FreeLance'
    employes_data = [
    ("Pierre", "Smith", "Responsable RH", 35000),
    ("Julie", "Martin", "Développeur Python", 42000),
    ("Éric", "Dupont", "Chef de projet", 50000),
    ]
    def __init__(self, name = None, employes_data=None):
        self.name = name or self.name
        self.employes = [Employe(*data) for data in (employes_data or self.employes_data)]
    
    def nombre_employes(self):
        return len(self.employes)
    
    def afficher_info_entreprise(self):
        print(f"L'entreprise {self.name} a {self.nombre_employes()} employés.")

    def afficher_noms_employes(self):
        if self.nombre_employes() > 0:
            print("Liste des employés :")
            for employe in self.employes:
                print(employe)
        else:
            print("Aucun employe dans l'entreprise")


class Employe:
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire

    def __repr__(self):
        return f" Nom : {self.prenom}, Prénom : {self.nom}"


entreprise = Entreprise()
entreprise.afficher_info_entreprise()
entreprise.afficher_noms_employes()




