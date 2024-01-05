class Chemin:
    def __init__(self, chemin):
        self.chemin = chemin

    def __str__(self):
        return self.chemin


c = Chemin("/Users/john")
composite = c + "dossier" + "test" + "script"
print(composite)