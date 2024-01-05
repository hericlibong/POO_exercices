class Entreprise:
    def __init__(self, name):
        self.name = name
        self.employes = []


    def ajouter_employes(self, employe):
        self.employes.append(employe)

    def nombre_employes(self):
        return len(self.employes)
    
    def afficher_info_entreprise(self):
        if self.employes:
            print(f"L'entreprise {self.name} compte {self.nombre_employes()} employés ")
        else :
            print(f"L'entreprise {self.name} n'a pas d'employés")

    def afficher_liste_employes(self):
        if self.nombre_employes:
            print('liste des employés :')
            for employe in self.employes :
                print(employe)
        else:
            print("Auncun employé dans cette entreprise")
        

class Employe:
    def __init__(self, prenom, nom, position, salaire=float):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire

    
    def __str__(self):
        return f"Prenom : {self.prenom}, Nom: {self.nom}, Position:{self.position}"
    


#Création d'une entreprise
Freelance = Entreprise(name='Freelance')

# Création d'employés
employe1 = Employe('Fred', 'Vaughn', 'directeur commercial', 900.0)
employe2 = Employe('Lance', 'Stroll', 'merketing manager', 500.5)
employe3 = Employe('Alex', 'Red', 'Editor', 250.0)

#Ajout d'employés
Freelance.ajouter_employes(employe1)
Freelance.ajouter_employes(employe2)
Freelance.ajouter_employes(employe3)

#calculer nombre des employés dans l'entreprise
Freelance.nombre_employes()

#Afficher infos entreprise
Freelance.afficher_info_entreprise()

#Afficher liste des employés
Freelance.afficher_liste_employes()








