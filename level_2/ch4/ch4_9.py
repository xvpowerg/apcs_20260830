def printList(data):
    for s in data:
        print(s,end=" | ")
    print()    
        
class Student:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def __str__(self):
        return f"{self.name} {self.age} {self.gpa}"
    def __lt__(self,other):
        if self.age < other.age:
            return True
        else:
            return False
data=[Student('Amy', 15, 4.2),
      Student('Bill', 16, 3.8),
      Student('Chris', 13, 4.0),
      Student('David', 19, 4.8),
      Student('Ed', 17, 2.6)]    
printList(data)
n = len(data)
for i in range(n-1):
    minIdx = i
    for j in range(i+1,n):
        if data[j] < data[minIdx]:
            minIdx = j
    data[i],data[minIdx] = data[minIdx],data[i]
    printList(data)
    
