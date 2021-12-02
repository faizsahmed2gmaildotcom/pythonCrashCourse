from SAtask import *


def seatsDigitChecker(variable):
    if variable == 0:
        return ''
    elif variable < 10:
        return '     '
    elif variable < 100:
        return '    '
    elif variable < 1000:
        return '   '
    elif variable < 10000:
        return '  '


def moneyDigitChecker(variable):
    if variable < 10:
        return '    '
    elif variable < 100:
        return '   '
    elif variable < 1000:
        return '  '
    elif variable < 10000:
        return ' '


def printOriginalTable():
    print(f"")
    print('-------------------------------------------')
    print(f"| Leave  | 09:00  | 11:00 | 13:00 | 15:00 |")
    print(
        f"| Seats  | {remainingSeatsChecker(0)}{seatsDigitChecker(remainingSeats[0])} | {remainingSeatsChecker(2)}{seatsDigitChecker(remainingSeats[2])}| {remainingSeatsChecker(4)}{seatsDigitChecker(remainingSeats[4])}| {remainingSeatsChecker(6)}{seatsDigitChecker(remainingSeats[6])}|")
    if devMode == 'true':
        print(
            f"| Money  | ${moneyTaken[0]}{moneyDigitChecker(moneyTaken[0])} | ${moneyTaken[2]}{moneyDigitChecker(moneyTaken[2])}| ${moneyTaken[4]}{moneyDigitChecker(moneyTaken[4])}| ${moneyTaken[6]}{moneyDigitChecker(moneyTaken[6])}|")
    print('-------------------------------------------')
    print(f"| Return | 10:00  | 12:00 | 14:00 | 16:00 |")
    print(
        f"| Seats  | {remainingSeatsChecker(1)}{seatsDigitChecker(remainingSeats[1])} | {remainingSeatsChecker(3)}{seatsDigitChecker(remainingSeats[3])}| {remainingSeatsChecker(5)}{seatsDigitChecker(remainingSeats[5])}| {remainingSeatsChecker(7)}{seatsDigitChecker(remainingSeats[7])}|")
    if devMode == 'true':
        print(
            f"| Money  | ${moneyTaken[1]}{moneyDigitChecker(moneyTaken[1])} | ${moneyTaken[3]}{moneyDigitChecker(moneyTaken[3])}| ${moneyTaken[5]}{moneyDigitChecker(moneyTaken[5])}| ${moneyTaken[7]}{moneyDigitChecker(moneyTaken[7])}|")
    print('-------------------------------------------')
    if devMode == 'true':
        print(f"             | Total")
        print(f"| Money      | ${sum(moneyTaken)}{moneyDigitChecker(sum(moneyTaken))} ")
        print(
            f"| Passengers | {(sum(remainingSeats) * -1) + 4000}{seatsDigitChecker((sum(remainingSeats) * -1) + 4000)}")
        print('-------------------------------------------')
        print(f"| Most Passengers")
        print(f"| Train: {mostPassengersTrain}:00")
        print(f"| Passengers: {mostPassengers}")
        print('-------------------------------------------')
    print(f"Your Total | ${totalUserMoney}{moneyDigitChecker(totalUserMoney)}|")
    print(f"Selected Buses | {':00 & '.join(set(saveData))}:00 |")
    print('-------------------------------------------')
    print(f"")
