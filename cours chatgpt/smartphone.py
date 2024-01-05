class Smartphone:
    """Smartphone"""
    def __init__(self, marque, modele, etat_batterie=100):
        """initialisee la marque, le modele, et l'état de la batterie"""
        self.marque = marque
        self.modele = modele
        self.etat_batterie = etat_batterie

    def envoyer_message(self, destinataire, message):
        """Envoyer message"""
        print(f"Message envoyé à {destinataire}:{message}")
        
    def prendre_photo(self):
        """Prendre photo"""
        print("Photo prise!")
    
    def consulter_batterie(self):
        """Consulter la batterie"""
        print(f"Niveau de batterie : {self.etat_batterie}")

class TelephonePortable(Smartphone):
    """Telephone portable qui hérite de smartphone"""
    def __init__(self, marque, modele, numero, etat_batterie=100):
        super().__init__(marque, modele, etat_batterie)
        self.numero = numero
    
    def passer(self, destinataire):
        """Passe un appel"""
        print(f"appel en cours vers {destinataire}...")



mon_smartphone = Smartphone(marque = 'Samsung', modele="A22")
mon_smartphone.envoyer_message("Héric", "Bonjour, Comment vas-tu?")
mon_smartphone.prendre_photo()
mon_smartphone.consulter_batterie()

print('--------')

telephone_portable = TelephonePortable(marque = 'Nokia', modele='T244', etat_batterie=80, numero='0745735625')
telephone_portable.envoyer_message("Paul", "il fait beau temps aujourd'hui")
telephone_portable.prendre_photo()
telephone_portable.consulter_batterie()
telephone_portable.passer("Corinne")