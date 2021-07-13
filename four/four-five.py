numbers = []
for i in range(1, 1000001):
    numbers.append(i)
    i += 1
print("min: " + str(min(numbers)))
print("max: " + str(max(numbers)))
print("sum: " + str(sum(numbers)))
