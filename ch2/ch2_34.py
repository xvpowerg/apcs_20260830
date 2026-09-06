results = ["Ken","Lucy","Joy"]
count = [0,0,0]
for i in range(5):
    vote = input("投票給:")
    if vote not in results:
        print("無效票")
        continue
    for i in range(len(results)):
        if results[i] == vote:
            count[i]+= 1

for v1 in results:
    print(v1,end="\t")
print()
for c in count:
    print(c,end="\t")
