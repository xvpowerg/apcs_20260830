def  myMap(func,myList):
    results = []
    for v in myList:
        results.append(func(v))
    return     results
def toStr(v):
    return str(v)
def toInt(v):
    return int(v)
data = [1.2,8.7,5.2]
print(data)

newData = myMap(toStr,data)
print(newData)
print("======================")
data2 = ["15","30","40"]
print(data2)
newData2 = myMap(toInt,data2)
print(newData2)

