def makeShirt(size, text):
    print(f"Got it, we'll make a size {int(size)} shirt for you that says: '{text}'")

shirtSize = input('What size shirt would you like?')
shirtText = input('What would you like your shirt to say?')
makeShirt(shirtSize, shirtText)
