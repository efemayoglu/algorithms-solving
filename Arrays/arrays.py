# append, pop 

array = []

array.append('a') 
array.append('a')

array.append('b')

print(array)


print(array.count('a')) # O(n)

last = array.pop() #  O(1)

print(last)

print(array)