
from vehicule import Vehicule


class Bus(Vehicule):
    

    etages = (1, 2)

    def __init__(self, nombre_etages, immatriculation, couleur):
        self.nombre_etages = nombre_etages
        super().__init__(immatriculation, couleur)

    @property
    def nombre_etages(self):
        return self.__nombre_etages
    
    @nombre_etages.setter
    def nombre_etages(self, etage):
        if 1 == etage or 2 == etage:
            self.__nombre_etages = etage
        else :
            self.__nombre_etages = False
    
