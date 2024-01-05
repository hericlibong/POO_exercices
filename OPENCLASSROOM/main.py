# class Cake:
#     def __init__(self, flavor):
#         self.flavor = flavor 


# cake1 = Cake(flavor='Banana')
# print(cake1)
# print(cake1.flavor)



# class Bird:
#      names = ('mouette', 'pigeon', 'moineau', 'hirondelle')
#    ...:     positions = {}
#    ...:     def __init__(self, name):
#    ...:         self.position = 1, 2
#    ...:         self.name = name
#    ...:         self.positions[self.position] = self.name
#    ...:         @classmethod
#    ...:         def find_bird(cls, position):
#    ...:             if position in cls.positions:
#    ...:                 return f"on a trouvé un {cls.positions[position]}"
#              return "on a rien trouvé"


# class Bird:
#     """Un oiseau. 🐦"""

#     # ici on utilise deux attributs de classe.
#     names = ("mouette", "pigeon", "moineau", "hirrondelle")
#     positions = {}

#     def __init__(self, name):
#         """Les attributs définis ici sont des attributs d'instance."""
#         self.position = 1, 2
#         self.name = name
        
#         # On accède à l'attribut de classe "positions" avec self (c'est possible).
#         self.positions[self.position] = self.name

#     @classmethod
#     def find_bird(cls, position):
#         """Retrouve un oiseau selon la position donnée."""
#         if position in cls.positions:
#             return f"On a trouvé un {cls.positions[position]} !"

#         return "On a rien trouvé..."


# # On peut accéder aux variables de classe sans instanciation.
# Bird.names
# Bird.positions
# print(Bird.find_bird((1, 2)))

# # On instancie un oiseau
# bird = Bird("hirrondelle")

# # On le retrouve avec la méthode find_bird.
# print(Bird.find_bird((1, 2)))


class Toolbox:
    """Boite à outils """
   
    def __init__(self):
        """Initialise les outils """
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil"""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enlève un outil"""
        index = self.tools.index(tool)
        del self.tools[index]

    def __str__(self):

        if not self.tools:
            return "il n'y a pas d'outil dans la boite à outil"
        
        tool_list = "\n".join(str(tool) for tool in self.tools)
        return f" Outils dans la boite à outils : \n{tool_list}"


class Screwdriver:
    """Tournevis"""
    
    def __init__(self, size=3):
        """Initialise la taille"""
        self.size = size

    def tighten(self, screw):
        """Serrer une vis"""
        screw.tighten()

    def loosen(self, screw):
        """Desserrer une vis"""
        screw.loosen()

    def change_size(self, new_size):
        self.size = new_size
        print(f'nouvelle taille du tournevis: {self.size} cm')
    
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"
    

class Hammer:
    """Marteau"""


    def __init__(self, color="red"):
        """Initialise la couleur"""
        self.color = color
    
    def paint(self, color):
        """Paint le marteau"""
        self.color = color

    def hammer_in(self, nail):
        """Enfonce un clou"""
        nail.nail_in()

    def remove(self, nail):
        """Enleve un clou"""
        nail.remove()

    def __repr__(self):
        """Représentation de l'objet"""
        return f"Marteau de couleur {self.color}"


class Screw:
    """Vis"""

    MAX_TIGHTNESS = 5

    def __init__(self):
        """Initialise son degré de serrage"""
        self.tightness = 0
    
    def loosen(self):
        """Desserre la vis"""
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        """Serre la vis"""
        
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1
           
        else: 
            print(f'Vous dépassez la capacité de serrage maximum:{self.tightness}')





    

    def __str__(self):
        return "vis avec serrage de {}".format(self.tightness)


class Nail:
    """Clou"""
    total_nail = 0


    def __init__(self):
        """Initialise son statut 'dans le mur'. """
        self.in_wall = False
        Nail.total_nail +=1

    def nail_in(self):
        """Enfonce le clou dans un mur"""
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        """retire le clou du mur"""
        if self.in_wall:
            self.in_wall = False
    
    
    def __str__(self):
        """Retourne une forme visible de l'objet"""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"clou {wall_state}. Total de clous enfoncés dans le mur : {Nail.total_nail}" 
    
