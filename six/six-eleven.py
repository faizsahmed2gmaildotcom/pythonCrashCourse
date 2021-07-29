cities = {
    'Baskerville': {
        'name': 'Baskerville',
        'population': 3,
        'fact': 'This place has the central freeway.',
    },
    'Fugging': {
        'name': 'Fugging',
        'population': 696969,
        'fact': 'Used to be called something... else',
    },
    'Bill': {
        'name': 'Bill',
        'population': 4444,
        'fact': "Bob's favourite Bill.",
    },
}

for cityNumber, city in cities.items():
    print(f"Name: {city['name']}")
    print(f"Population: {city['population']}")
    print(f"Fact: {city['fact']}\n")
