class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None





def nth_to_last_node(n, head):
    leftPointer = head
    rightPointer = head

    for i in range(n-1): # right pointer head move n step 
        rightPointer = rightPointer.next
        if rightPointer == None:
            raise LookupError('there is no node')


    while rightPointer.next != None:
        leftPointer = leftPointer.next
        rightPointer = rightPointer.next


    return leftPointer.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

print(nth_to_last_node(2, a))




