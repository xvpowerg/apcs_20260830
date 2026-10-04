n = int(input())
antuRule = []
for _ in range(n):
    s1 = list(map(int, input().split()))    #上聯
    s2 = list(map(int, input().split()))    #下聯
    if (s1[1] == s1[3]) | (s1[1] != s1[5]) |(s2[1] == s2[3])|(s2[1] != s2[5]):
        antuRule.append("A")
    if (s1[6] != 1) | (s2[6] != 0):
        antuRule.append("B")
    if (s1[1] == s2[1]) |   (s1[3] == s2[3]) | (s1[5] == s2[5]) :
        antuRule.append("C")
    print("".join(antuRule)) if antuRule != [] else print("None")
    antuRule = []
