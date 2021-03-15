class Stack(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[self.size() -1]

	def size(self):
		return len(self.items)



#remmina rdp

s = Stack()


print(s.isEmpty() == True)

s.push('test')

print(s.peek() == 'test')

print(s.pop() == 'test')


s.push('hey')

s.push('bro')

s.push('how are you?')


print(s.size() == 3)

print(s.pop() == 'how are you?')

print(s.peek() == 'bro')





 	
	

	   




# Implement a Stack¶
# A very common interview question is to begin by just implementing a Stack! Try your best to implement your own stack!

# It should have the methods:

# Check if its empty
# Push a new item
# Pop an item
# Peek at the top item
# Return the size
