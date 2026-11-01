#print(ord("A"))#文字轉數字
#print(chr(65))#數字轉文字
c = 65
for i in range(0,5):
    for j in range(0,5):
        if j == i :
            continue
        for k in range(0,5):
            if  k ==i or k ==j:
                continue
            for l in range(0,5):
                if l ==k or l == j or  l == i:
                    continue
                for m in range(0,5):
                    if m ==l or m ==k or m == j or m == i:
                        continue
                    print(f"{chr(c+i)},{chr(c+j)},{chr(c+k)},{chr(c+l)},{chr(c+m)}")
                
