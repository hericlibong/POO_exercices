
"""Définit les films.

Note: l'utilisation de l'héritage ici est surtout à but éducatif.
"""
from datas import films

class Film:
    """Film."""

    def __init__(self, name, date):
        """Initialise le nom et la date.

        L'attribut "where" permet de savoir où est un film.
        """
        self.name = name
        self.date = date
        self.where = None

    def __str__(self):
        return f"{self.name} ({self.date})"

    def __repr__(self) -> str:
        return str(self)


class FilmVHF(Film):
    """Film VHF."""

    type = "vhf"

    def __init__(self, name, date):
        """Initialise le type."""
        super().__init__(name, date)
        self.magnetic_tape = True


class FilmDVD(Film):
    """Film DVD."""

    type = "dvd"

    def __init__(self, name, date):
        """Initialise le type."""
        super().__init__(name, date)
        self.mega_octets = 4700


class FilmClean:
    """Génère un film à partir de données brutes."""

    NAME_AND_DATE_INDEX = 0
    TYPE_INDEX = 1

    def __init__(self, film_data):
        self.film_data = film_data

    def generate(self):
        """Génère le film."""
        name = self.generate_name()
        date = self.generate_date()
        type = self.generate_type()

        # ici on itère sur un tuple de classes (et non d'instances) !
        for Film in (FilmVHF, FilmDVD):
            # on vérifie le type du film par rapport au type de chaque classe
            if type == Film.type:
                # et on retourne un instance de la classe choisie.
                return Film(name, date)

    def generate_name(self):
        """Génère le nom."""
        name_date = self.film_data[self.NAME_AND_DATE_INDEX]
        if "(" in name_date:
            return name_date[:name_date.index("(")].strip()
        else:
            # Gérer le cas où "(" n'est pas présent
            return name_date.strip()


    def generate_date(self):
        """Génère la date."""
        name_date = self.film_data[self.NAME_AND_DATE_INDEX]
        date_with_parenthesis = name_date[name_date.index("(") :]
        date_letters = date_with_parenthesis.replace("(", "").replace(")", "")
        return int(date_letters)

    def generate_type(self):
        """Génère le type."""
        return self.film_data[self.TYPE_INDEX].lower()
    

data_film_cleaned = FilmClean(films)

cleaned_films = []

for film_data in films:
    cleaned_film = data_film_cleaned.generate()
    cleaned_films.append(cleaned_film)

for film in cleaned_films:
    print(film)





