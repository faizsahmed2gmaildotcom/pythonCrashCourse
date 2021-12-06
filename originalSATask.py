# submit by Monday, 6th December
import math

# variables
maxCapacity = [480, 480, 480, 480, 480, 480, 480, 640]
remainingSeats = [480, 480, 480, 480, 480, 480, 480, 640]
moneyTaken = [0, 0, 0, 0, 0, 0, 0, 0]
saveData = []
userGroupAmount = 999
discountedPeople = 0
currentPeopleCounter = 0
mostPassengers = 0
currentTime = 0
currentNumber = 0
totalUserMoney = 0
userPurchaseLeaveTime = 0
userPurchaseReturnTime = 0
pwdCount = 0
devMode = ''
userPurchaseTicketConfirm = ''
mostPassengersTrain = ''


# returns the remaining seats while checking its capacity
def remainingSeatsChecker(pos):
    if remainingSeats[pos] == 0:
        return 'Closed'
    else:
        return remainingSeats[pos]


# returns the raw value of the remaining seats by inputting the time number (9, 12, 13, etc.)
def takenSeats(variable):
    return maxCapacity[variable] - remainingSeats[variable]


# task 3 function - updates the train(s) with the most passengers
def updateTrain():
    global currentNumber
    global mostPassengers
    global mostPassengersTrain

    currentTimes = []
    for i in range(8):
        if (mostPassengers == (remainingSeats[i] - maxCapacity[i]) * -1) and (remainingSeats[i] != maxCapacity[i]):
            currentNumber = takenSeats(i)
            currentTimes.append(str(i + 9))
            mostPassengersTrain = ':00 & '.join(currentTimes)
        elif (takenSeats(i)) > currentNumber:
            currentNumber = takenSeats(i)
            mostPassengers = takenSeats(i)
            mostPassengersTrain = i + 9


# used to format the "printTable" function
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


# used to format the "printTable" function
def moneyDigitChecker(variable):
    if variable < 10:
        return '    '
    elif variable < 100:
        return '   '
    elif variable < 1000:
        return '  '
    elif variable < 10000:
        return ' '


# task 1 function - prints the data table
def printTable():
    updateTrain()

    print(f"")
    print('-------------------------------------------')
    # leave times
    print(f"| Leave  | 09:00  | 11:00 | 13:00 | 15:00 |")
    print(
        f"| Seats  | {remainingSeatsChecker(0)}{seatsDigitChecker(remainingSeats[0])} | {remainingSeatsChecker(2)}{seatsDigitChecker(remainingSeats[2])}| {remainingSeatsChecker(4)}{seatsDigitChecker(remainingSeats[4])}| {remainingSeatsChecker(6)}{seatsDigitChecker(remainingSeats[6])}|")
    if devMode == 'true':
        print(
            f"| Money  | ${moneyTaken[0]}{moneyDigitChecker(moneyTaken[0])} | ${moneyTaken[2]}{moneyDigitChecker(moneyTaken[2])}| ${moneyTaken[4]}{moneyDigitChecker(moneyTaken[4])}| ${moneyTaken[6]}{moneyDigitChecker(moneyTaken[6])}|")
    print('-------------------------------------------')
    # return times
    print(f"| Return | 10:00  | 12:00 | 14:00 | 16:00 |")
    print(
        f"| Seats  | {remainingSeatsChecker(1)}{seatsDigitChecker(remainingSeats[1])} | {remainingSeatsChecker(3)}{seatsDigitChecker(remainingSeats[3])}| {remainingSeatsChecker(5)}{seatsDigitChecker(remainingSeats[5])}| {remainingSeatsChecker(7)}{seatsDigitChecker(remainingSeats[7])}|")
    if devMode == 'true':
        print(
            f"| Money  | ${moneyTaken[1]}{moneyDigitChecker(moneyTaken[1])} | ${moneyTaken[3]}{moneyDigitChecker(moneyTaken[3])}| ${moneyTaken[5]}{moneyDigitChecker(moneyTaken[5])}| ${moneyTaken[7]}{moneyDigitChecker(moneyTaken[7])}|")
    print('-------------------------------------------')
    if devMode == 'true':
        # task 3 data
        print(f"             | Total")
        print(f"| Money      | ${sum(moneyTaken)}{moneyDigitChecker(sum(moneyTaken))} ")
        print(
            f"| Passengers | {(sum(remainingSeats) * -1) + 4000}{seatsDigitChecker((sum(remainingSeats) * -1) + 4000)}")
        print('-------------------------------------------')
        print(f"| Most Passengers")
        print(f"| Train: {mostPassengersTrain}:00")
        print(f"| Passengers: {mostPassengers}")
        print('-------------------------------------------')
    # user-specific data
    print(f"Your Total | ${totalUserMoney}{moneyDigitChecker(totalUserMoney)}|")
    print(f"Selected Buses | {':00 & '.join(set(saveData))}:00 |")
    print('-------------------------------------------')
    print(f"")


# task 2 starts here
# does not continue program unless the input value is an integer
def valueError(returnValue, inputMessage, returnMessage):
    while True:
        try:
            returnValue = int(input(inputMessage))
        except ValueError:
            print(returnMessage)
            continue
        else:
            return returnValue


# subtracts the number of seats remaining in a bus
def subtractRemainingSeats(schedule, seats):
    global remainingSeats
    remainingSeats[schedule - 9] -= seats


