#輸入身高 體重 計算bmi
#身高浮點數 公分
#體重是整數
#bmi = 體重 / 身高(公尺) 的平方
#輸出bmi

height = float(input("請輸入身高單位公分:"))
weight = int(input("請輸入體重單位公斤:"))
bmi = weight / (height / 100) ** 2
print(bmi)
print(round(bmi,2) )
