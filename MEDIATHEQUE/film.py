

class Film:
    """création de la classe film"""
    def __init__(self, name, created_date):
        """
        Initialise le nom du film et sa date de création
        l'attribut where permet de savoir où se trouve le film

        """
        self.name = name
        self.created_date = created_date
        self.where = None

    def __str__(self):
        return f"{self.name}, ({self.created_date})"
    
    def __repr__(self) -> str:
        return str(self)
    
class FilmVHF(Film):
    """Film VHF"""

    type = 'vhf'
    
    def __init__(self, name, created_date):
        "Initialise le type de film vhf"
        super().__init__(name, created_date)
        self.magnetic_tape = True


class FilmDVD(Film):
    """Film DVD"""

    type = 'dvd'

    def __init__(self, name, created_date):
        """Initialise le type de film dvd"""
        super().__init__(name, created_date)
        self.mega_octets = 4900
    

