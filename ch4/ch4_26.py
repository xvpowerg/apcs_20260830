mydata = []
#預設值為100 有300各100
for i in range(300):
    mydata.append(100)

print(len(mydata))
print(mydata[1])

mydata = [100]*300
print(len(mydata))
print(mydata[5])
try:
    num1 = 10
    num2 = 0
    num1 / num2
    
except:
    print("例外發生")
finally:#一定做一次
     print("清除")
     mydata = []  
print(len(mydata))

