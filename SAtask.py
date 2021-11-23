# submit by Monday, 6th December
import math

# variables
maxCoachCapacity = 80
maxCapacity = [480, 480, 480, 480, 480, 480, 480, 640]
remainingSeats = [480, 480, 480, 480, 480, 480, 480, 640]
moneyTaken = [0, 0, 0, 0, 0, 0, 0, 0]
saveData = []
userGroupAmount = 999
discountedPeople = 0
currentPeopleCounter = 0
devMode = ''
userPurchaseTicketConfirm = ''
mostPassengersTrain = ''
mostPassengers = 0
currentTime = 0
currentNumber = 0
totalUserMoney = 0
userPurchaseLeaveTime = 0
userPurchaseReturnTime = 0


def takenSeats(pos):
    if remainingSeats[pos] == 0:
        return 'Closed'
    else:
        return remainingSeats[pos]


def fetchTakenSeats(variable):
    return maxCapacity[variable] - remainingSeats[variable]


def naeem():
    mostRemaining = fetchTakenSeats(0)
    a = []
    for i in range(8):
        if mostRemaining == fetchTakenSeats(i):
            a.append(i)
        elif mostRemaining < fetchTakenSeats(i):
            mostRemaining = fetchTakenSeats(i)
            a = [i]
    return a


def updateTrain():
    global currentNumber
    global mostPassengers
    global mostPassengersTrain
    global remainingSeats
    global saveData
    currentTimes = []
    for i in range(8):
        if (mostPassengers == (remainingSeats[i] - maxCapacity[i]) * -1) and (remainingSeats[i] != maxCapacity[i]):
            currentNumber = fetchTakenSeats(i)
            currentTimes.append(str(i + 9))
            mostPassengersTrain = ':00 & '.join(currentTimes)
        elif (fetchTakenSeats(i)) > currentNumber:
            currentNumber = fetchTakenSeats(i)
            mostPassengers = fetchTakenSeats(i)
            mostPassengersTrain = f"{i + 9}:00"


while True:
    devMode = str(input("Enable Developer Mode? ('true' / 'false')"))
    if devMode == 'true' or devMode == 'false':
        break


# task 3 function


def currentCapacity():
    capacity = sum(remainingSeats)
    return capacity


def totalMoneyEarned():
    maxMoney = currentCapacity() * 50
    return maxMoney


def getMoneyTaken(schedule):
    return moneyTaken[schedule - 9]


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


# task 1 function
def printTable(printMoney):
    updateTrain()
    print(f"")
    print('-------------------------------------------')
    print(f"| Leave  | 09:00  | 11:00 | 13:00 | 15:00 |")
    print(
        f"| Seats  | {takenSeats(0)}{seatsDigitChecker(remainingSeats[0])} | {takenSeats(2)}{seatsDigitChecker(remainingSeats[2])}| {takenSeats(4)}{seatsDigitChecker(remainingSeats[4])}| {takenSeats(6)}{seatsDigitChecker(remainingSeats[6])}|")
    if printMoney == 'true':
        print(
            f"| Money  | ${moneyTaken[0]}{moneyDigitChecker(moneyTaken[0])} | ${moneyTaken[2]}{moneyDigitChecker(moneyTaken[2])}| ${moneyTaken[4]}{moneyDigitChecker(moneyTaken[4])}| ${moneyTaken[6]}{moneyDigitChecker(moneyTaken[6])}|")
    print('-------------------------------------------')
    print(f"| Return | 10:00  | 12:00 | 14:00 | 16:00 |")
    print(
        f"| Seats  | {takenSeats(1)}{seatsDigitChecker(remainingSeats[1])} | {takenSeats(3)}{seatsDigitChecker(remainingSeats[3])}| {takenSeats(5)}{seatsDigitChecker(remainingSeats[5])}| {takenSeats(7)}{seatsDigitChecker(remainingSeats[7])}|")
    if printMoney == 'true':
        print(
            f"| Money  | ${moneyTaken[1]}{moneyDigitChecker(moneyTaken[1])} | ${moneyTaken[3]}{moneyDigitChecker(moneyTaken[3])}| ${moneyTaken[5]}{moneyDigitChecker(moneyTaken[5])}| ${moneyTaken[7]}{moneyDigitChecker(moneyTaken[7])}|")
    print('-------------------------------------------')
    if devMode == 'true':
        print(f"             | Total")
        print(f"| Money      | ${sum(moneyTaken)}{moneyDigitChecker(sum(moneyTaken))} ")
        print(
            f"| Passengers | {(currentCapacity() * -1) + 4000}{seatsDigitChecker((currentCapacity() * -1) + 4000)}")
        print('-------------------------------------------')
        print(f"| Most Passengers")
        print(f"| Train: {mostPassengersTrain}:00")
        print(f"| Passengers: {mostPassengers}")
        print('-------------------------------------------')
    print(f"Your Total | ${totalUserMoney}{moneyDigitChecker(totalUserMoney)}|")
    print(f"Your Buses | {':00 & '.join(set(saveData))}:00 |")
    print('-------------------------------------------')
    print(f"")


