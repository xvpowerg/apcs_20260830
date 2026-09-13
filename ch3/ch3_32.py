myList = [("Ken",100),("Iris",89),("Ken",50),("Lucy",85),("Iris",77),("Lucy",82),("Iris",61)]


group = {}
for k,v in myList:
    oldValue = group.get(k,0)
    oldValue += v
    group[k] = oldValue

    
print(group)
