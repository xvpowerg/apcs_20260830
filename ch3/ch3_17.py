cars = ["Honda","Ford","Toyta","Ford","BMW"]
print("移除前:",cars)
print("移除前長度:",len(cars))

remove_key = "Ford"
cars.remove(remove_key)
print("移除後:",cars)
print("移除後長度:",len(cars))

print(remove_key in cars)
