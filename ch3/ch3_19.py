cars = ["Honda","Ford","Toyta","Ford","BMW"]
print("刪除前:",cars)
print("刪除前長度:",len(cars))

del cars[4]
print("刪除後:",cars)
print("刪除後長度:",len(cars))
del cars[1:3]
print("刪除後:",cars)
print("刪除後長度:",len(cars))
