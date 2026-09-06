num = int(input("輸入整數"))

isP = True
for i in range(2,num):
    if num % i == 0:
        isP = False
        break
if isP:
    print(num,"是質數")
else:
    print(num,"不是質數")
