import math

days = 0
prevDays = 0
adultCount = 0
childCount = 0
seniorCount = 0
familyCount = 0
groupCount = 0
userMoney = 0
repeat = False
lionCount = 0
penguinCount = 0
eveningCount = 0


# TODO: a booking can be made up to a week in advance; show the days available for booking;
# TODO: allocate a unique booking number

def printTable():
    print('|-------------------------------------------------|--------------|---------------|')
    print('|                   Ticket Type                   | Cost (1 day) | Cost (2 days) |')
    print('|-------------------------------------------------|--------------|---------------|')
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


def attractionInput(days):
    printAttractions(days)
    while True:
        attraction = input(
            "Which attraction would you like to do? Just enter the first word of the 'Extra Attraction'! (e.g. penguin) ")
        attraction.lower()
        if (attraction == 'lion') or (attraction == 'penguin') or ((attraction == 'evening') and (days == 2)):
            break
    return attraction


def userSummary(days, attractionLion, attractionPenguin, attractionEvening):
    costMod = 0
    if days == 1:
        costMod = 1
    elif days == 2:
        costMod = 1.5

    # task 2
    print('')
    print(f'|                  Your Summary                   |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                   Ticket Type                   |     {days} Day(s)     |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                      Adult                      | Amount: {adultCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {adultCount * 20 * costMod}     |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                      Child                      | Amount: {childCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {childCount * 12 * costMod}     |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                     Senior                      | Amount: {seniorCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {seniorCount * 16 * costMod}     |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                     Family                      | Amount: {familyCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {familyCount * 60 * costMod}     |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                      Group                      | Amount: {groupCount}        |')
    print(f'|-------------------------------------------------| Cost: $ {groupCount * 15 * costMod}     |')
    print(f'|-------------------------------------------------|------------------|')
    print('')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                 Attraction Type                 |   {days} day(s)       |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                  Lion Feeding                   | Amount: {attractionLion}       |')
    print(f'|-------------------------------------------------| Cost: $ {attractionLion * 2.5}     |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                 Penguin Feeding                 | Amount: {attractionPenguin}       |')
    print(f'|-------------------------------------------------| Cost: $ {attractionPenguin * 2}     |')
    print(f'|-------------------------------------------------|------------------|')
    print(f'|                Evening Barbecue                 | Amount: {attractionEvening}       |')
    print(f'|-------------------------------------------------| Cost: $ {attractionEvening * 5}     |')
    print(f'|-------------------------------------------------|------------------|')
    print('')


def intChecker(text):
    returnValue = None
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
    returnValue = None
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


def attractionAmount(attraction):
    global penguinCount
    global lionCount
    global eveningCount
    while True:
        amount = intChecker(f"How many {attraction} tickets would you like to buy? ")
        if attraction == 'penguin':
            penguinCount += amount
            break
        elif attraction == 'lion':
            lionCount += amount
            break
        elif attraction == 'evening':
            eveningCount += amount
            break


def YorN(text):
    while True:
        returnValue = input(text)
        returnValue.lower()
        if (returnValue == 'y') or (returnValue == 'n'):
            return returnValue


def askAttraction():
    global days
    while True:
        attractionAsk = input("Would you like to do extra attractions? ('y' / 'n') ")
        attractionAsk.lower()
        if attractionAsk == 'y':
            userAttraction = attractionInput(days)
            attractionAmount(userAttraction)
        elif attractionAsk == 'n':
            break


