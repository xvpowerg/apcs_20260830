class Queue:
    def __init__(self):
        self.my_queue = []
    def enqueue(self,data):
        self.my_queue.append(data)
    def dequeue(self):
        return self.my_queue.pop(0)
    def size(self):
        return len(self.my_queue)
    def isEmpty(self):
        return self.my_queue == []
quque = Queue()

people = ["Amy","David","Sean"]

for person in people:
    quque.enqueue(person)
    
while not quque.isEmpty():
    print(quque.dequeue())
