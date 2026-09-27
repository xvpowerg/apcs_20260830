try:
    for i in range(1,6):
        for k in range(1,6):
                print("i:",i,"k:",k,end=" ")
                if i == 3:
                    raise Exception
        print()        
except:
    pass
