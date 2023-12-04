'''
Создать класс Country: Столица, Площадь, Численность населения.
Создать список объектов. Вывести:
a) список стран по заданной площади;
b) список стран по заданной численности населения.
'''

class Country:

    def __init__(self, name, capital, area, population):
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population


countries = [
    Country("РБ", "Минск", 34567, 12493849),
    Country("РФ", "Москва", 298565643, 2082438),
    Country("Южная Корея", "Сеул", 839483767, 9283283)
]

selected_area = 1000000
countries_by_area = [country.name for country in countries if country.area > selected_area]
print(f"список стран с площадью больше {selected_area} : {countries_by_area}")


selected_population = 1000000
countries_by_population = [country.name for country in countries if country.population > selected_population]
print(f"список стран по численностью населения больше {selected_population}: {countries_by_population}")
