# 1
while True:
    try:
        height = int(input('How tall are you in meters? '))
    except ValueError:
        print('Please enter a number!')
        continue
    else:
        break

if height > 1.2:
    print('You can ride the rollercoaster! \n')
else:
    print('You are not tall enough to ride the rollercoaster! \n')


# 2
while True:
    difficulty = input("Input difficulty: 'easy' / 'medium' / 'hard' ")
    if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':
        break
print(f"You have selected: {difficulty}.")


# 3
name = input("What is your name? ")
name.capitalize()
print(f"Hello, {name}!")
age = input("How old are you? ")
print(f"I see. You are {age} years old!")