class Wrench:
    def __init__(self):
      pass  

    def __repr__(self):
        return 'Clé'

  

# Instanciez une boite à outil, un tournevis et un marteau
bte_outil = Toolbox()
tournevis = Screwdriver()
marteau = Hammer()

# Placez le tournevis et le marteau dans la boite à outil
bte_outil.add_tool(tournevis)
bte_outil.add_tool(marteau)

# Instanciez une vis, et serrez-la avec le tournevis. 
# Affichez la vis avant et après avoir été serrée.

vis = Screw()
print("Avant serrage:", vis)
vis.tighten() 
print("Après serrage:", vis)

#Instanciez un clou, puis enfoncez-le avec le marteau. 
# Affichez le clou avant et après avoir été enfoncé.

clou = Nail()
print("Non enfoncé", clou)
clou.nail_in()
print(clou)

# Ajout d'outils à la boîte à outils :
# Ajoutez un nouveau type d'outil, par exemple, une clé (Wrench), à la boîte à outils.
clé = Wrench()
bte_outil.add_tool(clé)

# Peindre le marteau :
# Utilisez la méthode paint de la classe Hammer pour changer la couleur du marteau et affichez la nouvelle couleur.

marteau.paint('noire')
print('la nouvelle couleur du marteau est :', marteau.color)

# Desserrage d'une vis :
# Instanciez une nouvelle vis.
# Utilisez le tournevis pour serrer la vis une fois.
# Utilisez le tournevis pour desserrer la vis et affichez l'état final de la vis.
vis2 = Screw()
vis2.tighten()
print('vis2 :', vis2)
vis2.loosen()
print('vis2', vis2)


# Retrait d'un clou avec le marteau :
# Instanciez un nouveau clou et enfoncez-le dans le mur avec le marteau.
# Utilisez le marteau pour retirer le clou et affichez l'état final du clou.
clou2 = Nail()
print('avant utilisation de clou2 :', clou2)
clou2.nail_in()
print('après utilisation de clou2:', clou2)
# clou2.remove()
# print('après seconde utilisation', clou2)

# Gestion des outils dans la boîte à outils :
# Affichez la liste des outils actuellement présents dans la boîte à outils.

# boucle for
for tool in bte_outil.tools:
    print('Dans la boite à outils il y a :  1', tool)
# affichage par défaut
print(bte_outil.tools)

# après ajout de la méthode
print(bte_outil)


# Modification de la taille du tournevis :
# Changez la taille du tournevis à 5 et affichez la nouvelle taille.
# tournevis.size = 5
# print('la taille du tournevis a été changé à :', tournevis.size)

tournevis.change_size(10)
#print(tournevis.size)



# Max Tightness pour la vis :
# Essayez de serrer la vis au-delà de sa capacité maximale (MAX_TIGHTNESS). Comment le programme réagit-il?

for _ in range(6):
    vis2.tighten()





# Enfoncer plusieurs clous :
# Utilisez une boucle pour instancier et enfoncer cinq clous avec le marteau.
for _ in range(5):
    clou = Nail()
print(clou)
marteau.hammer_in(clou)
print(clou)




# Retrait de tous les outils de la boîte à outils :
# Utilisez une boucle pour retirer tous les outils de la boîte à outils et affichez-les à mesure qu'ils sont retirés.
bte_outil.remove_tool(tournevis)
print(bte_outil)

#for tool in bte_outil:
# tool_in_box = [Hammer(), Wrench()]
# for tool in tool_in_box:
#     bte_outil.remove_tool(tool) 
# print(bte_outil) 



tool_in_box = [Hammer(), Wrench()]

# Utiliser une boucle pour retirer les outils un par un
for tool in tool_in_box:
    bte_outil.remove_tool(tool)

# Afficher l'état final de la boîte à outils
print(bte_outil)







# Interaction entre tournevis et marteau :
# Utilisez le tournevis pour serrer une vis.
# Ensuite, utilisez le marteau pour enfoncer un clou.
# Enfin, utilisez le tournevis pour desserrer la même vis. Que se passe-t-il?







