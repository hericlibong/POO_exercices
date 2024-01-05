import random
import string


class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance
        self.virements = {}

    def virement(self, montant):
        self.balance += montant
        uuid = "".join(random.sample(string.digits + string.ascii_letters, 15))
        self.virements[uuid] = montant


john = Compte(nom="John Smith", numero="123456", balance=20000)
john.virement(montant=5000)