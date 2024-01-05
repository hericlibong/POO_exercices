class Livre:
    prix = 9.99

    def __init__(self, prix):
        self.prix = prix
        
    def changer_prix(self, prix):
        self.prix = prix


harry_potter = Livre(19.99)
harry_potter.changer_prix(prix=14.99)