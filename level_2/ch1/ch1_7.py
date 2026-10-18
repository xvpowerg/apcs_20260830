class Point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __lt__(self,other):
        self_msg = (self.x ** 2) + (self.y ** 2)
        other_msg = (other.x **2) + (other.y **2)
        return self_msg < other_msg
p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(3,7)
p4 = Point(6,2)
print(p1 < p2)
myList = [p1,p2,p3,p4]
myList.sort()
for p in myList:
    print(p)
