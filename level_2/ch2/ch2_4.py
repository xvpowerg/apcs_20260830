y = []
for i in range(1,10):
    y.append(i**2)
print(y)    
y2 = [i**2 for i in range(1,10)]
print(y2)    
x = [i for  i in range(1,10) if i % 2 == 0] 
print(x)    

d1 = {x:x**2 for x in range(1,10)}
print(d1)
