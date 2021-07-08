pet = ['cat', 'domestic cat', 'wild cat']
petLoc = 0
for petLen in range(len(pet)):
    if petLoc < 2:
        input(pet[petLoc] + "s are very cute!")
    elif petLoc >= 2:
        input(pet[petLoc] + "s are very scary.\n")
    petLoc += 1
input("But any of these animals would be very cute!")
