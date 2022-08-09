import random


counter = 0
while True:
    counter += 1
    print('forever...')
    print('and ever...')
    if counter == 100000:
        break


randomNumber = random.randint(0, 10)
while True:
    guessedNumber = int(input("Try guessing my number from 1 to 10! "))
    if guessedNumber == randomNumber:
        print(f"You got it! My number was {randomNumber}.")
        break
    elif guessedNumber < randomNumber:
        print("Oops, try higher next time!")
    elif guessedNumber > randomNumber:
        print("Oops, try lower next time!")


numCounter = 0
while True:
    print(numCounter)
    numCounter += 1
    if numCounter == 100000:
        break
