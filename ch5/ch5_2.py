numStr = input()
A,B = 0,0
numLen = len(numStr)
for i in range(-1,-numLen-1,-1):
    if i % 2 != 0:
        A = A + int(numStr[i])
    else:
       B = B + int(numStr[i])

x = abs(A-B)
print(x)
