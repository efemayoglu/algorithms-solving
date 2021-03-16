class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node(1)

b = Node(2)

c = Node(3)


a.next = b


b.next = c



iterator = a
while iterator.next != None:
    print(iterator.value)
    iterator = iterator.next

print (iterator.value)





