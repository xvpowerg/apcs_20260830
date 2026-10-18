x = [5,15,25,35,45]
for data in x:
    print(data,end=" ")
print()
for i in range(len(x)):
    print(i,x[i],end=" ")
print()   
x.insert(2,100)
print(x)
x.append(200)
print(x)
x[2] = 30
print(x)
x.remove(30)
print(x)
n = x.pop()
print("pop:",n)
print(x)
n = x.pop(2)
print("pop:",n)
print(x)
