a = 20
def func():
    global a #跟python說a是全域變數
    a += 1

print("Func呼叫前:",a)
func()
print("Func呼叫後:",a)
