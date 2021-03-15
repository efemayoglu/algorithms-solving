class Stack(object):

	def __init__(self):
		self.items = []

	def add(self, item):
		self.items.append(item)


	def pop(self):
		s = self.items.pop()
		return s

	def isEmpty(self):
		return self.items == []




def balance_check(string):
	if len(string) %2 != 0:
		return False # check if string even 
	s = Stack()
	for i in string:
		if i == '(' or i == '{' or i == '[':
			s.add(i)
		else:
			if s.isEmpty():
				return False

			if i == '}' and s.pop() != '{':
				return False

			elif i ==')' and s.pop() != '(':
				return False 

			elif i == ']' and s.pop() != '[':
				return False

	return True if s.isEmpty() else False

print(balance_check('[](){([[[]]])}' ) == True)



print(balance_check(')(){]}') == False)

print(balance_check('[](){([[[]]])}(') == False)
print(balance_check('[{{{(())}}}]((()))') == True)
print(balance_check('[[[]])]') == False)


print(balance_check('[()]{}{[()()]()}') == True)

print(balance_check('[(])') == False)






# # Balanced Parentheses Check 

# ## Problem Statement

# Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not. 


# You can assume the input string has no spaces.

# ## Solution

# Fill out your solution below: