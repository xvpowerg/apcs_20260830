from collections import deque
q = deque([1,2,3,4,5])
q.append(6)
print(q)
q.rotate(2)
print(q)
q.rotate(-3)
print(q)
first = q.popleft()#彈出第一筆
print(first)
print(q)
right = q.pop()#彈出最後一筆
print(right)
print(q)
q.insert(0,10)
print(q)
