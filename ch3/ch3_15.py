cars = ["Honda","Toyta","Ford","BMW"]
print("彈出前:",cars)
print("長度:",len(cars))
p1_car = cars.pop()
print("彈出後1:",cars)
print("長度:",len(cars))
print("p1_car:",p1_car)#彈出後面

p2_car = cars.pop(0)
print("彈出後2",cars)
print("長度:",len(cars))
print("p2_car:",p2_car)
#cars.pop(9)#IndexError: pop index out of range
cars.pop()
cars.pop()
print("長度:",len(cars))
cars.pop()
