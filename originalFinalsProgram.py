currentDay = 0
prevDays = 0
adultCount = 0
childCount = 0
seniorCount = 0
familyCount = 0
groupCount = 0
userMoney = 0
repeat = 'false'


# Booking for how many days?
# loop to get booking inputs?
# booking complete? N: loop
#                   Y: check best value AND then continue
# loop to new booking

# assumptions: an adult OR senior may bring up to 2 children

# booking variables:
#  adultCount
#  childCount
#  seniorCount
#  familyCount
#  groupCount
#  lionCount
#  penguinCount
#  bbqCount


def printTable():
    print('|-------------------------------------------------|--------------|---------------|')
    print('|                   Ticket Type                   | Cost (1 day) | Cost (2 days) |')
    print('|-------------------------------------------------|--------------|----------------|')
    print('| 1 Adult                                         | $ 20.00      | $ 30.00       |')
    print('|-------------------------------------------------|--------------|---------------|')
    print('| 1 Child (max. 2 per Adult)                      | $ 12.00      | $ 18.00       |')
    print('|-------------------------------------------------|--------------|---------------|')
    print('| 1 Senior (age 60+)                              | $ 16.00      | $ 24.00       |')
    print('|-------------------------------------------------|--------------|---------------|')
    print('| Family Ticket (2 Adults/Seniors + 3 Children)   | $ 60.00      | $ 90.00       |')
    print('|-------------------------------------------------|--------------|---------------|')
    print('| Groups of 6/more (cost per person)              | $ 15.00      | $ 22.50       |')
    print('|-------------------------------------------------|--------------|---------------|')
    print('')


def printAttractions(days):
    print('|------------------------------------------|-------------------|')
    print('|             Extra Attraction             | Cost (per person) |')
    print('|------------------------------------------|-------------------|')
    print('| Lion Feeding                             | $2.50             |')
    print('|------------------------------------------|-------------------|')
    print('| Penguin Feeding                          | $2.00             |')
    print('|------------------------------------------|-------------------|')
    if days == 2:
        print('| Evening Barbecue (2 days tickets only)   | $5.00             |')
        print('|------------------------------------------|-------------------|')
    print('')


# def returnTicketCost(user, days, groupNumber):
#     cost = 0
#     if user == 'adult':
#         cost = 20
#     elif user == 'child':
#         cost = 12
#     elif user == 'senior':
#         cost = 16
#     elif user == 'family':
#         cost = 60
#     elif user == 'groups':
#         cost = 15
#
#     if days == 2:
#         cost = cost * 1.5
#     if (user == 'groups') or (user == 'child'):
#         cost = cost * groupNumber
#
#     return cost


def returnAttractionCost(attraction):
    if attraction == 'evening':
        attractionCost = 5
    elif attraction == 'penguin':
        attractionCost = 2
    elif attraction == 'lion':
        attractionCost = 2.5
    else:
        attractionCost = 0

    return attractionCost


def attractionInput(days):
    printAttractions(days)
    selectedDay = 0
    while True:
        # todo: enter first letter only (upper case or lower case)
        attraction = input(
            "Which attraction(s) would you like to do? Just enter the first word of the 'Extra Attraction'! (e.g. penguin) ")
        attraction.lower()
        if (attraction == 'lion') or (attraction == 'penguin') or ((attraction == 'evening') and (days == 2)):
            break
    return attraction


def groupInputFunction(groupNumber):
    while True:
        try:
            groupNumber = int(input("Please input the number '6' or more! "))
        except ValueError:
            print("Please enter a number!")
            continue
        if (groupNumber >= 6) or (groupNumber == 0):
            break
    return groupNumber


