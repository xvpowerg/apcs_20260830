k = int(input())
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())

i = 0
while k > 0:
    i += k
    if i % x1 == 0:
        k -= y1
    if  i % x2 == 0:
        k -= y2
print(i)        
