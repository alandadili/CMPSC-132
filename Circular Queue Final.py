class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None

class CircularQueue(object):
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    def enqueue(self, x):
        newNode = Node(x)
        newNode.next = None
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        elif self.length < 4:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        else:
            self.tail = (self.tail + 1) % 4
        self.length += 1
    def dequeue(self):
        if self.count == 0:
            print ("The Queue is empty!")
        self.count -= 1
        return self.item.pop()
    def size(self):
        return self.length