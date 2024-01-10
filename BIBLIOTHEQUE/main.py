from livre import Livre
from member import Member
from bibliothèque import Bibliothèque


def main():
    #creation de la bibliothèque
    bibli = Bibliothèque()

    #creation de livres
    livre_1 = Livre('Silver', 'James Joyce', '#34567')
    livre_2 = Livre('Flagrant délit', 'Henry Paul', '#29076', available = False)

    #Affichage d'un livre
    livre_1.affiche_livre()
    print("--------")

    #afficher tous les livres présents
    Livre.afficher_livres()
    
    #Creation de membres
    member_1 = Member("Josepha")
    member_2 = Member('Adrien')
    
    # emprunt de livres
    bibli.emprunter_livre(member_1, 'Silver') # le livre "---" a été emprunté par Josepha
    
    
    bibli.emprunter_livre(member_2, 'Flagrant délit') # output : le livre "---" n'est pas disponible (avalaible=False)
    bibli.emprunter_livre(member_2, 'Le bruit et la fureur')# output : le livre "---" n'a pas été trouvé

    
    print('---------')
    bibli.emprunter_livre(member_2, 'Silver') # output : le livre "---" n'est pas disponible (déjà emprunté)

    #retourner le livre
    bibli.retourner_livre(member_1, 'Silver')
    bibli.emprunter_livre(member_2, 'Silver')
    

if __name__ == "__main__":
    main()