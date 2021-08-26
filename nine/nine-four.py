class Restaurant:
    def __init__(self, restaurantName, cuisineType, numberServed, incrementNumberServed):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        self.numberServed = numberServed
        self.incrementNumberServed = incrementNumberServed

    def describeRestaurant(self):
        print(f"{self.restaurantName.title()} is this restaurant's name.")
    def describeCuisine(self):
        print(f"{self.cuisineType.title()} are this restaurant's cuisine.")
    def setNumberServed(self):
        print(f"{self.numberServed} people are to be served.")
    def callIncrementNumberServed(self):
        print(f"{self.incrementNumberServed + self.numberServed} people were served today.")


thisRestaurant = Restaurant('farty poo', 'toilets', 5, 69415)
thisRestaurant.describeRestaurant()
thisRestaurant.describeCuisine()
thisRestaurant.setNumberServed()
thisRestaurant.callIncrementNumberServed()
