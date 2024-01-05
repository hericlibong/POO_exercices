


class Livre:
    """Création de la classe livre"""
    def __init__(self, titre, auteur, ISBN, genre, prix = float, pub_year = int, stock = True):
        """Initialise le titre, l'auteur, l'isbn, le genre et le stock"""
        self.titre = titre
        self.auteur = auteur
        self.ISBN = ISBN
        self.genre = genre
        self.prix = prix
        self.pub_year = pub_year
        self.stock = stock

    
    def __repr__(self):
        """Affiche la représentation du livre par son titre"""
        return self.titre
