class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        removed_item = self.queue[self.front]
        elif (self.front == self.rear):
            self.front = self.rear = -1
    else:
        self.front = (self.front + 1) % self.size
    return removed_item


def size(self):
    if self.is_empty():
        return 0
    elif self.front <= self.rear:
        return self.rear - self.front + 1
    else:
        return self.size - self.front + self.rear + 1