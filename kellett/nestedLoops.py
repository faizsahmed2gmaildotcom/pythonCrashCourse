names = ['Harry', 'Hermione', 'Ron', 'Hagrid', 'Dumbledore']
letterCount = 0
for a in names:
    for b in a:
        letterCount += 1
print(f"Letters: {letterCount}")
print('\r')

numbersArray = [102, 402, 521, 595, 123, 852, 763, 999, 101, 765, 981, 111]
for c in numbersArray:
    digitTotal = 0
    c = str(c)
    for d in c:
        digitTotal += int(d)
    print(digitTotal)
