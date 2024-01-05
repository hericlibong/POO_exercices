class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self._numero = numero
        self.balance = balance

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        raise AttributeError("Vous ne pouvez pas modifier le numéro du compte.")


john = Compte(nom="John Smith", numero="123456", balance=20000)