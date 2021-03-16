class Node(object):


    def __init__(self, value):
        self.value = value
        self.next = None


def cycle_check(node):
    iterator = node

    while(iterator.next != None):

        iterator = iterator.next
        if iterator == node:
            return False


    return True 
    




a = Node(1)


b = Node(2)


c = Node(3)


a.next = b

b.next = c

c.next = a


print(a.value == 1)

print(b.value == 2)

print(c.value == 3)

print(a.next.value == 2)

print(a.next.next.value == 3)

print(a.next.next.next.value == 1)


print(a)

print(b)

print(c)

print(c.next)


print('check section: ')

print(cycle_check(a))


c.next = None

print('after fixed: ')
print(cycle_check(a))




