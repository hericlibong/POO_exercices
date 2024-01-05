class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parle(self):
        raise NotImplementedError("Je ne sais pas quoi dire...")


class Chien(Animal):
    def parle(self):
        return "Woof!"


class Chat(Animal):
    def parle(self):
        return "Miaou!"


a = Animal("Patrick")
chat = Chat("Titi")
chien = Chien("Max")

print(chat.parle())
print(chien.parle())