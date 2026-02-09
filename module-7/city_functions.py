def city_country(city, country, *args):
    
    return f"{city}, {country} {', '.join(args)}"



print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan", "Population: 37 million"))
print(city_country("New York", "United States", "Population: 8.4 million", "Language: English"))
print(city_country("Sydney", "Australia"))
print(city_country("Barcelona", "Spain", "Population: 1.6 million"))
