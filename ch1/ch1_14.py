msg1 = "這是"
name = "小民"
msg2 = "的成績是"
score = 100
msg3 = "身高是"
height = 172.56
msg = msg1 + name+msg2+str(score)

# %d(表示整數) %s(表示字串) %f(表示浮點數)
msg = "這是%s的成績是%d身高是%.2f"%(name,score,height)
print(msg)
msg = "這是{}的成績是{}身高是{}".format(name,score,height)
print(msg)
msg = "這是{name}的成績是{score}身高是{height}".format(name = name,score=score,height=height)
print(msg)
msg = f"這是{name}的成績是{score}身高是{height}"
print(msg)