# subtracts the money earned from a bus
def updateMoneyTaken(schedule, groupAmount):
    global discountedPeople
    global totalUserMoney
    moneyTaken[schedule - 9] = groupAmount * 25
    discountedPeople = math.floor(groupAmount / 10)
    moneyTaken[schedule - 9] -= discountedPeople * 25
    totalUserMoney += moneyTaken[schedule - 9]


# used to obtain the desired number of tickets to purchase from the user
def purchaseTicketAmount():
    global userGroupAmount
    printTable()
    userGroupAmount = 99
    # exits program if there are no more seats available anywhere
    if sum(remainingSeats) - sum(maxCapacity) == 0:
        print("There are no more tickets available today!")
        printTable()
        exit()
    while userGroupAmount < 1 or userGroupAmount > 80:
        userGroupAmount = valueError(userGroupAmount, 'Tickets for how many?', 'Please input a number from 1-80.')
        if userGroupAmount < 1 or userGroupAmount > 80:
            print('Please input a number from 1-80.')


# checks if the capacity of a train is greater than zero
def capacityChecker(time, groupAmount):
    if remainingSeats[time - 9] - groupAmount < 0:
        return 'false'
    elif remainingSeats[time - 9] - groupAmount >= 0:
        return 'true'


# main function
def purchaseTicket():
    global userPurchaseTicketConfirm
    global currentTime
    global userPurchaseLeaveTime
    global userPurchaseReturnTime
    purchaseTicketAmount()
    # user's leave time
    userPurchaseLeaveTime = 0
    while True:
        userPurchaseLeaveTime = valueError(userPurchaseLeaveTime,
                                           "What time would you like to leave? (9 / 11 / 13 / 15)",
                                           "Please enter: 9 / 11 / 13 / 15 ")
        if (
                ((userPurchaseLeaveTime == 9) or (userPurchaseLeaveTime == 11) or
                 (userPurchaseLeaveTime == 13) or (userPurchaseLeaveTime == 15))) and (
                capacityChecker(userPurchaseLeaveTime, userGroupAmount) == 'true'):
            break
        if capacityChecker(userPurchaseLeaveTime, userGroupAmount) == 'false':
            print(f"There is not enough space left in the {userPurchaseLeaveTime - 9}:00 train!")
            purchaseTicket()

    # user's return time
    userPurchaseReturnTime = 0
    while True:
        userPurchaseReturnTime = valueError(userPurchaseReturnTime,
                                            "What time would you like to return? (10 / 12 / 14 / 16)",
                                            "Please enter: 10 / 12 / 14 / 16: ")
        if ((userPurchaseReturnTime == 10) or (userPurchaseReturnTime == 12) or (userPurchaseReturnTime == 14) or (
                userPurchaseReturnTime == 16)) and (
                capacityChecker(userPurchaseReturnTime, userGroupAmount) == 'true') and (
                userPurchaseLeaveTime < userPurchaseReturnTime):
            break
        if capacityChecker(userPurchaseReturnTime, userGroupAmount) == 'false':
            print(f"There is not enough space left in the {userPurchaseReturnTime - 9}:00 train!")
            purchaseTicket()
        if userPurchaseLeaveTime > userPurchaseReturnTime:
            print("You cannot stay overnight!")
    # updates the variables in the data table here
    currentTime = userPurchaseReturnTime
    subtractRemainingSeats(userPurchaseReturnTime, userGroupAmount)
    updateMoneyTaken(userPurchaseReturnTime, userGroupAmount)
    saveData.append(str(userPurchaseReturnTime))
    subtractRemainingSeats(userPurchaseLeaveTime, userGroupAmount)
    updateMoneyTaken(userPurchaseLeaveTime, userGroupAmount)
    saveData.append(str(userPurchaseLeaveTime))
    printTable()

    # asks user if they would like to purchase more tickets
    while True:
        userPurchaseTicketConfirm = input("Would you like to purchase more tickets? ('yes' / 'no')")
        if userPurchaseTicketConfirm.lower() == 'yes' or userPurchaseTicketConfirm.lower() == 'no':
            break


# loop to enable developer mode to see all data
while True:
    print("Enable Developer Mode to run as an Administrator. Disable Developer Mode to run the program as a user.")
    devMode = str(input("Enable Developer Mode? ('true' / 'false')"))
    if (devMode == 'true') or (devMode == 'false'):
        break

if devMode == 'true':
    # if developer mode is to be enabled, the password "iHateSA" must be entered
    while True:
        inputPwd = input("Password: ")
        if pwdCount > 3:
            print(
                "You have failed too many times! (The Password is in the private comments on the submission in Google Classroom!)")
            exit()
        if inputPwd != 'iHateSA':
            print('Incorrect Password! Please try again.')
            pwdCount += 1
        elif inputPwd == 'iHateSA':
            break

# main program
while True:
    purchaseTicket()
    if userPurchaseTicketConfirm.lower() == 'no':
        totalUserMoney = 0
        userPurchaseLeaveTime = 0
        userPurchaseReturnTime = 0
        saveData = []

        # the user can exit the program if they are a developer
        if devMode == 'true':
            while True:
                userExit = input("Exit program? ('yes' / 'no')")
                if userExit == 'yes':
                    exit(print("Exiting program..."))
                    printTable()
                elif userExit == 'no':
                    break
        print("Please allow the next user to purchase tickets.\n")
