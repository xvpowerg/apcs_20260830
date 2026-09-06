listOfTuple = [(5,6),(7,10),(8,13),(7,2)]
myMax = -1
mySum = 0

for v in listOfTuple:
    v1,v2 =v
    if v1 >myMax:
        myMax = v1
    if v2 >  myMax:
        myMax = v2
    mySum += v1 + v2        
print(myMax)
print(mySum)
