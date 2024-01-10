class Livre:
    """Classe livre"""

    list_livres = []

    def __init__(self, titre, auteur, id, available=True):
        """initialise le nom, l'auteur, l'id unique et la disponibilité placé sur True par défaut"""
        self.titre = titre
        self.auteur = auteur
        self.id = id
        self.available = available
        Livre.add_livre(self)

    @classmethod
    def add_livre(cls, livre):
        cls.list_livres.append(livre)

    def affiche_livre(self):
        """Affiche la fiche complète du livre choisi"""
        for livre in self.list_livres:
            if livre.available == True:
                livre.message ="Livre en stock"
            else :
                livre.message = "Livre n'est pas disponible"
            print("--- Fiche du livre ---- ")
            print(f" Titre : {livre.titre} \n Auteur : {livre.auteur} \n id : {livre.id} \n available : {livre.message}")

    def __str__(self):
        return self.titre
    
    @classmethod
    def afficher_livres(cls):
        """Affiche la liste de livres présent"""
        print("-----liste des livres------")
        for livre in cls.list_livres:
            
            print(f"Titre : {livre.titre } \n Auteur : {livre.auteur} \n id :{livre.id} \n available :{livre.available} ")
            print("------------")