def userSummary(days, attractionCost):
    costMod = 0
    if days == 1:
        costMod = 1
    elif days == 2:
        costMod = 1.5

    print('')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                   Ticket Type                   |   {days} day(s)   |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                      Adult                      | Amount: {adultCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {adultCount * 20 * costMod}       |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                      Child                      | Amount: {childCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {childCount * 12 * costMod}       |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                     Senior                      | Amount: {seniorCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {seniorCount * 16 * costMod}       |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                     Family                      | Amount: {familyCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {familyCount * 60 * costMod}       |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                      Group                      | Amount: {groupCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {groupCount * 15 * costMod}       |')
    print(f'|-------------------------------------------------|------------------|')
    print('')


def intChecker(text):
    while True:
        try:
            returnValue = int(input(text))
        except ValueError:
            print('Please enter a number!')
            continue
        else:
            break
    return returnValue


def rangeIntChecker(text, low, high):
    while True:
        try:
            returnValue = int(input(text))
        except ValueError:
            print('Please enter a number!')
            continue
        if (returnValue >= low) and (returnValue <= high):
            break
        else:
            print(f"Please enter a value from {low} to {high}!")
    return returnValue


def userInputChecker(repeat):
    global adultCount
    global childCount
    global seniorCount
    global familyCount
    global groupCount
    global prevDays
    global userMoney
    global currentDay
    global prevDays
    if repeat == 'false':
        days = 0
    elif repeat == 'true':
        days = prevDays

    printTable()
    if repeat == 'false':
        while True:
            try:
                days = int(input("How many days would you like to stay for? (1 or 2) "))
            except ValueError:
                print("Please input '1' or '2'!")
                continue
            if (days == 1) or (days == 2):
                break

    if repeat == 'false':
        adultCount += intChecker("For how many adults? ")
        seniorCount += intChecker("For how many seniors?")
        childCount += rangeIntChecker("For how many children? ", 0, (adultCount + seniorCount) * 2)
        familyCount += intChecker("How many family tickets? ")
        groupCount += intChecker("How many people would you like in your group? (Enter '0' for no group!) ")
        groupInputFunction(groupCount)
    elif repeat == 'true':
        adultCount += intChecker("For how many more adults? ")
        seniorCount += intChecker("For how many more seniors?")
        childCount += rangeIntChecker("For how many more children? ", 0, (adultCount + seniorCount) * 2)
        familyCount += intChecker("How many more family tickets? ")
        groupCount += intChecker("How many more people would you like in your group? (Enter '0' for no group!) ")
        groupInputFunction(groupCount)

    # try:
    #         if user[i - 1] == 'adult':
    #             while True:
    #                 childInput = input("Would you like to buy tickets for children? (y / n) ")
    #                 childInput.lower()
    #                 if childInput == 'y':
    #                     adultCount += 1
    #                     childPresence = 'true'
    #                     break
    #                 elif childInput == 'n':
    #                     childPresence = 'false'
    #                     break
    #     except IndexError:
    #         'null'
    #
    #     n = i
    #     groupNumber = 0
    #
    #     printTable()
    #     if adultCount == 0:
    #         user.append(input(
    #             "Who would you like to book a ticket for? Just enter the first word of the 'Ticket Type'! (e.g. senior, family) "))
    #     elif (childPresence == 'true') and (childInput == 'y'):
    #         user.append('child')
    #     user[i].lower()

    #     while True:
    #         if user[i] == 'group':
    #             user[i] = 'groups'
    #         if (user[i] == 'groups') or ((user[i] == 'child') and (adultCount > 0)):
    #             try:
    #                 if user[i] == 'groups':
    #                     groupNumber = groupInputFunction(groupNumber)
    #                 elif user[i] == 'child':
    #                     groupNumber = int(input("Tickets for how many? "))
    #             except ValueError:
    #                 if user[i] == 'groups':
    #                     print("Please input '6' or more!")
    #                 elif user[i] == 'child':
    #                     print("Max 2 per adult!")
    #                 else:
    #                     print("Please input a number!")
    #                 continue
    #         if (groupNumber >= 6) or (
    #                 (user[i] == 'adult') or (
    #                 (user[i] == 'child') and ((groupNumber > 0) and (groupNumber < 3) and adultCount > 0)) or (
    #                         user[i] == 'senior') or (user[i] == 'family') or (
    #                         user[i] == 'groups')):
    #             if user[i] == 'family':
    #                 groupNumber = 5
    #             break
    #         else:
    #             if user[i] != 'child':
    #                 user[i] = input("Please enter a valid 'Ticket Type'! ")
    #             else:
    #                 if adultCount > 0:
    #                     print("Max 2 per adult!")
    #                 else:
    #                     userInputChecker(n)

    while True:
        attractionAsk = input("Would you like to do extra attractions? (y / n) ")
        if attractionAsk == 'y':
            userAttraction = attractionInput(currentDay)
            break
        elif attractionAsk == 'n':
            userAttraction = 'null'
            break
    attractionCost = intChecker(f"How many {userAttraction} tickets would you like to buy?")

    while True:
        moreInput = input("Would you like to buy tickets for anyone else? (y / n) ")
        if moreInput == 'y':
            userSummary(days, attractionCost)
            prevDays = days
            return 'true'
        elif moreInput == 'n':
            userSummary(days, attractionCost)
            currentDay = 0
            prevDays = 0
            adultCount = 0
            childCount = 0
            seniorCount = 0
            familyCount = 0
            groupCount = 0
            userMoney = 0
            return 'false'


def userInput():
    global repeat
    print("Welcome to the Wildlife Park booking system!")
    while True:
        repeat = userInputChecker(repeat)


# main program
userInput()
