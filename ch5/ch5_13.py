n = int(input())                    #圍籬寬度n
h = list(map(int, input().split())) #各圍籬高度
cost = 0
for i in range(n):
    if h[i] == 0:                   #圍籬被吹斷
        if i == 0 :                 #左邊界
            cost += h[1]            #修補成本為h[1]
        elif i == n-1 :             #右邊界
            cost += h[n-2]          #修補成本為h[n-2]
        else:                       #非左右邊界
            if h[i-1] >= h[i+1]:    #以左右圍籬高度較小的為成本
                cost += h[i+1]
            else:
                cost += h[i-1]
print(cost)                         #列印成本
