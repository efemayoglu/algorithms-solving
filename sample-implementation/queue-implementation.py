class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()


print(q.isEmpty())
q.enqueue('hey')
print(q.isEmpty())

q.enqueue('dd')

print(q.dequeue())
print(q.dequeue())



#Queue() creates a new queue

#enqueue(item) adds a new item

#dequeue() removes the front item from the queue

#isEmpty() tests to see thetther the queue is empty

#size returns the number of items in the queue
