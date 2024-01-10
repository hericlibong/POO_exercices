from livre import Livre

class Bibliothèque:
    """construire de la bibliothèque"""
 
    @classmethod
    def emprunter_livre(cls, member, titre_livre):
        """Emprunter un livre"""
        livre_trouve = None

        for livre in Livre.list_livres:
            if livre.titre == titre_livre: 
                livre_trouve = livre
                if livre.available:
                    
                    print(f"Le livre {livre.titre} a été emprunté par {member.nom}")
                    
                    livre.available = False
                    member.livre_emprunte.append(livre)
                else :
                    print(f"Le livre '{livre.titre}' n'est pas disponible")
                break
        if livre_trouve is None:
            print(f"Le livre '{titre_livre}' n'a pas été trouvé")
    
    @classmethod
    def retourner_livre(cls, member, titre_livre):
        """Retourner le livre"""
        for livre in Livre.list_livres:
            if livre.titre == titre_livre and livre in member.livre_emprunte:
                print(f"Le livre '{livre.titre}' a été retourné par {member.nom} et il est de nouveau disponible")
                livre.available = True
                member.livre_emprunte.remove(livre)
                break
        else:
            print(f"Le livre '{titre_livre}' ne peut pas être retourné (non emprunté)")