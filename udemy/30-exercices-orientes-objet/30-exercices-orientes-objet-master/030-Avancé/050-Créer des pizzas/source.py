class Pizza:
    def __init__(self, nom, ingredients, prix=9.99):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

napo = Pizza.napolitaine()
fromage = Pizza.fromage()