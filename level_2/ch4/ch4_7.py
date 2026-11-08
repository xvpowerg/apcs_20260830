data=[16,25,39,63,27,12,8,45]
print(data)
n = len(data)
for i in range(1,n):
    for j in range(n-i):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]
    print(data)        