# task 3
def simplify(adult, child, senior, family, groupAdult, groupSenior, groupChild):
    global adultCount
    global childCount
    global seniorCount
    global familyCount
    global groupCount
    adultSeniorMath = math.floor((adult + senior) / 2)
    childMath = math.floor(child / 3)

    # family simplification
    if ((adult + senior) >= 2) and (child >= 3):
        familyConvertQuery = YorN(
            f"Would you like to buy Family Ticket(s) instead of {adult} Adult, {senior} Senior, and {child} Children tickets? ('y' / 'n') ")
        if familyConvertQuery == 'y':
            if adultSeniorMath <= childMath:
                familyConvertAmount = adultSeniorMath
            else:
                familyConvertAmount = childMath
            for b in range(familyConvertAmount):
                if child >= 3:
                    child -= 3
                else:
                    break
                if adult >= 2:
                    adult -= 2
                elif senior >= 2:
                    senior -= 2
                else:
                    break
                family += 1

    # group simplification
    if (senior != 4) or (child != 2):
        if ((adult + senior) >= 6) and (childMath < adultSeniorMath):
            groupConvertQuery = YorN(
                f"Would you like to buy Group Ticket(s) instead of {adult} Adults and {senior} Senior tickets? ('y' / 'n') ")
            if groupConvertQuery == 'y':
                while True:
                    adultSeniorMath = math.floor((adult + senior) / 2)
                    childMath = math.floor(child / 3)
                    if childMath >= adultSeniorMath:
                        break
                    if adult > 0:
                        adult -= 1
                    elif senior > 0:
                        senior -= 1
                    groupCount += 1

    adultCount = adult
    childCount = child
    seniorCount = senior
    familyCount = family


#           elif groupConvertQuery == 'n':
#               adultCount -= groupAdult
#               seniorCount -= groupSenior
#               childCount -= groupChild
#               groupCount += (groupAdult + groupSenior + groupChild)


def userInputChecker(repeat):
    global adultCount
    global childCount
    global seniorCount
    global familyCount
    global groupCount
    global prevDays
    global userMoney
    global days
    global lionCount
    global penguinCount
    global eveningCount
    groupAdultCount = 0
    groupSeniorCount = 0
    groupChildCount = 0

    printTable()
    if not repeat:
        days = rangeIntChecker("How many days would you like to stay for? (1 or 2) ", 1, 2)
        adultCount += intChecker("For how many adults? ")
        seniorCount += intChecker("For how many seniors? ")
        childCount += rangeIntChecker("For how many children? ", 0, (adultCount + seniorCount) * 2)
        familyCount += intChecker("How many family tickets? ")
        groupQuery = YorN("Would you like to create a Group ticket? ('y' / 'n') ")
    else:
        days = prevDays
        adultCount += intChecker("For how many more adults? ")
        seniorCount += intChecker("For how many more seniors? ")
        childCount += rangeIntChecker("For how many more children? ", 0, (adultCount + seniorCount) * 2)
        familyCount += intChecker("How many more family tickets? ")
        groupQuery = YorN("Would you like add to your create a Group ticket? ('y' / 'n') ")

    if groupQuery == 'y':
        while True:
            groupAdultCount = intChecker("Group with how many adults? ")
            groupSeniorCount = intChecker("Group with how many seniors? ")
            groupChildCount = rangeIntChecker("Group with how many children? ", 0, (adultCount + seniorCount) * 2)
            groupTotal = groupAdultCount + groupSeniorCount + groupChildCount
            if groupTotal < 6:
                print(f"Group tickets must have at least 6 people in them! You have {groupTotal}.")
            else:
                break
        adultCount += groupAdultCount
        seniorCount += groupSeniorCount
        childCount += groupChildCount

    askAttraction()

    while True:
        moreInput = input("Would you like to buy tickets for anyone else? ('y' / 'n') ")
        if moreInput == 'y':
            userSummary(days, lionCount, penguinCount, eveningCount)
            prevDays = days
            return True
        elif moreInput == 'n':
            simplify(adultCount, childCount, seniorCount, familyCount, groupAdultCount, groupSeniorCount,
                     groupChildCount)
            userSummary(days, lionCount, eveningCount, penguinCount)
            days = 0
            prevDays = 0
            adultCount = 0
            childCount = 0
            seniorCount = 0
            familyCount = 0
            groupCount = 0
            userMoney = 0
            lionCount = 0
            penguinCount = 0
            eveningCount = 0
            return False


def userInput():
    global repeat
    print("Welcome to the Wildlife Park booking system!")
    repeat = userInputChecker(repeat)


# main program
while True:
    userInput()
