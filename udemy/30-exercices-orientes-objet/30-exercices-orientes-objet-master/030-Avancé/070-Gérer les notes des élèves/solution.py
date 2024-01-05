class Note:
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return "{} / 20".format(str(self.valeur))


class Notes(list):
    def ajouter_note(self, note):
        self.append(note)

    def notes_parfaites(self):
        nombre = 0
        for note in self:
            if note.valeur == 20:
                nombre += 1

        return nombre

    def moyenne(self):
        return round(sum([note.valeur for note in self]) / len(self), 1)


valeur_notes = [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17]
notes = Notes()

for valeur_note in valeur_notes:
    notes.ajouter_note(note=Note(valeur=valeur_note))

print(notes.notes_parfaites())
print(notes.moyenne())