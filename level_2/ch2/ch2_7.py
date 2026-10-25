a1 = [-1]*11
print(a1)
print(len(a1))

p = [[i*2]*5  for i in range(10)]
print(len(p),"x",len(p[0]))

for v1 in p :
    for v2 in v1:
        print(v2,end=" ")
    print()
print()    
