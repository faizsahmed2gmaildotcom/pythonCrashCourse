class User:
    def __init__(self, firstName, lastName, loginAttempts):
        self.firstName = firstName
        self.lastName = lastName
        self.loginAttempts = loginAttempts
    def callFirstName(self):
        print(f"{self.firstName.title()} is this person's first name.")
    def callLastName(self):
        print(f"{self.lastName.title()} is this person's last name.")
    def callLoginAttempts(self):
        print(f"{self.loginAttempts} login attempts have been made.")
    def callIncrementLoginAttempts(self):
        self.loginAttempts += 1
        print(f"{self.loginAttempts} login attempts have now been made.")
    def resetLoginAttempts(self):
        self.loginAttempts = 0
        print(f"Reset login attempts to {self.loginAttempts}.")


callUser = User('poopy p.', 'toilets', 68)
callUser.callFirstName()
callUser.callLastName()
callUser.callLoginAttempts()
callUser.callIncrementLoginAttempts()
callUser.resetLoginAttempts()
