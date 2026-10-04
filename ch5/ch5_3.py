a,b,c =  map(int,input().split())
a,b,c = sorted([a,b,c],reverse = True)
print(a,b,c)
if a == b and b == c:
    print("3",a)
elif a != b and b == c:
    print("2",a,b)
elif a == b and b != c:
    print("2",b,c)
else:
    print("1",a,b,c)
