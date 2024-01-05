class Lampe:
    """Lampe"""
    def __init__(self, couleur, luminosite=50):
         


        self._couleur = couleur
        self._allumee = False
        self._luminosite = luminosite

    @property
    def couleur(self):
        return self._couleur
    
    @property
    def allumee(self):
        return self._allumee
    
    @property
    def luminosite(self):
        return self._luminosite
    

    def allumer(self):
        """Allume la lampe"""
        self._allumee = True
        print(f"La Lampe {self.couleur} est maintenant allumée. Luminosité : {self.luminosite}%")

    def eteindre(self):
        """Eteindre la lampe"""
        self._allumee = False
        print(f"la lampe {self.couleur} est maintenant éteinte")

    def ajuster_luminosite(self, nouvelle_luminosite):
        if self.allumee:
            self._luminosite = nouvelle_luminosite
            print(f"Luminosité ajustée à {self.luminosite}%.")
        else :
            print("La lampe doit être allumée pour ajuster la luminosité")
    
    def __str__(self):
        etat = "allumé" if self.allumee else "eteinte"
        return f"Lampe de couleur {self.couleur}, {etat}, luminosité : {self.luminosite}"

    def __repr__(self):
        return f"Lampe(couleur='{self.couleur}', allumee={self.allumee}, luminosite={self.luminosite})"
    



lampe = Lampe('rouge')
print(lampe.couleur)
lampe.allumer()
lampe.eteindre()

print("------")

lampe2 = Lampe('bleue')
#print(lampe2.couleur)
lampe2.allumer()
lampe2.ajuster_luminosite(nouvelle_luminosite=80)
lampe2.eteindre()

print("-------")

lampe3 = Lampe(couleur='verte')
print(lampe3.couleur)
print(lampe3.allumee)
print(lampe3.luminosite)
lampe3.allumer()
lampe3.ajuster_luminosite(nouvelle_luminosite=75)
lampe3.eteindre()
print(lampe3.allumee)


print("-------")

# Utiliser la méthode '__str__' pour personnaliser l'affichage de la classe "Lampe".
Lampe4 = Lampe(couleur="jaune")
print(Lampe4)
Lampe4.allumer()
print(Lampe4)
Lampe4.ajuster_luminosite(nouvelle_luminosite=20)
print(Lampe4)

print('------')

#Utilise la méthode "__repr__" pour personnaliser 
#la représentation détaillée de la classe "Lampe"


lampe5 = Lampe(couleur="violette")
repr(lampe5)

print('--------')

lampe6 = Lampe(couleur="jaune", luminosite=90)
print(lampe6)
lampe6.ajuster_luminosite(nouvelle_luminosite='120')
print(lampe6.luminosite)

lampe6.ajuster_luminosite(nouvelle_luminosite=120)
print(lampe6)



    