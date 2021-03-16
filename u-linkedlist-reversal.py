class Node(object):

    def __init__(self, value):

        self.value = value
        self.next = None

    

def reverse(head):
    s = []

    iterator = head
    while iterator.next != None:
        s.append(iterator.value)
        iterator = iterator.next

    s.append(iterator.value)

    newNode = Node(s.pop())

    head = newNode

    for i in range(len(s)):
        newNode.next = Node(s.pop())
        newNode = newNode.next
    
    return head

a = Node(1)

b = Node(2)

c = Node(3)

d = Node(4)



a.next = b

b.next = c

c.next = d


iterator = a


print('before:reversed')


while iterator.next != None:
    print(iterator.value)
    iterator = iterator.next

print(iterator.value)



a = reverse(a)

print('after reversed:')


while a.next != None:
    print(a.value)
    a =a.next
print(a.value)








