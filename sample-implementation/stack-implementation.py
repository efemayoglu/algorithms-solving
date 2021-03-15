class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []# check if the list is empty then return 

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()#remove last index

    def peek(self):
        return self.items[len(self.items) - 1]#return last item in items

    def size(self):
        return len(self.items)


s = Stack()

print(s.isEmpty() == True)

s.push(1)
s.push('two')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty() == False)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty() == True)


# def Stack():#creates a new stack that is empty
#     pass

# def push(item):#adds a new item to the top of the stack
#     pass

# def pop():#removes the top item from the stack
#     pass

# def peek():#return the top item from the stack but does not remove.
#     pass

# def isEmpty():#tests to see whether the stack is empty
#     pass

# def size():#returns the number of items on the stack
#     pass