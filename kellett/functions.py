def introduction():
    print('This is an introduction.')
    print('Proceeding...')
    print('\r')


def multiplication(numberOne, numberTwo):
    return numberOne * numberTwo


def parameterAddition(parameterOne, parameterTwo):
    for a in range(len(parameterOne)):
        print(parameterOne[a] + parameterTwo[a])
    print('\r')


def wholeNumberAdder(wholeNumber):
    total = 0
    for b in range(1, wholeNumber):
        total += b
    return total


introduction()
print(multiplication(25, 54))
print('\r')
parameterAddition([5, 12, 54, 21], [47, 88, 103, 99])
print(wholeNumberAdder(500))
