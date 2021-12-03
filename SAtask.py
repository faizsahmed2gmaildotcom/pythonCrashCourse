# submit by Monday, 6th December
import math
from tkinter import *
from tkinter import ttk

# variables
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
pwdCount = 0
windowHeight = 0
tableHeight = 0


def remainingSeatsChecker(pos):
    if remainingSeats[pos] == 0:
        return 'Closed'
    else:
        return remainingSeats[pos]


def takenSeats(variable):
    return maxCapacity[variable] - remainingSeats[variable]


# task 3 function
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


# task 1 function
def printTable():
    updateTrain()

    timeTable = Tk()
    timeTable.title('Train Table')
    timeTable.geometry(f'1900x{str(windowHeight)}')

    sat = ttk.Treeview(timeTable, height=tableHeight)
    sat.pack()

    sat['columns'] = ('Leave', '09:00', '11:00', '13:00', '15:00', '', 'Return', '10:00', '12:00', '14:00', '16:00')
    sat.column("#0", width=10, stretch=NO)
    sat.column("Leave", anchor=CENTER, width=170)
    sat.column("09:00", anchor=CENTER, width=170)
    sat.column("11:00", anchor=CENTER, width=170)
    sat.column("13:00", anchor=CENTER, width=170)
    sat.column("15:00", anchor=CENTER, width=170)
    sat.column("", anchor=CENTER, width=170)
    sat.column("Return", anchor=CENTER, width=170)
    sat.column("10:00", anchor=CENTER, width=170)
    sat.column("12:00", anchor=CENTER, width=170)
    sat.column("14:00", anchor=CENTER, width=170)
    sat.column("16:00", anchor=CENTER, width=170)

    sat.heading("#0", text="", anchor=CENTER)
    sat.heading("Leave", text="Leave", anchor=CENTER)
    sat.heading("09:00", text="09:00", anchor=CENTER)
    sat.heading("11:00", text="11:00", anchor=CENTER)
    sat.heading("13:00", text="13:00", anchor=CENTER)
    sat.heading("15:00", text="15:00", anchor=CENTER)
    sat.heading("", text="", anchor=CENTER)
    sat.heading("Return", text="Return", anchor=CENTER)
    sat.heading("10:00", text="10:00", anchor=CENTER)
    sat.heading("12:00", text="12:00", anchor=CENTER)
    sat.heading("14:00", text="14:00", anchor=CENTER)
    sat.heading("16:00", text="16:00", anchor=CENTER)

    # leave & return
    sat.insert(parent='', index='end', iid='1', text='',
               values=(
                   'Seats Left', remainingSeatsChecker(0), remainingSeatsChecker(2), remainingSeatsChecker(4),
                   remainingSeatsChecker(6), '', 'Seats Left',
                   remainingSeatsChecker(1),
                   remainingSeatsChecker(3), remainingSeatsChecker(5), remainingSeatsChecker(7)))
    if devMode == 'true':
        sat.insert(parent='', index='end', iid='2', text='',
                   values=(
                       'Money', f'${moneyTaken[0]}', f'${moneyTaken[2]}', f'${moneyTaken[4]}', f'${moneyTaken[6]}', '',
                       'Money',
                       f'${moneyTaken[1]}', f'${moneyTaken[3]}', f'${moneyTaken[5]}', f'${moneyTaken[7]}'))
        sat.insert(parent='', index='end', iid='3', text='',
                   values=('----------------------------------------', '----------------------------------------',
                           '----------------------------------------'))
        sat.insert(parent='', index='end', iid='4', text='',
                   values=('Most-Passengers', f'Train', 'Passengers'))
        sat.insert(parent='', index='end', iid='5', text='',
                   values=('', f'{mostPassengersTrain}:00', mostPassengers))

        # totals (task 3)
        sat.insert(parent='', index='end', iid='7', text='',
                   values=('----------------------------------------', '----------------------------------------',
                           '----------------------------------------'))
        sat.insert(parent='', index='end', iid='8', text='',
                   values=('Totals', 'Money', 'Passengers'))
        sat.insert(parent='', index='end', iid='9', text='',
                   values=('', f'${sum(moneyTaken)}', (sum(remainingSeats) * -1) + 4000))

    # user data (task 3)
    sat.insert(parent='', index='end', iid='10', text='',
               values=('----------------------------------------', '----------------------------------------',
                       '----------------------------------------'))
    sat.insert(parent='', index='end', iid='11', text='Your Totals',
               values=('Your-Data',))
    sat.insert(parent='', index='end', iid='12', text='',
               values=('Money', f'${totalUserMoney}'))
    sat.insert(parent='', index='end', iid='13', text='',
               values=('Buses', f"{':00 & '.join(set(saveData))}:00"))

    # button
    leaveBtn = Button(timeTable, text="Continue", command=timeTable.destroy)
    leaveBtn.pack()

    # run window
    timeTable.mainloop()


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
    printTable()
    userGroupAmount = 99
    if sum(remainingSeats) - 160 == 0:
        print("There are no more tickets available today!")
        printTable()
        exit()
    while userGroupAmount < 1 or userGroupAmount > 80:
        userGroupAmount = valueError(userGroupAmount, 'Tickets for how many?', 'Please input a number from 1-80.')
        if userGroupAmount < 1 or userGroupAmount > 80:
            print('Please input a number from 1-80.')


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
    # leave
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

    # return
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
    currentTime = userPurchaseReturnTime
    subtractRemainingSeats(userPurchaseReturnTime, userGroupAmount)
    updateMoneyTaken(userPurchaseReturnTime, userGroupAmount)
    saveData.append(str(userPurchaseReturnTime))
    subtractRemainingSeats(userPurchaseLeaveTime, userGroupAmount)
    updateMoneyTaken(userPurchaseLeaveTime, userGroupAmount)
    saveData.append(str(userPurchaseLeaveTime))
    printTable()

    while True:
        userPurchaseTicketConfirm = input("Would you like to purchase more tickets? ('yes' / 'no')")
        if userPurchaseTicketConfirm.lower() == 'yes' or userPurchaseTicketConfirm.lower() == 'no':
            break


# developer mode
while True:
    print("Enable Developer Mode to run as an Administrator. Disable Developer Mode to run the program as a user.")
    print("IMPORTANT: DATA TABLE WILL OPEN IN A NEW WINDOW\n")
    devMode = str(input("Enable Developer Mode? ('true' / 'false')"))
    if (devMode == 'true') or (devMode == 'false'):
        break

if devMode == 'true':
    windowHeight = 320
    tableHeight = 13
    while True:
        inputPwd = input("Password: ")
        if pwdCount > 3:
            print(
                "You have failed too many times! (The Password is in the private comments on the submission in Google Classroom!")
            exit()
        if inputPwd != 'iHateSA':
            print('Incorrect Password! Please try again.')
            pwdCount += 1
        elif inputPwd == 'iHateSA':
            break
elif devMode == 'false':
    windowHeight = 190
    tableHeight = 6

# main program
while True:
    purchaseTicket()
    if userPurchaseTicketConfirm.lower() == 'no':
        totalUserMoney = 0
        userPurchaseLeaveTime = 0
        userPurchaseReturnTime = 0
        saveData = []

        if devMode == 'true':
            while True:
                userExit = input("Exit program? ('yes' / 'no')")
                if userExit == 'yes':
                    exit(print("Exiting program..."))
                    printTable()
                elif userExit == 'no':
                    break
        print("Please allow the next user to purchase tickets.\n")
    if sum(remainingSeats) == 0:
        print("There are no more seats remaining.")
        printTable()
        break
