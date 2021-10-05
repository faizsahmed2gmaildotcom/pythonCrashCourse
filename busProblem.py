# basic program functions
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

# use 2D arrays below
# convert following 6 lines to a 2D array for Week 1
weekOneA = []
weekOneB = []
weekOneC = []
weekOneD = []
weekOneE = []
weekOneF = []
weekTwo = [[], [], [], [], []]
weekThree = [[], [], [], [], []]
weekFour = [[], [], [], [], []]
userState = 'n'

# main program
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
        weekCounterDay = 'null'
        if weekCounter == 0:
            weekCounterDay = 'Monday'
        elif weekCounter == 1:
            weekCounterDay = 'Tuesday'
        elif weekCounter == 2:
            weekCounterDay = 'Wednesday'
        elif weekCounter == 3:
            weekCounterDay = 'Thursday'
        elif weekCounter == 4:
            weekCounterDay = 'Friday'
        else:
            print("An error has occurred in the 'weekCounter' for loop.")

        while True:
            try:
                storedValue = int(input(
                    f'Please enter how many minutes early (+) / late (-) Bus {storedBusLetter.title()} was on '
                    f'{weekCounterDay}:'))
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
            printList(storedBusLetter, storedWeek)
        elif storedBusLetter == 'c':
            weekChecker().append(storedValue)
            printList(storedBusLetter, storedWeek)
        elif storedBusLetter == 'd':
            weekChecker().append(storedValue)
            printList(storedBusLetter, storedWeek)
        elif storedBusLetter == 'e':
            weekChecker().append(storedValue)
            printList(storedBusLetter, storedWeek)
        elif storedBusLetter == 'f':
            weekChecker().append(storedValue)
            printList(storedBusLetter, storedWeek)
        else:
            print("The program has run into an error in the 'weekCounter' function. Please try again.")


    def editQueryFunction():
        editQuery = input(f"Would you like to edit anything from Week {storedWeek}? (y / n)")
        while editQuery != 'y' and editQuery != 'n':
            print('Invalid input! Please try again:')
            editQuery = input(f"Would you like to edit anything from Week {storedWeek}? (y / n)")
        print('Valid value entered.')
        return editQuery


    queryEdit = editQueryFunction()


    def queryFunction():
        newNumberInput = int(0)
        if queryEdit == 'y':
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

            continueQuery = input('Would you like to edit another value? (y / n)')
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
        elif queryEdit == 'n':
            print("Thank you for using this service.")
            printList(storedBusLetter, storedWeek)


    currentLatestBusNumber = 0
    currentLatestBusWeek = 'null'
    currentLatestBusLetter = 'null'

    queryFunction()
    forWeekNumber = 0
    late = 0
    lateNumbers = []
    early = 0
    onTime = 0


    def latestBusFunction():
        global currentLatestBusNumber
        global currentLatestBusWeek
        global currentLatestBusLetter
        for latestBusFunctionCounter in range(0, len(lateNumbers)):
            if lateNumbers[latestBusFunctionCounter] < currentLatestBusNumber:
                currentLatestBusNumber = lateNumbers[latestBusFunctionCounter]
                currentLatestBusWeek = storedWeek
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
        lateAverage = 0
        for averageLateCheckerCounter in range(0, len(lateNumbers)):
            lateTotal += lateNumbers[averageLateCheckerCounter]
        try:
            lateAverage = lateTotal / len(lateNumbers)
        except ZeroDivisionError:
            print(f"Bus {storedBusLetter.title()} was not late this week.")
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
            queryOfTheUser()
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

print(
    f"The latest bus was Bus {currentLatestBusLetter.title()} on Week {currentLatestBusWeek} with a maximum late "
    f"time of {currentLatestBusNumber}")

userAnalysisUserState = 'y'


def userAnalysis(userAnalysisDay, userAnalysisBus):
    userAnalysisLateNumber = 0
    if userAnalysisDay == 'mon':
        userAnalysisLateNumber = weekChecker()[0]
    elif userAnalysisDay == 'tue':
        userAnalysisLateNumber = weekChecker()[1]
    elif userAnalysisDay == 'wed':
        userAnalysisLateNumber = weekChecker()[2]
    elif userAnalysisDay == 'thu':
        userAnalysisLateNumber = weekChecker()[3]
    elif userAnalysisDay == 'fri':
        userAnalysisLateNumber = weekChecker()[4]
    else:
        print("The program has run into an error at the 'userAnalysis' function.")
    if userAnalysisLateNumber >= 0:
        print(f"Bus {userAnalysisBus.title()} was not late on {userAnalysisDay.title()}!")
    elif userAnalysisDay < 0:
        print(
            f"Bus {userAnalysisBus.title()} was {userAnalysisLateNumber * -1} minutes late on {userAnalysisDay.title()}.")
    else:
        print("Impossible error has been made...")


while userAnalysisUserState == 'y':
    userAnalysis(day(), bus())
    userAnalysisUserState = input('Would you like to input another value? (y / n)')
    if userAnalysisUserState != 'n' and userAnalysisUserState != 'y':
        print("Please enter 'y' / 'n'")
    elif userAnalysisUserState == 'n':
        break
