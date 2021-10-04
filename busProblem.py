def week():
    internalWeek = input('Please enter the week (ONLY WORKS WITH WEEK 1):')
    while internalWeek != '1' and internalWeek != '2' and internalWeek != '3' and internalWeek != '4':
        print('Invalid week! Please try again:')
        internalWeek = input('Please enter the week (ONLY WORKS WITH WEEK 1):')
    print('Valid value entered.')
    return internalWeek


def day():
    internalDay = input('Please enter the day (e.g. mon, thu):')
    while internalDay != 'mon' and internalDay != 'tue' and internalDay != 'wed' and internalDay != 'thu' and internalDay != 'fri':
        print('Invalid day! Please try again:')
        internalDay = input('Please enter the day (e.g. mon, thu):')
    print('Valid value entered.')
    return internalDay


def bus():
    internalBus = input('Please enter the bus letter:')
    while internalBus != 'a' and internalBus != 'b' and internalBus != 'c' and internalBus != 'd' and internalBus != 'e' and internalBus != 'f':
        print('Invalid bus letter! Please try again.')
        internalBus = input('Please enter the bus letter:')
    print('Valid value entered.')
    return internalBus


storedWeek = week()
storedBusLetter = bus()
busData = {
    'week': 'Week: ' + str(storedWeek),
    'letter': 'Bus Letter: ' + str(storedBusLetter.title()),
}


def userConfirm():
    global busData
    global storedBusLetter
    global storedWeek
    print('Please confirm that this is your entered data:')
    for dataCounter in busData.values():
        print(f'{dataCounter}')
    confirmation = input('y / n')
    if confirmation != 'y' and confirmation != 'n':
        userConfirm()
    elif confirmation == 'n':
        print("Please resubmit form.")
        storedWeek = week()
        storedBusLetter = bus()
        busData = {
            'week': 'Week: ' + str(storedWeek),
            'letter': 'Bus Letter: ' + str(storedBusLetter.title()),
        }
    else:
        print('Values registered.')


userConfirm()

# implement 2D array here
weekOneA = []
weekOneB = []
weekOneC = []
weekOneD = []
weekOneE = []
weekOneF = []
userState = 'n'

