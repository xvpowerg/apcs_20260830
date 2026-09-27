def testScore(s):
    #必須0~100之間 說明及格或不及格
    #不在0~100之間顯示錯誤的成績
    if s < 0  or  s > 100:
        raise OverflowError("錯誤的成績")
    elif s  < 60:
          print("不及格")
    else:
         print("及格")
         
testScore(85)
testScore(50)
testScore(-25)
