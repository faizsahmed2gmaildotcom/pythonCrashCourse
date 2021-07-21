input("'Buffay' foods (not legit):")
buffetFoods = ('Cake', 'Pizza', 'Butter chicken', 'Naan', 'Puu')
for i in range(0, 5, 1):
    input(buffetFoods[i])

input("Buffet foods (legit):")
buffetFoods = ('Cake', 'Pee', 'Poo', 'Naan', 'Puu')
for r in range(0, 5, 1):
    input(buffetFoods[r])

input("Attempting direct modification...")
buffetFoods[0] = 'ree'
