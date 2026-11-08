def josephus(ls,skip):
    idx = skip -1
    while len(ls) > 1:
        print(ls,end="\t")
        print(ls.pop(idx))
        idx = (idx + skip - 1) % len(ls) #idx的位置 必須小於ls長度
    print("survior:",ls[0])   

n = 12
m = 3
list1 = [ i for i in  range(1,n+1)]
josephus(list1,m)
