

from vehicule import Vehicule

class Voiture(Vehicule):

    portes = (3, 5)

    def __init__(self, nb_portes, immatriculation, couleur):
        self.nb_portes = nb_portes
        super().__init__(immatriculation, couleur)

    @property
    def nb_portes(self):
        return self.__nb_portes
    
    @nb_portes.setter
    def nb_portes(self, portes):
        if 3 == portes or 5 == portes:
            self.__nb_portes = portes
        else : 
            self.__nb_portes = False