def sortH(data):
    return data[1]
info = [("Ken",178),("Joy",150),("Alice",165),("Bob",175)]
info.sort(key=sortH)
print(info)
