newList =  list(map(int,input().split()))
a,b,c = sorted(newList)
print(a,b,c)

if a+b <= c:
    print("No")
elif a**2 + b **2 < c **2:
    print("Obtuse")#鈍角
elif a **2 + b**2  == c ** 2 :
    print("Right")#直角
else:
    print("Acute")#銳角
