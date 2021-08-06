a = 0
b = 1
c = 1
FBNum = 0
def generate_next_fib(a, b, c):
    a = b
    b = c
    c = a + b
    return a, b, c

while FBNum != int(161803398875):
    a, b, c = generate_next_fib(a, b, c)
    FBNum = int((c / b) * 100000000000)
    print(str(c) + ',', str(b) + '  ', str(FBNum / 100000000000))
