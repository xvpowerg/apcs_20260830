class Employee:
    def __init__(self,name,salary=28000):#每個物件都要設定的事
                self.name = name
                self.salary = salary
    def printInfo(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print()
emp1 = Employee("Lucy",72000)
emp1.printInfo()
emp2 = Employee("Iris")
emp2.printInfo()
