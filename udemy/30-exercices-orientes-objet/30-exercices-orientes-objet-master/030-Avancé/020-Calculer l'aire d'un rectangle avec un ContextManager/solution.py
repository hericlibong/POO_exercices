class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    def __enter__(self):
        print("L'aire d'un rectangle de {}m par {}m est de :".format(self.longueur, self.largeur))
        return self
        
    def __exit__(self, exception_type, exception_value, callback):
        print("{}m2".format(self.aire))
    
    def calcul_aire(self):
        self.aire = self.longueur * self.largeur

with Rectangle(6, 12) as r:
    r.calcul_aire()