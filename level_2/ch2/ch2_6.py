scores = [[70,80,90],
               [60,55,70]]#2x3

print(len(scores))
print(len(scores[0]))

print(scores[0])
print(scores[1])
print(scores[0][1])
print(scores[1][0])

for i in range(len(scores)):
    for k in range(len(scores[i])):
        print(scores[i][k],end = " ")
    print()

print()
for v1 in scores:
    for v2 in v1:
        print(v2,end=" ")
    print()     
print()    
