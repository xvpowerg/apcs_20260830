class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def add(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            return
        ptr =  self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newNode
    def getNode(self,index):
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
            if ptr == None:
                break
        return ptr
    def  indexOf(self,value):
        ptr = self.head
        i = 0
        while ptr:
            if ptr.data == value:
                break
            ptr = ptr.next
            i += 1
        else:
            i = -1
        return i
    def insert(self,index,item):
        newNode = Node(item)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            preNode = self.getNode(index-1)
            newNode.next = preNode.next
            preNode.next = newNode
            
import random
link = Linked_list()
for i in range(5):
    link.add(random.randint(1,10))
link.print_list()   
