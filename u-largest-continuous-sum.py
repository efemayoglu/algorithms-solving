#modern solution
# def large_cont_sum(arr):
#     if len(arr) == 0:
#         return 0

#     max_sum = current_sum = arr[0]

#     for num in arr[1:]:

#         current_sum = max(current_sum+num, num)

#         max_sum = max(max_sum, current_sum)

#     return max_sum       


# print( large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))


#my naive solution
def large_cont_sum(arr): 
    s = arr[0]
    temp  = 0 
    for i in arr:
        temp += i
        if temp < 0:
            temp = 0
        s = max(s, temp)
    return s 

#Largest Continuous Sum
#Problem
#Given an array of integers (positive and negative) find the largest continuous sum.
#
#Solution
#Fill out your solution below: