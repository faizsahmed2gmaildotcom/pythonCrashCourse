sandwichOrders = ['original', 'Sand-witch', 'pastrami', 'beef', 'poo', 'pastrami', 'variety', 'pastrami']
finishedSandwiches = []
i = 0
for sandwichOrdersNum in sandwichOrders:
    if sandwichOrdersNum == 'pastrami':
        sandwichOrders.remove('pastrami')
        print("There's no more pastrami.")
    else:
        print('I finished your ' + sandwichOrders[i] + ' sandwich.')
        finishedSandwiches.append(sandwichOrders[i])
    i += 1
