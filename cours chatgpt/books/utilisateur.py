# utilisateur.py

from bibliothèque import Bibliothèque

class Utilisateur:
    """Création de la classe Utilisateur"""
    utilisateurs_inscrits = []  # Liste des utilisateurs inscrits
    
    def __init__(self, prenom, nom):
        """Initie le prenom, le nom et le pseudo de l'utilisateur"""
        self.prenom = prenom
        self.nom = nom
        self.pseudo = None
        self.bibliotheque = Bibliothèque()  # Instancier la bibliothèque ici
        Utilisateur.utilisateurs_inscrits.append(self)

    def __str__(self):
        return f"{self.prenom}, {self.nom}"

    def create_pseudo(self, pseudo):
        """Crée un pseudo pour l'utilisateur"""
        if not self.pseudo:
            self.pseudo = pseudo
            print(f"Bienvenue {self.pseudo}! Vous êtes inscrits et vous pouvez emprunter des livres de la bibliothèque.")

    def emprunter_livre(self, titre_livre):
        """Emprunte un livre de la bibliothèque"""
        livre_trouve = None

        for livre in self.bibliotheque.liste_livres():  # Appeler la méthode sur l'instance de la bibliothèque
            if livre.titre == titre_livre:
                livre_trouve = livre
                if livre.stock:
                    print(f"Le livre '{livre.titre}' a été emprunté avec succès.")
                    livre.stock = False  # Mettre à jour l'état du stock
                else:
                    print(f"Le livre '{livre.titre}' n'est pas disponible pour le moment.")
                break

        if livre_trouve is None:
            print(f"Le livre '{titre_livre}' n'a pas été trouvé dans la bibliothèque.")
