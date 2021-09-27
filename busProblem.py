def week():
    internalWeek = input('Please enter the week:')
    if internalWeek != '1' and internalWeek != '2' and internalWeek != '3' and internalWeek != '4':
        print('Invalid week! Please try again:')
        week()
    else:
        print('Valid value entered.')
        return internalWeek


def day():
    internalDay = input('Please enter the day (e.g. mon, thu):')
    if internalDay != 'mon' and internalDay != 'tue' and internalDay != 'wed' and internalDay != 'thu' and internalDay != 'fri':
        print('Invalid day! Please try again:')
        day()
    else:
        print('Valid value entered.')
        return internalDay


def bus():  # Only 'Bus A' will be used for the sake of testing
    internalBus = input('Please enter the bus letter:')
    if internalBus != 'a' and internalBus != 'b' and internalBus != 'c' and internalBus != 'd' and internalBus != 'e' and internalBus != 'f':
        print('Invalid bus letter! Please try again:')
        bus()
    else:
        print('Valid value entered.')
    return internalBus


storedWeek = week()
storedBusLetter = bus()
busData = {
    'week': 'Week: ' + str(storedWeek),
    'letter': 'Bus Letter: ' + str(storedBusLetter.title()),
}


def userConfirm():
    print('Please confirm that this is your entered data:')
    for dataCounter in busData.values():
        print(f'{dataCounter}')
    confirmation = input('y / n')
    if confirmation != 'y' and confirmation != 'n':
        userConfirm()
    elif confirmation == 'n':
        print("Please run the program again to resubmit.")
        exit()
    else:
        print('Values registered.')


userConfirm()

weekOneA = []
weekOneB = []
weekOneC = []
weekOneD = []
weekOneE = []
weekOneF = []


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
    elif storedBusLetter == 'b':
        return weekOneF
    else:
        print("The program has run into an error at the 'weekChecker' function. Please try again.")


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
    storedValue = input(
        f'Please enter how many minutes early (+) / late (-) Bus {storedBusLetter.title()} was on Day '
        f'{weekCounter + 1}:')
    if storedBusLetter == 'a':
        weekChecker().append(storedValue)
        printList(storedBusLetter, storedWeek)
    elif storedBusLetter == 'b':
        weekOneB.append(storedValue)
    elif storedBusLetter == 'c':
        weekOneC.append(storedValue)
    elif storedBusLetter == 'd':
        weekOneD.append(storedValue)
    elif storedBusLetter == 'e':
        weekOneE.append(storedValue)
    elif storedBusLetter == 'f':
        weekOneF.append(storedValue)
    else:
        print("The program has run ino an error in the 'weekCounter' function. Please try again.")


def editQueryFunction():
    editQuery = input(f"Would you like to edit anything from Week {storedWeek}? (yes / no)")
    if editQuery != 'yes' and editQuery != 'no':
        print('Invalid input! Please try again:')
        editQueryFunction()
    else:
        print('Valid value entered.')
        return editQuery


queryEdit = editQueryFunction()


def queryFunction():
    if queryEdit == 'yes':
        dayChange = day()
        if dayChange == 'mon':
            weekChecker()[0] = input('Input new number:')
        elif dayChange == 'tue':
            weekChecker()[1] = input('Input new number:')
        elif dayChange == 'wed':
            weekChecker()[2] = input('Input new number:')
        elif dayChange == 'thu':
            weekChecker()[3] = input('Input new number:')
        elif dayChange == 'fri':
            weekChecker()[4] = input('Input new number:')
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


queryFunction()


def queryOfTheUser():
    userQueryAgainOfTheUser = input("Would you like to enter data for a different week? (y / n)")
    if userQueryAgainOfTheUser != 'y' and userQueryAgainOfTheUser != 'n':
        print("Invalid input. Please try again.")
    elif userQueryAgainOfTheUser == 'y':
        storedWeek = week()
        storedBusLetter = bus()
        # run main program again here
    elif userQueryAgainOfTheUser == 'n':
        print("Exiting...")
    else:
        print("Well... this error is impossible to achieve. I guess congrats?")


queryOfTheUser()
