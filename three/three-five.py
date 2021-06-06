invDinner = ['Burp', 'Tyee', 'Puu']
dinNum = 0
for dinNum in range (3):
    print('Dear ' + invDinner[dinNum] + ', please come for dinner.')
    dinNum += 1
print("Hold up. Idiot Burp can't make it because he's too cool.")
del(invDinner[0])
print("I'll just call upon... The Fart!")
invDinner.append("Fart")
dinNum = 0
for dinNum in range (3):
    print('Dear ' + invDinner[dinNum] + ', please come for dinner.')
    dinNum += 1
