# def finder(arr1, arr2):
#     arr1.sort()
#     arr2.sort()

#     for i in range(len(arr1)):
#         if arr1[i] != arr2[i]:
#             return arr1[i]

#     return -1


# def finder(arr1, arr2):
#     arr1.sort()
#     arr2.sort()

#     for num1, num2 in zip(arr1, arr2):
#         if num1 != num2:
#             return num1

#     return arr2[-1]


def finder(arr1, arr2):
    a = {}
    for i in arr1:
        if i not in a:
            a[i] = 1
        else:
            a[i] = a[i] + 1
  
    for i in arr2:
        if i not in a:
            return i
        else:
            a[i] = a[i] -1
    print(a)
    for i in a.keys():
        print(f'i = {i}, a[{i}]= {a[i]}')
        if a[i] !=0:
            return i
    return  -1

print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
print(finder([5,5,7,7], [5,7,7]))













# Find the Missing Element
# Problem
# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

# Input:

# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output:

# 5 is the missing number
# Solution¶
# Fill out your solution below:

# def finder(arr1,arr2):
    
#     pass
# arr1 = [1,2,3,4,5,6,7]
# arr2 = [3,7,2,1,4,6]
# finder(arr1,arr2)
# 5
# arr1 = [5,5,7,7]
# arr2 = [5,7,7]
# ​
# finder(arr1,arr2)
# 5