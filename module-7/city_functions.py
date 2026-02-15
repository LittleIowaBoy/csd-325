def city_country(city, country, population=None, language=None):
    parts = [f"{city}, {country}"]
    if population:
        parts.append(f"Population: {population}")
    if language:
        parts.append(f"Language: {language}")
    return ", ".join(parts)



print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan", population="37 million"))
print(city_country("New York", "United States", population="8.4 million", language="English"))
print(city_country("Sydney", "Australia"))
print(city_country("Barcelona", "Spain", population="1.6 million"))
