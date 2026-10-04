F = int(input())                            #哥哥出拳
N = int(input())                        
y = [int(x) for x in input().split()]
win = {0:5, 2:0, 5:2}                       #5勝0, 0勝2, 2勝5

for i in range(N):
    print(F, end=' ')                       #哥哥本次出拳  
    if(y[i]==F):                            #哥妹平手
        if(i>0 and y[i]==y[i-1]):           #妹兩拳一樣
            F = win[y[i]]                   #哥出可贏妹的拳
        if(i==N-1):                         #最後一拳仍平手,列印平手並跳離
            print(": Drew at round %d" %(i+1))
            break
    elif (F == win[y[i]]):                  #哥出可贏妹的拳
        print(": Won at round %d" %(i+1))   #列印哥勝並跳離
        break
    else:                                   #哥出輸妹的拳
        print(": Lost at round %d" %(i+1))  #列印妹勝並跳離
        break
