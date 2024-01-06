
from customer import Customer
from employe import Employe
from product import Product




"""script launch"""
if __name__ == "__main__":

    """we attribute values to the attributes of the Customer 
    class and we measure them with the format method"""
    c = Customer("charles", "chalgoumi", 39, "vélo", 100)
    customer = ("Idendités complétes du client:\n nom: {}\n prénom: {}\n age: {} ans\n panier: {}\n montant: {}€".format(c.firstname, c.lastname, c.year, c.basket, c.amount))
    print(customer)

    print("--------------------------------------------------------")

    """we attribute values to the attributes of the Employee 
    class and we measure them with the format method"""
    e = Employe("boules", "praliné", 24, "cadre")
    employe = ("Idendités complétes de l'employé:\n nom: {}\n prénom: {}\n age: {} ans\n statut: {}".format(e.firstname, e.lastname, e.year, e.statut))
    print(employe)