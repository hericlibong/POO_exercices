class Livre:
    prix = 9.99
    def __init__(self, prix):
        self.prix = prix



harry_potter = Livre(9.99)
print(harry_potter.prix)