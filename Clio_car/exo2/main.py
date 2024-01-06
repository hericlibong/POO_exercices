from voiture import Voiture
from vehicule import Vehicule
from bus import Bus

if __name__== "__main__":


    bus_1 = Bus("EXV104", 'rouge', 1)
    print(f"Le bus immatriculé '{bus_1.immatriculation}' de couleur '{bus_1.couleur}' a '{bus_1.nombre_etages}' étage ")
    print(bus_1)
    voiture_1 = Voiture("TZ285", 'bleue', 5)
    print(f"La voiture immatriculé '{voiture_1.immatriculation}' de couleur '{voiture_1.couleur}' a '{voiture_1.nb_portes}' portes ")
    print(voiture_1)

