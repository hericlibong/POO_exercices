#from cities import cities_list
class Base:
    cities_list = []

    def load_data(self):
        for city_data in self.cities_list:
            city = City(**city_data)
            Base.cities_list.append(city)
            

class City:

    def __init__(self, name, department, country, population, mayor, capital):
        self.name = name
        self.department = department
        self.country = country
        self.population = population
        self.mayor = mayor
        self.capital = capital
        

    def __repr__(self):
        return f"{self.name} \n {self.department} \n {self.country} \n {self.population} \n {self.mayor} \n {self.capital}"
    
    



   