printTable(devMode)


# task 2 starts here
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
    global remainingSeats
    remainingSeats[schedule - 9] -= seats


def updateMoneyTaken(schedule, groupAmount):
    global discountedPeople
    global totalUserMoney
    moneyTaken[schedule - 9] = groupAmount * 25
    discountedPeople = math.floor(groupAmount / 10)
    moneyTaken[schedule - 9] -= discountedPeople * 25
    totalUserMoney += moneyTaken[schedule - 9]


def purchaseTicketAmount():
    global userGroupAmount
    userGroupAmount = 99
    if sum(remainingSeats) - 160 == 0:
        print("There are no more tickets available today!")
        printTable(devMode)
        exit()
    while userGroupAmount < 1 or userGroupAmount > 80:
        userGroupAmount = valueError(userGroupAmount, 'Tickets for how many?', 'Please input a number from 1-80.')
        if userGroupAmount < 1 or userGroupAmount > 80:
            print('Please input a number from 1-80.')


def capacityChecker(time, groupAmount):
    if getRemainingSeats(time) - groupAmount < 0:
        return 'false'
    elif getRemainingSeats(time) - groupAmount >= 0:
        return 'true'


# main function
def purchaseTicket():
    global userPurchaseTicketConfirm
    global currentTime
    global userPurchaseLeaveTime
    global userPurchaseReturnTime
    purchaseTicketAmount()
    printTable(devMode)
    userPurchaseLeaveTime = 0
    while userPurchaseLeaveTime != 9 or userPurchaseLeaveTime != 11 or userPurchaseLeaveTime != 13 or userPurchaseLeaveTime != 15:
        userPurchaseLeaveTime = valueError(userPurchaseLeaveTime,
                                           "What time would you like to leave? (9 / 11 / 13 / 15)",
                                           "Please enter a valid value.")
        if userPurchaseLeaveTime != 9 or userPurchaseLeaveTime != 11 or userPurchaseLeaveTime != 13 or userPurchaseLeaveTime != 15:
            print("Please enter a valid value.")
        if (
                userPurchaseLeaveTime == 9 or userPurchaseLeaveTime == 11 or userPurchaseLeaveTime == 13 or userPurchaseLeaveTime == 15) and (
                capacityChecker(userPurchaseLeaveTime, userGroupAmount) == 'true'):
            break
    currentTime = userPurchaseLeaveTime
    if capacityChecker(userPurchaseLeaveTime, userGroupAmount) == 'false':
        print(f"There is not enough space left in the {userPurchaseLeaveTime - 9}:00 train!")
        purchaseTicket()
    subtractRemainingSeats(userPurchaseLeaveTime, userGroupAmount)
    updateMoneyTaken(userPurchaseLeaveTime, userGroupAmount)
    saveData.append(str(userPurchaseLeaveTime))
    printTable(devMode)

    userPurchaseReturnTime = 0
    while userPurchaseReturnTime != 10 or userPurchaseReturnTime != 12 or userPurchaseReturnTime != 14 or userPurchaseReturnTime != 16:
        userPurchaseReturnTime = valueError(userPurchaseReturnTime,
                                            "What time would you like to return? (10 / 12 / 14 / 16)",
                                            "Please enter a valid value.")
        if userPurchaseReturnTime != 10 or userPurchaseReturnTime != 12 or userPurchaseReturnTime != 14 or userPurchaseReturnTime != 16:
            print("Please enter a valid value.")
        if userPurchaseReturnTime == 10 or userPurchaseReturnTime == 12 or userPurchaseReturnTime == 14 or userPurchaseReturnTime == 16 and (
                capacityChecker(userPurchaseReturnTime, userGroupAmount) == 'true'):
            break
    currentTime = userPurchaseReturnTime
    if capacityChecker(userPurchaseReturnTime, userGroupAmount) == 'false':
        print(f"There is not enough space left in the {userPurchaseReturnTime - 9}:00 train!")
        purchaseTicket()
    subtractRemainingSeats(userPurchaseReturnTime, userGroupAmount)
    updateMoneyTaken(userPurchaseReturnTime, userGroupAmount)
    saveData.append(str(userPurchaseReturnTime))
    printTable(devMode)
    while True:
        userPurchaseTicketConfirm = input("Would you like to purchase more tickets? ('yes' / 'no')")
        if userPurchaseTicketConfirm.lower() == 'yes' or userPurchaseTicketConfirm.lower() == 'no':
            break


while True:
    purchaseTicket()
    if userPurchaseTicketConfirm.lower() == 'no':
        totalUserMoney = 0
        userPurchaseReturnTime = 0
        userPurchaseLeaveTime = 0
        saveData = []
        print("Please allow the next user to purchase tickets.\n")
    if sum(remainingSeats) == 0:
        print("There are no more seats remaining anywhere!")
        printTable(devMode)
        break
