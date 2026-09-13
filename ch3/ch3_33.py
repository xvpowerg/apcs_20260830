a = 10#全域
def func():
    #區域變數
    a = 25 #選告了一個新a
    print("func內部:",a)
    
print("外部的a:",a)
func()
print("外部的a:",a)
