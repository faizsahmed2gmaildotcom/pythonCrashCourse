# 1
cloudCover = int(input('Input the cloud cover %: '))
UVIndex = int(input('Input the UV index: '))
if (cloudCover < 50) and (UVIndex >= 7):
    print('Sunscreen is required!')
else:
    print('Sunscreen is not needed.')

# 2
A = int(input('Input a number for A: '))
B = int(input('Input a number for B: '))
C = int(input('Input a number for C: '))
D = int(input('Input a number for D: '))
if (A > B or (C < D and A > C)) and (C != D):
    print(True)
else:
    print(False)

# 3
A = int(input('Input a number for A: '))
B = int(input('Input a number for B: '))
C = int(input('Input a number for C: '))
D = int(input('Input a number for D: '))
if ((A > D) and (B < C and A < C)) or ((D > A) and (A > C)):
    print('These numbers are true, according to me!')
else:
    print('For some reason, these numbers are false!')
