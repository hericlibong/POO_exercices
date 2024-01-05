class Voiture:
    def __init__(self):
        self.marque = "Mazda"
        self.couleur = "Rouge"

    def recuperer_couleur(self):
        return self.couleur


mazda_rouge = Voiture()
couleur = mazda_rouge.recuperer_couleur()