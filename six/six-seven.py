person = {'firstName': 'bob', 'lastName': 'bill', 'city': 'baskerville'}
print(f"First name: {person['firstName'].title()}")
print(f"Last name: {person['lastName'].title()}")
print(f"City: {person['city'].title()}")
people = {
    'urmom': {
        'firstName': 'ur',
        'lastName': 'mom',
        'city': 'farts'
    },
    'poopoo': {
        'firstName': 'mom',
        'lastName': 'ur',
        'city': 'straf'
    },
    'bobBill':{
        'firstName': 'bob',
        'lastName': 'bill',
        'city': 'baskerville'}
}

for personNumber, personInfo in people.items():
    print(f"First Name: {personInfo['firstName']}")
    print(f"Last Name: {personInfo['lastName']}")
    print(f"City: {personInfo['lastName']}\n")
