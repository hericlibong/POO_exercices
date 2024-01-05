class Boisson:
    def __init__(self, prix, description):
        self.prix = prix
        self.description = description
    
    def boire(self):
        print(f"C'est une boisson que je bois sans savoir ce qu'il y a dedans. {self.description}")

class Café(Boisson):
    tarifs = {'normal': 1, 'serré': 1.5, 'allongé': 2}

    def __init__(self, type, description):
        self.type = type
        super().__init__(prix=self.tarifs.get(type, 1), description=description)
    
    def boire(self):
        #super().boire()
        print(f"Cela fera : {self.prix} Euros !! Merci !! Un bon café {self.type} pour me réveiller !")

# Exemple d'utilisation
cafe_allonge = Café(type='allongé', description="Un café fort avec une grande quantité d'eau.")
description_cafe = cafe_allonge.description
print(description_cafe)
cafe_allonge.boire()



# boisson = Boisson(prix = 4)
# boisson.boire()
# cafe_allonge = Café(type='allongé')
# cafe_allonge.boire()