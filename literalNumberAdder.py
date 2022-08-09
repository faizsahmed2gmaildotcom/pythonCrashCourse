def literalNumberAdder(literalNumber):
    literalTotal = 0
    literalInteger = literalNumber
    while True:
        if literalInteger < 1:
            return literalTotal
        else:
            literalTotal += int(literalInteger) % 10
            literalInteger = literalInteger / 10


while True:
    while True:
        try:
            inputNumber = int(input('Input a whole number! '))
        except ValueError:
            print('This is not a (whole) number...')
            continue
        break

    print(f"Literal Total: {literalNumberAdder(inputNumber)}")
