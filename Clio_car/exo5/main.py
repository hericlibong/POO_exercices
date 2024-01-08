from city import City, Base
from cities import cities_list


for city_data in cities_list:
    city = City(**city_data)
    Base.cities_list.append(city)
    print(city.name)