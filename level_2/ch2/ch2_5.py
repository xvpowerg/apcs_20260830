#遞增陣列
#1 2 3 9 11
num = input("輸入整數")
num = map(int,num.split())
arr = list(num)
for j  in range(len(arr) - 1):
    if arr[j] >= arr[j+1]:
        print("不是遞增陣列")
        break
else:
    print("遞增陣列")
    
        
