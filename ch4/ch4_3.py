def func(a): #在func新宣告了一個a
    a = 99
    print("func 內的 a:",a)
a = 200
func(a)
print("func 外的 a:",a)
    
