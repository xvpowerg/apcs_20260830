def gcd_recr(m,n):
    print(f"gcd({m},{n})")
    if n == 0:
        return m
    else:
        return gcd_recr(n,m%n)
n1 = 20
n2 = 14
gcd = gcd_recr(n1,n2)
print(gcd)
