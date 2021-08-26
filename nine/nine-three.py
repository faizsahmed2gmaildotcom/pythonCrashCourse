class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def describeRestaurant(self):
        print(f"{self.firstName.title()} is this person's first name.")
    def describeCuisine(self):
        print(f"{self.lastName.title()} is this person's last name.")


thisRestaurant = User('poopy p.', 'toilets')
thisRestaurant.describeRestaurant()
thisRestaurant.describeCuisine()
