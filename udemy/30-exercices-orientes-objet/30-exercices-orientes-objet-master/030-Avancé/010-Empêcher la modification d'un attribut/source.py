class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance

john = Compte(nom="John Smith", numero="123456", balance=20000)