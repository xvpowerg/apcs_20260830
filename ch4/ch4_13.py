def funcPow(x):
    return x ** 2
def func2(x):
    return x ** 3
def func3(x):
    return x * 2

funcList = [funcPow,func2,func3]
list1 = [1,2,3,4,5]
list2 = []
for v in list1:
    for f in funcList:        
        list2.append(f(v))
    
print(list2)
