class Email:
    number_of_mails_sent = 0

    def __init__(self, content):
        self.content = content
        self.is_sent = False

    def send_to(self, email):
        if not self.is_sent:
            self.is_sent = True
            Email.number_of_mails_sent += 1
            return "E-mail envoyé"
        return "L'e-mail a déjà été envoyé"

email = Email(content="La nouvelle formation est disponible !")
response_01 = email.send_to(email="JohnSmith@gmail.com")
response_02 = email.send_to(email="JohnSmith@gmail.com")