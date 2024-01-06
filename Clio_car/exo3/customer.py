from person import Person


class Customer(Person):
    """definit un client"""
    basket = []
    amount = 0

    def __init__(self, firstname, lastname, year, basket, amount):
        self.basket = basket
        self.amount = amount
        super().__init__(firstname, lastname, year)
