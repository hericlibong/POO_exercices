
class Clio():
    """cree la voiture"""

    doors = (3, 5)
    colors = {
        'black': '#000000',
        'white': '#FFFFFF',
        'red':	'#FF0000',
        'blue': '#0000FF',
        'silver':'#C0C0C0'
    }
    price_range =[8000, 30000]
    price = 20000


    def __init__(self, num_doors, color, code_color ):
        self.__color = color
        self.__num_doors = num_doors
        self.__code_color = code_color

    @property
    def number_doors(self):
        return self.__num_doors
    
    @number_doors.setter
    def number_doors(self, number_doors) :
        if number_doors in Clio.doors :
            self.__num_doors = number_doors
        else :
            raise ValueError  
        

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        if new_color in Clio.colors.keys():
            self.__color = new_color
        else : 
            raise ValueError
        

    @property
    def code_color(self):
        return self.__code_color
    
    @code_color.setter
    def code_color(self, new_code_color):
        if new_code_color in Clio.colors.values():
            self.__code_color = new_code_color
        else : 
            raise ValueError("le code couleur n'est pas le bon")


    @classmethod
    def checkprice(cls):
        if cls.price in range (8000, 30000):
            return cls.price
        else :
            raise ValueError


        

        