class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        s = []
        for i in self.items:
            s.append(f'item ={i}\n')
            
        return ''.join(s)

d = Deque()

d.addFront(5)

d.addRear(10)

d.addFront(20)

d.addRear(50)

d.addFront(200)


d.addFront(200)

d.addRear(10)
d.addRear(11)

d.removeFront()
d.removeFront()
d.removeFront()

d.removeRear()
d.removeRear()
d.removeRear()


print(d)



print(d.size())

