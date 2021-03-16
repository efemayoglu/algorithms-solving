class NodeSingly(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList(object):
    
    def __init__(self, head):
        self.head = head


    def append(self, val):
        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next

        iterator.next = NodeSingly(val)

    def prepend(self, val):
        n = NodeSingly(val)
        n.next = self.head
        
        self.head = n

    def removeAt0(self):
        self.head = self.head.next

    def __str__(self):
        vals = []
        iterator =self.head
        while iterator != None:
            vals.append(str(iterator.val))
            iterator = iterator.next
        
        return ','.join(vals)


a = NodeSingly(1)
b = NodeSingly(2)
c = NodeSingly(3)

a.next = b
b.next =c

s = SinglyLinkedList(a)
print(s)
s.append(20)
print(s)
s.removeAt0()
print(s)
s.removeAt0()

print(s)

