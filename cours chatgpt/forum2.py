

class Utilisateur:
    """Utilisateur"""
    def __init__(self, username, password):
        """initialise le username, le password et l'état de l'utilisateur"""
        self.username = username
        self.password = password
        self.connecte = False
        self.role = 'utilisateur'

    def login(self):
        """Connecte un utilisateur"""
        if not self.connecte:
            print(f"{self.username} est connecté en tant que {self.role} ")
            self.connecte = True
        else:
            print(f"L'utilisateur {self.username} est déjà connecté ")

    def se_deconnecter(self):
        """Se déconnecter du forum"""
        if self.connecte:
            print(f"L'utilisateur {self.username} s'est déconnecté avec succès ")
            self.connecte = False
        else:
            print(f"L'utilisateur {self.username} n'est pas connecté ")

    def __str__(self):
        if self.connecte:
            return f"Bienvenue, {self.username} Vous êtes connecté et vous pouvez publier"
        else:
            return "Vous devez vous connecter pour publier."

class Post:
    """Post de forum"""
    def __init__(self, titre, utilisateur, date):
        """Initialize le texte, l'utilisateur et la date, l'attaachement du fichier"""
        self.titre = titre
        self.utilisateur = utilisateur
        self.date = date
        self.fichier_attaches = []

    def attached_file(self, fichier):
        self.fichier_attaches.append(fichier)

    def update_utilisateur(self, utilisateur):
        self.utilisateur = utilisateur    

    def __str__(self):
        return f"titre : {self.titre}, utilisateur : {self.utilisateur.username}, date : {self.date}"
    
class Reponse:
    """Reponses aux commentaires"""
    def __init__(self, texte, utilisateur, date):
        """initialise le texte, l'utilisateur et la date de la reponse à un commentaire"""
        self.texte = texte
        self.utilisateur = utilisateur
        self.date = date

class Commentaire:
    """Commentaires du fil de discussion"""
    def __init__(self, texte, utilisateur, date):
        """initialise le texte, l'utilisateur et la date des commentaires du fil"""
        self.texte = texte
        self.utilisateur = utilisateur
        self.date = date
        self.reponses = []

    def ajouter_reponse(self, reponse):
        self.reponses.append(reponse)
        print('Votre réponse a été ajouté au commentaire')

    def afficher_reponses(self):
        if self.reponses:
            print('Réponse au commentaire :')
            for reponse in self.reponses:
                print(f"\t{reponse.texte} par ({reponse.utilisateur} - le {reponse.date}")
        else :
            print("Ce commentaire n'a de commentaire")


class FilDiscussion : 
    """Fil de discussion"""
    def __init__(self, titre, utilisateur, date):
        """Initialise le titre, l'utilisateur et la date du fil de discussion"""
        self.titre = titre
        self.utilisateur = utilisateur
        self.date = date
        self.commentaires = []

    def ajouter_commentaire(self, commentaire):
        self.commentaires.append(commentaire)
        print("Votre commentaire a été ajouté au fil")
    
    def afficher_commentaires(self):
        for comment in self.commentaires:
            print(comment.texte)

class Moderateur(Utilisateur):
    """Classe Moderateur qui hérite d'utilisateur"""
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "moderateur"

    # def login(self):
    #     """Connecte un utilisateur"""
    #     if not self.connecte:
    #         print(f"{self.username} est connecté en tant que {self.role} ")
    #         self.connecte = True
    #     else:
    #         print(f"L'utilisateur {self.username} est déjà connecté ")

    def modifier_post(self, post, nouveau_contenu):
        """modifie le contenu"""
        if self.connecte:
            post.titre = nouveau_contenu
            print(f'le contenu de ce post a été modifié par {self.username}')
            return post
        else :
            print('Vous devez être connecté en tant que moderateur pour modifier le post')
            return post


    def supprimer_post(self, post):
        """supprimer le post"""
        if self.connecte:
            post.supprimer()
            print(f'le post a été supprimer par {self.username}')
        else : 
            print('vous devez être connecté en tant que modérateur pour supprimer ce post')



        
#Création d'utilisateurs
        
heric = Utilisateur(username='rico', password='##@123')
print(heric)
heric.login()
post1 = Post(titre = "Recette du PaneCake", utilisateur=heric, date ='2023-01-01')
post1.update_utilisateur(heric)
print(post1)

print('---------')

# Test fil de discussion et commentaires

# Créer un fil de discussion
discussion1 = FilDiscussion(titre = 'Ajout beurre sauce béarnaise', utilisateur ='flo', date = '2023-01-01')
#Créer un commentaire 
comment1 = Commentaire(texte="un très long texte sur la sauce béarnaise",utilisateur='john', date ='2023-01-01' )
#ajouter un commentaire au fil de discussion
discussion1.ajouter_commentaire(comment1)

#Nouveau fil de discussion
discussion2 = FilDiscussion(titre="Attention aus crevettes", utilisateur="adrien", date="2023-01-02")
#Création de deux nouveaux commentaires
comment2 = Commentaire(texte="untrès long texte sur les crevettes", utilisateur='lory',  date='2023-01-02')
comment3 = Commentaire(texte="un très long texte pas d'accord avec le premier sur les crevettes", utilisateur="pat", date= "2023-01-02")
#Ajouter les 2 commentaires au nouveau fil de discussion
discussion2.ajouter_commentaire(comment2)
discussion2.ajouter_commentaire(comment3)
#Afficher les commentaires du nouveau fil de discussion
discussion2.afficher_commentaires()
#Afficher une reponse à au commentaire 3
#Créer une réponse
response1 = Reponse(texte = "Je ne suis pas d'accord avec toi", utilisateur='ben', date= '2023-01-03')
#Ajouter la réponse au commentaire 3
comment3.ajouter_reponse(response1)
#Afficher la réponse du commentaire
comment3.afficher_reponses()

print('---------------')
# créer un modérateur
mode_1 = Moderateur(username='fredo', password='@@president1')
#tentez de modifier un post sans être connecté
mode_1.modifier_post(post1, nouveau_contenu="Recette du Panecake avec des anchois")
#connecter le moderateur
mode_1.login()
# modifie un post
print(post1)
mode_1.modifier_post(post1, nouveau_contenu ="Recette du Panecake avec des anchois")
print(post1)













    