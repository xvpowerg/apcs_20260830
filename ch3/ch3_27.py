name = {"Ken","Joy","Lucy","Ken","Lucy"} #結構本身為set會移除重複
print(name)
print(len(name))#長度

name.add("Iris")
print(name)

#轉換為List
myList = list(name)
print(myList)
myList.append("Ken")
print(myList)
#轉換為set
mySet = set(myList)
print(mySet)
