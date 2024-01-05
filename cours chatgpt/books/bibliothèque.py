
from data import list_books
from livre import Livre
import random



class Bibliothèque:
    """Création de la classe Bibliothèque"""
    livres = []  # Déclarer livres comme une variable de classe

    def __init__(self):
        """Initialise les livres"""
        self.get_data()

    def get_data(self):
        """Charge les données depuis le fichier liste"""
        for book in list_books:
            new_book = Livre(**book)
            Bibliothèque.livres.append(new_book)
        print('Données chargées avec succès')
    
    @classmethod
    def liste_livres(cls):
        livres = [livre for livre in cls.livres]
        return livres


    def add_livre(self, livre):
        """Ajoute un livre et affiche le livre"""
        self.livres.append(livre)
        print(f"'{livre}' a été ajouté à la bibliothèque")
    
    def afficher_fiches(self):
        """Affiche tous les livres avec leur fiche complète"""
        for livre in self.livres:
            print("-----Fiche complète------")
            print(f"Titre : {livre} | Auteur : {livre.auteur} ")
            print(f"Prix : {livre.prix}")
            print(f"Genre : {livre.genre}")
            print(f" Date de publication : {livre.pub_year} | ISBN-13 : {livre.ISBN}")
            if livre.stock:
                print(f"Ce livre est disponible en stock")
            else :
                print("Ce livre n'est pas disponible en stock")
            print("----------")
    
    def voir_livres(self):
        """Voir tous les titres de de tous les livres"""
        for livre in self.livres:
            print(livre.titre)
            print("-----")
    
    def count_livres(self):
        """afficher le nombre de livres présents dans la bibliothèque"""
        print(f"Il y a {len(self.livres)} dans la bibliothèque")

    def afficher_genre(self):
        """ afficher les genres"""
        for livre in self.livres:
            print(livre.genre)
    
    
    def recherche_par_genre(self, genre_recherche):
        """Permet de faire une recherche de livre par genre"""
        selected_genre = [livre for livre in self.livres if livre.genre == genre_recherche ]
        if not selected_genre:
            print(f"il n'y a pas de livre dans la catégorie : '{genre_recherche}'. ")
        else :
            print(f"il y a {len(selected_genre)} livre(s) dans : '{genre_recherche}'. ")
            print("------- Résultats de la recherche -----")
            for livre in selected_genre:
                print(f"Titre : {livre.titre} | Auteur : {livre.auteur}")
                print(f"Prix : {livre.prix} Euros")
                print(f"Genre : {livre.genre}")
                print(f" Date de publication : {livre.pub_year} | ISBN-13 : {livre.ISBN}")
                if livre.stock:
                    print(f"Ce livre est disponible en stock")
                else :
                    print("Ce livre n'est pas disponible en stock")
                print("----------")

    def genres_disponibles(self):
        """Renvoie les genres de livres présents avec le nombre d'éléments en face de chaque genre"""
        genres_counts = {}
        for livre in self.livres:
            if livre.genre in genres_counts:
                genres_counts[livre.genre] += 1
            else:
                genres_counts[livre.genre] = 1
        
        for genre, count in genres_counts.items():
            print(f"{genre} |  {count}")


    def livre_par_annee(self, année):
        """Recherche les fims par année et affiche la fiche des livres trouvés"""
        selected_year = [livre for livre in self.livres if livre.pub_year == année]
        if not selected_year:
            print(f"il n'y a pas de livre publié en {année} dans la bibliothèque")
        else :
            print(f"Il y a {len(selected_year)} livre(s) publié(s) en {année} dans la bibliothèque")
            print("-----Résultats de la Recherche---------")
            for livre in selected_year:
                print(f"Titre : {livre.titre} | Auteur : {livre.auteur}")
                print(f"Prix : {livre.prix} Euros")
                print(f"Genre : {livre.genre}")
                print(f" Date de publication : {livre.pub_year} | ISBN-13 : {livre.ISBN}")
                if livre.stock:
                    print(f"Ce livre est disponible en stock")
                else :
                    print("Ce livre n'est pas disponible en stock")
                print("----------")
    
    def livres_par_annee_disponibles(self):
        """Affiche l'année et le nombre de livres par année """
        pub_year_counts = {}
        for livre in self.livres:
            if livre.pub_year in pub_year_counts:
                pub_year_counts[livre.pub_year] +=1
            else :
                pub_year_counts[livre.pub_year] = 1
        
        for pub_year, count in pub_year_counts.items():
            print(f"{pub_year} | {count}")
    
    def get_random_books(self):
        """Affiche un livre de façon aléatoire"""
        livre_choisi = random.choice(self.livres)
        print(f"titre : {livre_choisi.titre} | Auteur : {livre_choisi.auteur}")
        
    def sort_by_name(self):
        """trie les livres par ordre alphabétique en fonction du nom de l'auteur"""
        self.livres.sort(key=lambda livre: livre.auteur)

    def sort_and_display_by_name(self):
        """Affiche les livres par ordre alphabétique avec leur année de sortie"""
        sorted_books = sorted(self.livres, key=lambda livre: livre.titre)
        print('---Livres triés par ordre alphabétique---')
        for book in sorted_books:
            print(f"{book.titre}, {book.pub_year}")
            print("----------")
    
    def livre_par_auteur(self):
        """Affiche le nombre de livres par auteur"""
        auteur_livre_counts = {}
        for livre in self.livres:
            if livre.auteur in auteur_livre_counts:
                auteur_livre_counts[livre.auteur] +=1
            else :
                auteur_livre_counts[livre.auteur] = 1
        for auteur, count in auteur_livre_counts.items():
            print(f"{auteur} | {count}")

    def recherche_par_auteur(self, auteur_recherche):
        """Recherche livre(s) par auteur"""
        selected_auteur = [livre for livre in self.livres if livre.auteur == auteur_recherche]
        if not selected_auteur:
            print(f"Il n'y pas de livre correspondant à {auteur_recherche} dans la bibliothèque")
        else:
            print(f"Il y a {len(selected_auteur)} de '{auteur_recherche}' dans la bibliothèque")
            print("------- Résultats de la recherche -----")
            for livre in selected_auteur:
                print(f"Titre : {livre.titre} | Auteur : {livre.auteur}")
                print(f"Prix : {livre.prix} Euros")
                print(f"Genre : {livre.genre}")
                print(f" Date de publication : {livre.pub_year} | ISBN-13 : {livre.ISBN}")
                if livre.stock:
                    print(f"Ce livre est disponible en stock")
                else :
                    print("Ce livre n'est pas disponible en stock")
                print("----------")
    
    def recherche_livre_par_critere(self, critere, valeur_recherche):
        """Recherche de livre(s) par critère spécifié"""
        selected_books = [livre for livre in self.livres if getattr(livre, critere)==valeur_recherche]
        if not selected_books:
            print(f"Il n'a pas de livre correspondant à '{valeur_recherche}' dans la bibliothèque")
        else : 
            print(f"Il y a {len(selected_books)} livre(s) correpondant(s) à '{valeur_recherche}' dans la bibliothèque") 
            for livre in selected_books:
                print("----Résultat de la recherche ------")
                print(f"Titre : {livre.titre} | Auteur : {livre.auteur}")
                print(f"Prix : {livre.prix} Euros")
                print(f"Genre : {livre.genre}")
                print(f" Date de publication : {livre.pub_year} | ISBN-13 : {livre.ISBN}")
                if livre.stock:
                    print(f"Ce livre est disponible en stock")
                else :
                    print("Ce livre n'est pas disponible en stock")
                print("----------")

    


