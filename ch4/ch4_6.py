def f2(x,y,**z):
    if "k1" in z:
        print("做某件事因為有k1")
    print(x,y,z)

f2(1,2)
f2(1,2,k1=3)
f2(1,2,k2=1,k8=9)
