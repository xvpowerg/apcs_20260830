num1 = 10
num2 = 1
nums = [1,3,5,7,9]

try:
    print("開始")
    ans = 0
    ans = num1 / num2
    print(nums[1])
except ZeroDivisionError:
    print("產生例外 分母不可為0")
except IndexError:
    print("索引發生錯誤")
else:
    print("沒有發生Error")
print("完成:",ans)
