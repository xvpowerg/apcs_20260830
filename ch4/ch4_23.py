import random
start,end = 1,100
answer = random.randint(start,end)
guess = int(input(f"猜一個{start}~{end}的整數"))
count = 1
print(answer)
while count < 5:
        if guess == answer:
            print("答對了")
            break
        elif guess > answer:
            end = guess - 1
        else:
            start = guess + 1
        count += 1
        guess = int(input(f"猜一個{start}~{end}的整數"))
else:
    print(f"答案是:{answer}")
    
