# 讀入 k
# k 代表：每一段大寫或小寫，長度都要剛好是 k
# 例如 k = 2，代表可以是：小寫2個、大寫2個、小寫2個...
k = int(input())

# 讀入原始字串
# 例如：aBBdaaa
a = input()

# uorl = Upper Or Lower List
# 用 0 / 1 記錄每個字元是大寫還是小寫
# 0 代表大寫
# 1 代表小寫
uorl = []

# 將每個字母轉成 0 或 1
for c in a:
    if c >= 'A' and c <= 'Z':
        # 如果是大寫字母，就記成 0
        uorl.append(0)

    elif c >= 'a' and c <= 'z':
        # 如果是小寫字母，就記成 1
        uorl.append(1)


# seg 用來記錄「連續同類型字母的長度」
# 例如：
# aBBdaaa
# 轉成 uorl 後是：
# 1 0 0 1 1 1 1
#
# 分段來看：
# a       -> 小寫 1 個
# BB      -> 大寫 2 個
# daaa    -> 小寫 4 個
#
# 所以 seg = [1, 2, 4]
seg = []

# my_len 代表目前這一段連續字母的長度
# 一開始至少會有第一個字元，所以先設為 1
my_len = 1

# 從第 1 個位置開始檢查
# 因為第 0 個字元沒有前一個可以比
for i in range(1, len(uorl)):

    if uorl[i] == uorl[i - 1]:
        # 如果現在這個字元，和前一個字元類型一樣
        # 例如都是小寫，或都是大寫
        # 代表還在同一段裡面，所以長度 +1
        my_len += 1

    else:
        # 如果現在這個字元，和前一個字元類型不同
        # 代表上一段結束了
        # 先把上一段的長度存進 seg
        seg.append(my_len)

        # 重新開始計算新的一段
        my_len = 1

# 迴圈結束後，最後一段還沒放進 seg
# 所以要補放一次
seg.append(my_len)


# longest 記錄目前找到的最長 k-交錯字串長度
longest = 0

# m 是總共有幾段連續大小寫區段
m = len(seg)

# le 是左指標，用來找一段長度剛好等於 k 的區段
le = 0

while le < m:

    # 先找到第一個「長度剛好是 k」的區段
    # 因為 k-交錯字串，中間完整的每一段都要剛好等於 k
    while le < m and seg[le] != k:
        le += 1

    # 如果已經超出範圍，代表後面都找不到長度 k 的區段
    if le >= m:
        break

    # ri 從 le 的下一段開始找
    # 目標是找出一整串連續都是 k 的區段
    ri = le + 1

    # 只要右邊這段也是 k，就繼續往右擴張
    while ri < m and seg[ri] == k:
        ri += 1

    # 現在 [le, ri) 這一段範圍內，全部都是長度 k 的區段
    #
    # 例如：
    # seg = [3, 2, 2, 2, 5]
    # k = 2
    #
    # 中間連續 k 區段是：
    # [2, 2, 2]
    #
    # 長度就是：
    # 3 段 * k
    t = (ri - le) * k

    # 左邊如果有一段長度大於 k
    # 可以從那一段切出 k 個字元，接到目前答案左邊
    #
    # 注意：
    # 如果左邊長度是 5，k = 2
    # 不是整段 5 都拿進來
    # 只能拿其中 k = 2 個
    if le > 0 and seg[le - 1] > k:
        t += k

    # 右邊如果有一段長度大於 k
    # 也可以從那一段切出 k 個字元，接到目前答案右邊
    if ri < m and seg[ri] > k:
        t += k

    # 更新目前找到的最大長度
    if t > longest:
        longest = t

    # ri 目前停在第一個「不是 k」的位置
    # 這一段本身不能當作中間完整的 k 區段
    # 所以下一輪從 ri + 1 繼續找
    le = ri + 1


# 輸出最長 k-交錯字串長度
# 如果完全找不到，longest 會維持 0
print(longest)