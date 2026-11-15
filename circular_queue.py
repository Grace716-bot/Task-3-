class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
            return None

        item = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return item

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

q = CircularQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
