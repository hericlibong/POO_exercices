class Film:

    def __init__(self, name):
        self.name = name

    def watch(self, player):
        """Regarder le film"""
        print('Bon visionage !!')

class FilmCassette(Film):
    """Un film en cassette"""
    def __init__(self, name, magnetic_tape=True):
        """Initialise la bande magnétique, le nom, l'année de sortie"""
        super().__init__(name)
        self.magnetic_tape = magnetic_tape
    
    def rewind(self):
        """rembobine le film une fois le film terminé"""
        print("Ce film est long à rembobiner!!")
        self.magnetic_tape = True 

    def watch(self, player):
        if player.type != 'cassettes':
            print("le lecteur n'est pas un lecteur de cassettes!"
                  "Vous en trouverez peut-être un au grenier")
        else :
            print("La lecture peut commencer")
        super().watch()

    
    

class FilmDvd(Film):
    def __init__(self, name):
        """Initialize le nom du film et le menu"""
        super().__init__(name)
        self.menu = True
    
    def display_menu(self):
        """affiche ou non un menu"""
        if self.menu ==False:
            print('Ce dvd ne possède pas de menu')
        else :
            print('Vous pouvez dérouler le menu du DVD') 

        




film = Film("2001: l'Odyssé de l'espace")
film_cassette = FilmCassette('Blade Runner')
film_dvd = FilmDvd(name='Superman Return', menu=False)

print(film.name)
film.watch()


print(film_cassette.name)
film_cassette.watch()
film_cassette.rewind()

print(film_dvd.name)
film_dvd.watch()
film_dvd.display_menu()



