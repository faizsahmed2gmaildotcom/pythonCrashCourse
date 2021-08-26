class IceCreamStand:
    def __init__(self, restaurantName, cuisineType):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
    def describeRestaurant(self):
        print(f"{self.restaurantName.title()} is this ice cream shop's name.")
    def describeCuisine(self):
        print(f"{self.cuisineType.title()} are this ice cream shop's cuisines.")
    def iceCreamFlavors(self):
        self.flavors = ['poo', 'pee', 'farts', 'vanilla', 'rotten flesh']
        print(f"{self.flavors} are available.")


thisRestaurant = IceCreamStand('farty poo', 'toilets')
thisRestaurant.describeRestaurant()
thisRestaurant.describeCuisine()
thisRestaurant.iceCreamFlavors()
