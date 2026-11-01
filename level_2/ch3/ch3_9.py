class Queue:
    def __init__(self,capacity):
        self.queue = []
        self.capacity = capacity
    def isEmpty(self):
        return len(self.queue) == 0
    def isFull(self):
        return len(self.queue) == self.capacity
    def enqueue(self,data):
        if self.isFull():
            print("已滿")
            return
        self.queue.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("為空")
            return None
        return self.queue.pop(0)
queue = Queue(3)
people = ['Amy', 'David', 'Sean', 'Nicole']
for p in people:
    queue.enqueue(p)

for i in range(4):
    print(queue.dequeue())
