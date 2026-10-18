def dec_to_bin(num):
    myList = []
    while True:
        num,reminder = divmod(num,2)#商 餘數
        myList.append(str(reminder))
        if num == 0:
            return "".join(myList[::-1])
def dec_to_oct(num):
    myList = []
    while True:
        num,reminder = divmod(num,8)#商 餘數
        myList.append(str(reminder))
        if num == 0:
            return "".join(myList[::-1])

#16進位
#A B C D E F        
def dec_to_hex(num):
    base = ['0',"1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    myList = []
    while True:
        num,rem = divmod(num,16)
        myList.append(base[rem])
        if num == 0:
            return "".join(myList[::-1])

num = int(input("輸入十進位")   )
#print( dec_to_bin(num))
print(dec_to_hex(num))
