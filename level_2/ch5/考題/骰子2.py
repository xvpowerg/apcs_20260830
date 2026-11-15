class Dice:
    def __init__(self):
        # 順序固定是：上、右、後、前、左、下
        self.faces = [1, 2, 3, 4, 5, 6]

    def up(self):
        # 回傳目前朝上的點數
        return self.faces[0]

    def roll_front(self):
        # 往前滾
        # 舊狀態：[上, 右, 後, 前, 左, 下]
        u, r, back, front, l, d = self.faces

        # 新狀態：[後, 右, 下, 上, 左, 前]
        self.faces = [back, r, d, u, l, front]

    def roll_right(self):
        # 往右滾
        # 舊狀態：[上, 右, 後, 前, 左, 下]
        u, r, back, front, l, d = self.faces

        # 新狀態：[左, 上, 後, 前, 下, 右]
        self.faces = [l, u, back, front, d, r]


n, m = map(int, input().split())

works = []
for _ in range(m):
    works.append(list(map(int, input().split())))

# 建立 n 顆骰子，前面放 None 是為了讓骰子從 1 開始編號
dices = [None] + [Dice() for _ in range(n)]

for a, b in works:
    if b > 0:
        # 交換第 a 顆和第 b 顆骰子
        dices[a], dices[b] = dices[b], dices[a]

    elif b == -1:
        # 第 a 顆骰子往前滾
        dices[a].roll_front()

    elif b == -2:
        # 第 a 顆骰子往右滾
        dices[a].roll_right()

for i in range(1, n + 1):
    print(dices[i].up(), end=' ')