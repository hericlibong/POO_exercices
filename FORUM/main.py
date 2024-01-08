


import time
from images import PNGImageFile
from moderator import Moderator
from user import User


def main():
    """Lance le code principal."""
    user = User("John", "superpassword")
    user_2 = User('Peter', "password")
    moderator = Moderator("Lucie", "helloworld")

    cake_thread = user.make_thread("Gâteau à la vanille 🍰 ???", "Vous aimez ou non ?")
    cake_thread.display()

    moderator.post(cake_thread, content="Oui j'aime beaucoup ! 😚")
    user_2.post(cake_thread, content='Bof!! Pas vraiment emballée ! 😕')
    cake_thread.display()

    irrelevant_post = user.post(cake_thread, content="Et vous aimez les voitures ?")
    response = moderator.post(cake_thread, content="C'est hors sujet sur ce forum 😕")
    cake_thread.display()

    print()
    print("après quelques minutes, le modérateur supprime les messages hors sujets...")
    print()
    # importer time n'était pas necessaire, c'est un plus:
    time.sleep(5)
    moderator.delete(cake_thread, irrelevant_post)
    moderator.delete(cake_thread, response)
    cake_thread.display()

    image = PNGImageFile(name="image de gâteau", size=3)
    user.post(cake_thread, content="Voici une image de mon gâteau !", file=image)
    moderator.post(cake_thread, "Woah, sublime !")
    cake_thread.display()

if __name__=='__main__':
    main()