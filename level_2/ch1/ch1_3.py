class Employee:
    def __init__(self,name,salary=28000):#每個物件都要設定的事
                self.name = name
                self.salary = salary

emp1 = Employee("Sean",50000)
print(emp1.name)
print(emp1.salary)
emp2 = Employee("Iris",25000)
print(emp2.name)
print(emp2.salary)
emp3 = Employee("Joy")
print(emp3.name)
print(emp3.salary)
