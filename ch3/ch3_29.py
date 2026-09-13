scores = {"Ch":100,"En":80,"Ma":95}
print(scores)
print(scores["En"])
for k in scores:
    print(k,scores[k])

    
scores["Ma"] = 92 #Key存在更新
print(scores)
scores["AS"] = 99#Key不存在新增
print(scores)
myKey = "LA"
if myKey in  scores:
    print(scores[myKey])#KeyError
