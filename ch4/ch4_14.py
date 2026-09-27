funcList = [lambda x:x**2,lambda  x:x**3,lambda x:x*2]
list1 = [1,2,3,4,5]
list2 = []
for v in list1:
    for f in funcList:        
        list2.append(f(v))
    
print(list2)
