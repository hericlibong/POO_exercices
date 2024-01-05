import string
import random


class PasswordGenerator:

    @staticmethod
    def generate(length):
        return "".join(random.sample(string.digits + string.ascii_letters, length))


mot_de_passe = PasswordGenerator.generate(15)