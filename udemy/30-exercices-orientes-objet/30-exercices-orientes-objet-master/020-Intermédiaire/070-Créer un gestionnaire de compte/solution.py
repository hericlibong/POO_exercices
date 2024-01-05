class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance

    def deposer(self, montant):
        self.balance += montant

    def retirer(self, montant):
        self.balance -= montant


compte_john = Compte(nom="John", numero="12345", balance=20000)
compte_john.deposer(montant=3000)
compte_john.retirer(montant=200)