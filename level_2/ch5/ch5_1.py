def myLog(a,b,pre=2):
    step = 1
    ans = step
    while step >= 10 **-pre:
        while b ** ans < a:
            ans += step
            if b ** ans == a:
                return ans
        ans -= step
        step /= 10
    return ans
    
a = 25#數值
b = 2#底數
print(f"{a}以{b}為底的log為:{myLog(a,b):.2f}")

