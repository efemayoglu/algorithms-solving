class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head):
    current = head
    prevNode = None
    nextNode = None

    while current:
        nextNode = current.next # backup
        current.next = prevNode # reversing
        prevNode = current # prev = current
        
        current = nextNode

    

a = Node(1)        

b = Node(2)

c = Node(3)

d = Node(4)


a.next = b
b.next = c
c.next = d

iterator = a

while iterator:
    print(iterator.value)
    iterator = iterator.next


print('-----------')

print(d.next.value)
print(c.next.value)
print(b.next.value)

print('------------')

    


