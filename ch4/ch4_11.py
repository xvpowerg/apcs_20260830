def strToInt(v):
    return int(v)
def intToStr(v):
    return str(v)

def myMap(func,myList):
    result = []
    for i in myList:
        result.append(func(i))
    return result

dataList = ["12","8","62","13"]
result = myMap(strToInt,dataList)
print(dataList)
print(result)

dataList = [12,8,62,13]
result = myMap(intToStr,dataList)
print(dataList)
print(result)
