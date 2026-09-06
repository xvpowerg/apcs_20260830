# 檢查使用者輸入的字串是否為迴文
#是顯示True 不是顯示Fasle
#迴文ABA 不是迴文 ABC
txt  = input("請輸入文字")
print(txt == txt[::-1])

