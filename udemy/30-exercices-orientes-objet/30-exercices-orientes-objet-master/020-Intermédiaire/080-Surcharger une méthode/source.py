class Animal:
    def __init__(self, nom):
        self.nom = nom


class Chien(Animal):
    pass


class Chat(Animal):
    pass


a = Animal("Patrick")
chat = Chat("Titi")
chien = Chien("Max")

print(chat.parle())
print(chien.parle())