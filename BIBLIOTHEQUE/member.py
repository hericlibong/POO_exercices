



class Member:
    """création des Membres"""


    members_list = []

    def __init__(self, nom):
        """Initialise le nom de membre"""
        self.nom = nom
        self.livre_emprunte = []
        Member.members_list.append(self)

    def __str__(self):
        return self.nom

    



        

        

        