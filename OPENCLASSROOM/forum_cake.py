class File:
    """classe du fichier"""
    def __init__(self, name, size):
        """initialise le nom et la taille"""
        self.name = name
        self.size = size

    def display(self):
        print(f" Fichier : {self.name}")

class Image(File):
    """image du fil de discussion et qui pourra faire l'objet de commentaires"""
    pass


class User:
    """Utilisateur"""
    def __init__(self, username, password):
        """Initialise le username et le password"""
        self.username = username
        self.password = password

    def login(self):
        """Affiche l'utilisateur connecté"""
        print(f"L'utilisateur {self.username} est connecté")
    
    def post(self, thread, content, file = None):
        """Poste un message sur le fil de discussion"""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else :
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post 
    
    
    def make_thread(self, title, content):
        """Créé un nouveau fil de discussion"""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)
    
    def __str__(self):
        """représentation de l'utilisateur"""
        return self.username

class Moderator(User):
    """Creation de la classe moderateur"""

    def edit(self, post, content):
        """Editer un post"""
        post.content = content
    
    def delet(self, thread, post):
        """Supprimer un post"""
        index = thread.posts.index(post)
        del thread.posts[index]
        

class Post:
    """Création de la class post"""
    def __init__(self, user, time_posted, content):
        """initialise le user, la date et le contenu"""
        self.user = user
        self.time_posted = time_posted
        self.content = content
    
    def display(self):
        """Affiche le message"""
        print(f"posté par {self.user} | date : {self.time_posted}")
        print(f"texte : {self.content}")

class FilePost(Post):
    """Message comportant un fichier"""
    def __init__(self, user, time_posted, content, file):
        self.user = user
        self.time_posted = time_posted
        self.content = content
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier"""
        super().display()
        print('pièce jointe :')
        self.file.display()


class Thread :
    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts.

        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)
        """
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """Display information of the thread"""
        print('----NewsWire Thread----')
        print(f'Titre : {self.title} | Date : {self.time_posted}')
        print()
        for post in self.posts:
            post.display()
            print()
        print('---------')

    def add_post(self, post):
        """Ajouter un post"""
        self.posts.append(post)



#Exercice 1 : Créez un utilisateur, postez un message simple dans un fil de discussion 
# et affichez le fil de discussion.

#Création d'un utilisateur       
utilisateur_1 = User(username='heric', password='S@cr#t')
#représentation de l'utilisateur
print(utilisateur_1)
#connexion de l'utilisateur
utilisateur_1.login()
#creation d'un post
post_1 = Post(user=utilisateur_1, time_posted="hier", content="une recette du pudding aux oranges sans oranges" )
#affichage du post
post_1.display()

print("------")

#Exercice 2 : Créez un fil de discussion, postez un message avec un fichier joint, 
#puis affichez le fil de discussion

#Creation d'un nouveau fil par utilisateur_1
new_fil = utilisateur_1.make_thread(title="1 Nouveau fil", content="série de recettes de pudding")

#Création d'un fichier
file_1 = File(name='portrait', size= 20)

utilisateur_1.post(new_fil, content='pudding recette_1', file=file_1).display()
# print('ex2 affichage bis-------')
# new_fil.display()
print('-----------')
print('Exercice 3')
#Exercice 3 : Ajoutons un utilisateur modérateur et testons ses fonctionnalités. 
#Tu peux suivre ces étapes :

# 1- Crée un utilisateur modérateur avec un nom d'utilisateur et un mot de passe.
moderateur_1 = Moderator(username='mod1', password='S@cret')
# 2 - Connecte l'utilisateur modérateur.
moderateur_1.login()
# 3 - Modifie le contenu d'un post existant dans le fil de discussion.
moderateur_1.edit(post=post_1, content='une recette de pudding avec des oranges')
# 4 - Supprime un post existant dans le fil de discussion.
# moderateur_1.delet(thread = new_fil, post=post_1)
# # 5 - Affiche le fil de discussion pour vérifier les modifications.
post_1.display()
new_fil.display()


















