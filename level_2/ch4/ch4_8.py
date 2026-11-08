data=[16,25,39,63,27,12,8,45]
print(data)
n  = len(data)
for i in range(n-1):
    minIndx = i
    for j in range(i+1,n):
        if data[j] < data[minIndx]:
            minIndx = j
    data[i],data[minIndx] = data[minIndx],data[i]
    print(data)
