favPlaces = {
    "Bill": {
        'name': 'Bill',
        'placeOne': 'Bas',
        'placeTwo': 'Oof',
        'placeThree': 'Aaa',
    },
    "Bob": {
        'name': 'Bob',
        'placeOne': 'Kerville',
        'placeTwo': 'Bulgaria',
        'placeThree': 'poopoo',
    },
    "Jeff": {
        'name': 'Jeff',
        'placeOne': 'Place',
        'placeTwo': 'Area',
        'placeThree': 'City'
    }
}

for favNumber, favInfo in favPlaces.items():
    print(f"{favInfo['name']}'s Favourite Places: \n{favInfo['placeOne']}")
    print(f"{favInfo['placeTwo']}")
    print(f"{favInfo['placeThree']}\n")
