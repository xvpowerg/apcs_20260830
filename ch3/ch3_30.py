scores = {"Ch":100,"En":80,"Ma":95}
add_dic = {"Ch":92,"En":77,"OS":86}
scores.update(add_dic)
print(scores)
ans1 = scores.get("LA","Empty")
ans2 = scores.get("En","Empty")
print(ans1)
print(ans2)
