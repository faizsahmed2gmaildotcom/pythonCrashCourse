burp = 9
numbers = []
for numberListMaker in range(1, 10):
    numbers.append(numberListMaker)
for i in range(burp):
    if numbers[i] == 1:
        print(str(numbers[i]) + 'st')
    elif numbers[i] == 2:
        print(str(numbers[i]) + 'nd')
    elif numbers[i] == 3:
        print(str(numbers[i]) + 'rd')
    else:
        print(str(numbers[i]) + 'th')
