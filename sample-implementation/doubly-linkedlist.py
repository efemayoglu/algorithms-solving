class DoublyLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None



a = DoublyLinkedList(5)


b = DoublyLinkedList(1)


c = DoublyLinkedList(2)


a.next =  b
b.prev = a

b.next = c
c.prev= b

iterator = a


print('next section:')

while iterator.next!= None:
    print(iterator.value)
    iterator = iterator.next

print(iterator.value)


print('previous section:')

while iterator.prev != None:
    print(iterator.value)
    iterator = iterator.prev

print(iterator.value)





