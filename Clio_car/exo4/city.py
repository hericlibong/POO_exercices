"""Ecriture d'une classe représentant une ville."""

class City:
    """definition de la classe City"""
    def __init__(self, name, dpt_name, dpt):
        """Initialise name et dpt de la ville"""
        self.name = name
        self.dpt_name = dpt_name
        self.dpt = dpt

    
    def show_location(self):
        print(f"la ville de {self.name} est dans le département du {self.dpt_name}, n°: {self.dpt}")
    