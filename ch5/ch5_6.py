a,b,c = map(int,input().split())
a = 1 if a != 0 else 0
b = 1 if b != 0 else 0

if (a and b) == c:
    print("AND")
if (a or b) == c:
    print("OR")
if (a ^ b )== c:
    print("XOR")

if (a and b) != c and     (a or b) != c and  (a ^ b) != c:
    print("IMPOSSIBLE")
