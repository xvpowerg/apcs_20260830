def myMap(func,myList):
    result = []
    for i in myList:
        result.append(func(i))
    return result

dataList = ["12","8","62","13"]
result = myMap(lambda x:int(x),dataList)
print(dataList)
print(result)

dataList = [12,8,62,13]
result = myMap(lambda x:str(x),dataList)
print(dataList)
print(result)
