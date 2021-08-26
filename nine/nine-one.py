class Restaurant:
    def __init__(self, restaurantName, cuisineType):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
    def describeRestaurant(self):
        print(f"{self.restaurantName.title()} is this restaurant's name.")
    def describeCuisine(self):
        print(f"{self.cuisineType.title()} are this restaurant's cuisine.")


thisRestaurant = Restaurant('farty poo', 'toilets')
thisRestaurant.describeRestaurant()
thisRestaurant.describeCuisine()
