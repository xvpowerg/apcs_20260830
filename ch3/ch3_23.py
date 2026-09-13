def  myMap(myList):
    results = []
    for v in myList:
        results.append(str(v))
    return     results
        
data = [1.2,8.7,5.2]
print(data)

newData = myMap(data)
print(newData)

data2 = ["15","30","40"]
myMap(data2)

