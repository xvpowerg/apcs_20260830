def test1(x):
    print("Start:",x)
    if x <= 5: #遞迴一定要有結束點
        test1(x + 1)
        print("End:",x)
        
test1(1)
