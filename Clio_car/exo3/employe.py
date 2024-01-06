from person import Person


class Employe(Person):
    def __init__(self, firstname, lastname, year, statut):
        self.statut = statut
        super().__init__(firstname, lastname, year)

        