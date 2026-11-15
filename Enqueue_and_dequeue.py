queue = []

def enqueue(item):
    queue.append(item)
    print(item, "inserted")

def dequeue():
    if len(queue) == 0:
        print("Queue Empty")
    else:
        print(queue.pop(0), "removed")

enqueue(10)
enqueue(20)
enqueue(30)

print(queue)

dequeue()
print(queue)
