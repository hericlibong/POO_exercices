# Création de blog spécialisé dans la cuisine


class File:
    """Fichier"""
    def __init__(self, name, size):
        """Initialize le nom et la taille du fichier"""
        self.name = name
        self.size = size


    
    def display(self):
        """Affiche le fichier."""
        print(f"Fichier '{self.name}'.")

class Image(File):
    """ fichier Image"""
    pass
    

class User:
    """Utilisateur"""
    
    def __init__(self, username, password):
        """Initialize le nom d'utilisateur et le mot de passe"""
        self.username = username
        self.password = password

    def login(self):
        """connecte un utilisateur"""
        print(f"L'utilisateur {self.username} est connecté ")
    
    def post(self, thread, content, file = None):
        """Poste un message dans un fil de discussion """
        if file :
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
        """Représentation de l'utilisateur"""
        return self.username



class Moderator(User):
    
    def __init__(self):
        """rien pour l'instant"""

    def edit(self, post, content):
        """Editer le post"""
        post.content = content
    
    def delete(self, thread, post):
        """supprime un message"""
        index = thread.posts.index(post)
        del thread.posts[index]



class Post:

    def __init__(self, user, time_posted, content):
        """Initialize l'utilisateur, la date et le contenu """
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """affiche le post"""
        print(f"Message posté par {self.user} - le {self.time_posted}")
        print(f" Contenu : {self.content}")


class FilePost(Post):
    """fichier de la discussion"""
    def __init__(self, file):
        """initialise le Ficher de la discussion"""
        self.file = file



class Thread:
    """fil de discussion"""
    def __init__(self, title, time_posted, post):
        """initialise le titre, la date et les posts"""
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """Affiche le fil de discussion"""
        print("-----THREAD----")
        print(f"titre : {self.title}, date : {self.time_posted} ")
        print()
        for post in self.posts:
            post.display()
            print()
        print("-------------------")
    
    def add_posts(self, post):
        """Ajouter un post"""
        self.posts.append(post)

    
    



    



    
# user1 = User('Heric', 'Secret')

# print(user1.username)
# print(user1.password)
# user1.login()

# file = File('cookie', 5)

# file.display()

