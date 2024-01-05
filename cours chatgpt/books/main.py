from bibliothèque import Bibliothèque
from livre import Livre
from utilisateur import Utilisateur

bibliothèque = Bibliothèque()

# Récupérer des données 
bibliothèque.get_data()

#Compter le nombre de livres présents dans la bibliothèque
bibliothèque.count_livres()

#Voir tous les titres de de tous les livres
bibliothèque.voir_livres()


print(bibliothèque.genres_disponibles())
bibliothèque.livres[0].stock = False
print(bibliothèque.livres[0].stock)
print(bibliothèque.livres[0].genre)
#bibliothèque.afficher_fiches()
bibliothèque.recherche_par_genre('Bandes dessinées')
# bibliothèque.livre_par_annee(2019)
#bibliothèque.livres_par_annee_disponibles()
nouveau_livre = Livre(titre='Mourir peut attendre', auteur='Medzi_O', ISBN='9782753657811', genre='Policier', prix = 19.2, pub_year=2022, stock=False)
bibliothèque.add_livre(nouveau_livre)
bibliothèque.get_random_books()
bibliothèque.sort_by_name()
bibliothèque.sort_and_display_by_name()
bibliothèque.livre_par_auteur()

#je  crée un nouveau livre
#bibliothèque.recherche_par_auteur('Medzi_O')
bibliothèque.recherche_livre_par_critere('prix', 20)

utilisateur_1 = Utilisateur(prenom='Héric', nom='Libong')
utilisateur_1.create_pseudo('rico69')
utilisateur_2 = Utilisateur(prenom='Pauline', nom='Ngom')
utilisateur_2.create_pseudo('pol2')
for user in Utilisateur.utilisateurs_inscrits:
    print(user.pseudo)

utilisateur_1.emprunter_livre("Il ne doit plus jamais rien m'arriver")
utilisateur_2.emprunter_livre("Les désobéissantes")
utilisateur_3 = Utilisateur(prenom='Agate', nom= 'Peter')
utilisateur_3.emprunter_livre("L'ombre des pins")
print(utilisateur_3.pseudo)
