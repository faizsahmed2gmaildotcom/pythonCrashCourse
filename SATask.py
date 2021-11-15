# submit by Monday, 6th December
import math

maxCoachCapacity = 80
remainingSeats = [480, 480, 480, 480, 480, 480, 480, 640]
moneyTaken = [0, 0, 0, 0, 0, 0, 0, 0]
maxCapacity = sum(remainingSeats)
userGroupAmount = 0
discountedPeople = 0
currentPeopleCounter = 0
userPurchaseInput = str('')


def currentCapacity():
    capacity = sum(remainingSeats)
    return capacity


def totalMoneyEarned():
    maxMoney = maxCapacity * 50
    return maxMoney


def getMoneyTaken(schedule):
    return moneyTaken[schedule - 9]


def digitChecker(variable):
    if variable < 10:
        return '    '
    elif variable < 100:
        return '   '
    elif variable < 1000:
        return '  '
    elif variable < 10000:
        return ' '


def printTable(printMoney):
    print(f"")
    print(f"| Leave  | 09:00  | 11:00 | 13:00 | 15:00 |")
    print(
        f"| Seats  | {remainingSeats[0]}{digitChecker(remainingSeats[0])}| {remainingSeats[2]}{digitChecker(remainingSeats[2])}| {remainingSeats[4]}{digitChecker(remainingSeats[4])}| {remainingSeats[6]}{digitChecker(remainingSeats[6])}|")
    if printMoney == 'true':
        print(
            f"| Money  | ${moneyTaken[0]}     | ${moneyTaken[2]}    | ${moneyTaken[4]}    | ${moneyTaken[6]}    |")
    print('-------------------------------------------')
    print(f"| Return | 10:00  | 12:00 | 14:00 | 16:00 |")
    print(
        f"| Seats  | {remainingSeats[1]}    | {remainingSeats[3]}   | {remainingSeats[5]}   | {remainingSeats[7]}   |")
    if printMoney == 'true':
        print(
            f"| Money  | ${moneyTaken[1]}     | ${moneyTaken[3]}    | ${moneyTaken[5]}    | ${moneyTaken[7]}    |")
    print(f"")


printTable('true')


def valueError(returnValue, inputMessage, returnMessage):
    while True:
        try:
            returnValue = int(input(inputMessage))
        except ValueError:
            print(returnMessage)
            continue
        else:
            return returnValue


def getRemainingSeats(schedule):
    return remainingSeats[schedule - 9]


def subtractRemainingSeats(schedule, seats):
    remainingSeats[schedule - 9] -= seats
    printTable('true')


def updateMoneyTaken(schedule, groupAmount):
    global discountedPeople
    moneyTaken[schedule - 9] = groupAmount * 25
    discountedPeople = math.floor(groupAmount / 10)
    moneyTaken[schedule - 9] -= discountedPeople * 25


def purchaseTicketAmount():
    global userPurchaseInput
    global userGroupAmount
    global discountedPeople
    while userPurchaseInput != 'one' and userPurchaseInput != '1' and userPurchaseInput != 'more':
        userPurchaseInput = str(input("Would you like to purchase a ticket for 'one' or 'more'?"))
        if userPurchaseInput == 'more':
            while userGroupAmount < 1 or userGroupAmount > 80:
                userGroupAmount = valueError(userGroupAmount, 'Tickets for how many?',
                                             'Please input a number from 1-80.')
        elif userPurchaseInput == 'one':
            userGroupAmount = 1


def purchaseTicket():
    global userGroupAmount
    purchaseTicketAmount()
    printTable('true')

    userPurchaseLeaveTime = 0
    while userPurchaseLeaveTime != 9 or userPurchaseLeaveTime != 11 or userPurchaseLeaveTime != 13 or userPurchaseLeaveTime != 15:
        userPurchaseLeaveTime = int(input("What time would you like to leave? (9 / 11 / 13 / 15)"))
        if userPurchaseLeaveTime == 9 or userPurchaseLeaveTime == 11 or userPurchaseLeaveTime == 13 or userPurchaseLeaveTime == 15:
            break
    subtractRemainingSeats(userPurchaseLeaveTime, userGroupAmount)
    updateMoneyTaken(userPurchaseLeaveTime, userGroupAmount)

    userPurchaseReturnTime = 0
    while userPurchaseReturnTime != 10 or userPurchaseReturnTime != 12 or userPurchaseReturnTime != 14 or userPurchaseReturnTime != 16:
        userPurchaseReturnTime = int(input("What time would you like to return? (10 / 12 / 14 / 16)"))
        if userPurchaseReturnTime == 10 or userPurchaseReturnTime == 12 or userPurchaseReturnTime == 14 or userPurchaseReturnTime == 16:
            break
    subtractRemainingSeats(userPurchaseReturnTime, userGroupAmount)
    updateMoneyTaken(userPurchaseReturnTime, userGroupAmount)


purchaseTicket()
userPurchaseTicketConfirm = ''
while userPurchaseTicketConfirm.lower() != 'yes' or userPurchaseTicketConfirm.lower() != 'no':
    userPurchaseTicketConfirm = input("Would you like to purchase more tickets? (yes / no)")
    if userPurchaseTicketConfirm.lower() == 'yes' or userPurchaseTicketConfirm.lower() != 'no':
        break
if userPurchaseTicketConfirm.lower() == 'yes' and currentPeopleCounter < 80:
    purchaseTicket()
elif userPurchaseTicketConfirm.lower() == 'no':
    printTable('true')
