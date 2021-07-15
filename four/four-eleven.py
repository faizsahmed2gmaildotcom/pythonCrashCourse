pizza = ['volcano', 'veggie', 'chicken']
friendPizza = ['volcano', 'veggie', 'chicken']
pizzaLoc = 0
for pizzaLen in range(len(pizza)):
    input("I don't like " + pizza[pizzaLoc] + " pizza.")
    pizzaLoc += 1
input("I like pizza.")
pizza.append(input("Please input a pizza."))
friendPizza.append(input("Please input a friend's pizza."))
input("My favorite pizzas are: " + str(pizza))
print("My friend's favorite pizzas are: ")
for i in range(len(friendPizza)):
    print(friendPizza[i])
