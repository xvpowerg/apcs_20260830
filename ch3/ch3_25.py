def sortMyLen(s):
    return len(s)
def sortUpper(s):
    return s.upper()
cars = ['honda','BMW','Toyota','audi']
print(cars)
cars.sort()
print(cars)
cars.sort(key=sortMyLen)
print(cars)
cars.sort(key=sortUpper)
print(cars)
mySr = "abc"
print(mySr.upper())