while userState == 'n':
    def weekChecker():
        if storedBusLetter == 'a':
            return weekOneA
        elif storedBusLetter == 'b':
            return weekOneB
        elif storedBusLetter == 'c':
            return weekOneC
        elif storedBusLetter == 'd':
            return weekOneD
        elif storedBusLetter == 'e':
            return weekOneE
        elif storedBusLetter == 'f':
            return weekOneF
        else:
            print("The program has run into an error at the 'weekChecker' function on line 61. Please try again.")


    def printList(busLetter, week):
        for i in range(0, len(weekChecker())):
            if i == 0:
                print(f"Monday: {weekChecker()[i]}")
            elif i == 1:
                print(f"Tuesday: {weekChecker()[i]}")
            elif i == 2:
                print(f"Wednesday: {weekChecker()[i]}")
            elif i == 3:
                print(f"Thursday: {weekChecker()[i]}")
            elif i == 4:
                print(f"Friday: {weekChecker()[i]}")


    def storedWeekFunction(storedWeekWeek, storedBusLetterBusLetter):
        return f'{storedWeekWeek}, {storedBusLetterBusLetter}'


    for weekCounter in range(0, 5):
        storedValue = 0
        while True:
            try:
                storedValue = int(input(
                    f'Please enter how many minutes early (+) / late (-) Bus {storedBusLetter.title()} was on Day '
                    f'{weekCounter + 1}:'))
            except ValueError:
                print("Please input a number.")
                continue
            else:
                break

        if storedBusLetter == 'a':
            weekChecker().append(storedValue)
            printList(storedBusLetter, storedWeek)
        elif storedBusLetter == 'b':
            weekChecker().append(storedValue)
        elif storedBusLetter == 'c':
            weekChecker().append(storedValue)
        elif storedBusLetter == 'd':
            weekChecker().append(storedValue)
        elif storedBusLetter == 'e':
            weekChecker().append(storedValue)
        elif storedBusLetter == 'f':
            weekChecker().append(storedValue)
        else:
            print("The program has run ino an error in the 'weekCounter' function. Please try again.")


    def editQueryFunction():
        editQuery = input(f"Would you like to edit anything from Week {storedWeek}? (yes / no)")
        while editQuery != 'yes' and editQuery != 'no':
            print('Invalid input! Please try again:')
            editQuery = input(f"Would you like to edit anything from Week {storedWeek}? (yes / no)")
        print('Valid value entered.')
        return editQuery


    queryEdit = editQueryFunction()


    def queryFunction():
        newNumberInput = int(0)
        if queryEdit == 'yes':
            dayChange = day()
            while True:
                try:
                    newNumberInput = int(input('Input new number:'))
                except ValueError:
                    print("Please input a number.")
                    continue
                else:
                    break
            if dayChange == 'mon':
                weekChecker()[0] = newNumberInput
            elif dayChange == 'tue':
                weekChecker()[1] = newNumberInput
            elif dayChange == 'wed':
                weekChecker()[2] = newNumberInput
            elif dayChange == 'thu':
                weekChecker()[3] = newNumberInput
            elif dayChange == 'fri':
                weekChecker()[4] = newNumberInput
            else:
                print("The program has run into an error. Please try again.")

            continueQuery = input('Continue? (y / n)')
            if continueQuery != 'y' and continueQuery != 'n':
                print('Please try again.')
                queryFunction()
            elif continueQuery == 'y':
                queryFunction()
            elif continueQuery == 'n':
                print("Thank you for using this service.")
                printList(storedBusLetter, storedWeek)
            else:
                print('The program has run into an error. Please restart.')
        elif queryEdit == 'no':
            print("Thank you for using this service.")
            printList(storedBusLetter, storedWeek)


    currentLatestBusNumber = 0
    currentLatestBusLetter = 'null'

    queryFunction()
    forWeekNumber = 0
    late = 0
    lateNumbers = []
    early = 0
    onTime = 0


    def latestBusFunction():
        global currentLatestBusNumber
        global currentLatestBusLetter
        for latestBusFunctionCounter in range(0, len(lateNumbers)):
            if lateNumbers[latestBusFunctionCounter] < currentLatestBusNumber:
                currentLatestBusNumber = lateNumbers[latestBusFunctionCounter]
                currentLatestBusLetter = storedBusLetter


    for forWeekCounter in range(0, 5):
        if weekChecker()[forWeekCounter] < 0:
            late += 1
            lateNumbers.append(weekChecker()[forWeekCounter])
        elif weekChecker()[forWeekCounter] > 0:
            early += 1
        elif weekChecker()[forWeekCounter] == 0:
            onTime += 1
        else:
            print("Error on For Loop")
        forWeekNumber += 1


    def timeEnglishCheckerEarly():
        if early == 1:
            return 'time'
        else:
            return 'times'


    def timeEnglishCheckerLate():
        if late == 1:
            return 'time'
        else:
            return 'times'


    def timeEnglishCheckerOnTime():
        if onTime == 1:
            return 'time'
        else:
            return 'times'


    def averageLateChecker():
        lateTotal = 0
        for averageLateCheckerCounter in range(0, len(lateNumbers)):
            lateTotal += lateNumbers[averageLateCheckerCounter]
        lateAverage = lateTotal / len(lateNumbers)
        return round(lateAverage)


    input(
        f"Bus {storedBusLetter.title()} was early {early} {timeEnglishCheckerEarly()} on week {storedWeek}. (press "
        f"RETURN to continue)")
    input(
        f"Bus {storedBusLetter.title()} was late {late} {timeEnglishCheckerLate()} on week {storedWeek}. (press "
        f"RETURN to continue)")
    input(
        f"Bus {storedBusLetter.title()} was on time {onTime} {timeEnglishCheckerOnTime()} on week {storedWeek}. ("
        f"press RETURN to continue)")
    input(
        f"Bus {storedBusLetter.title()} had an average late time of {averageLateChecker()} minutes on week {storedWeek}"
        f".")


    def queryOfTheUser():
        userQueryAgainOfTheUser = input("Would you like to enter data for a different week? (y / n)")
        if userQueryAgainOfTheUser != 'y' and userQueryAgainOfTheUser != 'n':
            print("Invalid input. Please try again.")
        elif userQueryAgainOfTheUser == 'y':
            global storedWeek
            global storedBusLetter
            storedWeek = week()
            storedBusLetter = bus()
        elif userQueryAgainOfTheUser == 'n':
            global userState
            userState = 'y'
        else:
            print("Well... this error is impossible to achieve. I guess, congrats?")


    latestBusFunction()
    queryOfTheUser()

print(f"The latest bus was Bus {currentLatestBusLetter} on week {currentLatestBusNumber}.")
print("Exiting...")
