class Stack:
    def __init__(self,capacity):
        self.my_stack = [None] * capacity
        self.top = -1
        self.capacity = capacity
    def push(self,data):
           if self.isFull():
               print("滿了")
           else:
              self.top += 1
              self.my_stack[self.top] = data
    def size(self):
        return self.top + 1

    def pop(self):
        if self.isEmpty():
            print("堆疊為空")
            return None
        data = self.my_stack[self.top]
        self.my_stack[self.top] = None
        self.top -= 1
        return data
        

    def isEmpty(self):
        return self.size() == 0
    
    def isFull(self):
        if self.size() >= self.capacity:
            return True
        else:
            return False
        
stack = Stack(3)

stack.push("A")
stack.push("B")
stack.push("C")
print(stack.isFull())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
