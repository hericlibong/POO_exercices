class Voiture:
    def __init__(self, marque = "Mazda" , couleur="Rouge"):
        self.marque = marque
        self.couleur = couleur

    def recuperer_couleur(self):
        return self.couleur


mazda_rouge = Voiture()
couleur = mazda_rouge.recuperer_couleur()