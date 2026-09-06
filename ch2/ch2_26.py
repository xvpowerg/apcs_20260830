word = "AcFgAuIok"
#兩個變數 v1 存放word的大寫字母
#v2存放word的小寫字母
v1 = ""
v2 = ""
for v in word:
    if v >= "A" and v <= "Z":
        v1+=v
    else:
        v2 +=v
print(v1)
print(v2)
