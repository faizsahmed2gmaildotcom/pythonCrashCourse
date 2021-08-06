def describeCity(city, country):
    print(f"{city.title()}, {country.title()}")

for i in range(3):
    inputCity = input("City?")
    inputCountry = input("Country?")
    describeCity(inputCity, inputCountry)
