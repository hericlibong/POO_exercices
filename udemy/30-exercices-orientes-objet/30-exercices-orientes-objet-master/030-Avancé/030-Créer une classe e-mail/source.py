class Email:
    def __init__(self, content):
        self.content = content
        self.is_sent = False

email = Email(content="La nouvelle formation est disponible !")
response_01 = email.send_to(email="JohnSmith@gmail.com")
response_02 = email.send_to(email="JohnSmith@gmail.com")