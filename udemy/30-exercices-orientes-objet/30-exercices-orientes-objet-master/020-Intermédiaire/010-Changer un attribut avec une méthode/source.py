class Voiture:
    def __init__(self, marque, prix=int):
        self.marque = marque
        self.prix = prix

    def changer_prix(self, prix):
        self.prix = prix
        print(f"le nouveau prix est {self.prix}") 


voiture = Voiture(marque="Mazda", prix=30000)
voiture.changer_prix(35000)

#Affiche prix changé
