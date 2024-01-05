class Pizza:
    def __init__(self, nom, ingredients, prix=9.99):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

    @classmethod
    def napolitaine(cls):
        return cls(nom="Napolitaine",
                   ingredients=["Tomates", "Anchois"],
                   prix=12.99)

    @classmethod
    def fromage(cls):
        return cls(nom="4 Fromages",
                   ingredients=["Mozzarella", "Comté", "Cheddar", "Gorgonzola"],
                   prix=14.99)


napo = Pizza.napolitaine()
fromage = Pizza.fromage()