def square_root(x,pre=2):
    step = 1
    r = step
    while step >= 10 ** -pre:
        while r*r < x:
            r += step
            if  r*r == x:
                return r
        r -= step
        step/=10
    return r    

print(f"{square_root(8):.2f}")
