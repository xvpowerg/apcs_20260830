def func1(a,b,c):
    ans = a + b * c
    return ans,a,b,c
v1,a,b,c = func1(5,2,3)
print(f"{a}+{b}*{c}={v1}")

v2,*a = func1(5,2,3)

print(f"{v2} {a[1]} {a[2]}")
