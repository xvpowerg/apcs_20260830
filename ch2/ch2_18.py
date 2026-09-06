num = 6
if  num % 2 == 0:
    print(f"{num}是2的倍數")
    if num%3 == 0:
        print("也是3的倍數")
else:
    if num%3 == 0:
        print(f"{num}是3的倍數")
    else:
        print(f"{num}是2與3的倍數")
    
