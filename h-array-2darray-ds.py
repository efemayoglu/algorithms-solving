import math
import os
import random
import re
import sys

def hourglassSum(arr):

    currenctCol = 0
    currentRow = 0

    isOk = False
    s = 0
    while currentRow+2 <= 6:
        tmp = 0
        if currenctCol +2 >= 6:
            currenctCol = 0
            currentRow += 1
        
        if currentRow +2 >=6:
            break

        
        tmp = arr[currentRow][currenctCol]  + arr[currentRow][currenctCol+1] + arr[currentRow][currenctCol+2] +arr[currentRow+1][currenctCol+1] +arr[currentRow+2][currenctCol] + arr[currentRow+2][currenctCol+1] + arr[currentRow+2][currenctCol+2]

        #s initiliazed with first hourGlass
        if isOk == False:
            s = tmp
            isOk = True

        s = max(s, tmp)

        currenctCol +=1

    return s

#X X 1 
#  1  
#1 1 1 










if __name__ == '__main__':
    fptr = sys.stdout  

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


#question
# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

# Example


# -9 -9 -9  1 1 1 
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
# The  hourglass sums are:

# -63, -34, -9, 12, 
# -10,   0, 28, 23, 
# -27, -11, -2, 10, 
#   9,  17, 25, 18
# The highest hourglass sum is  from the hourglass beginning at row , column :

# 0 4 3
#   1
# 8 6 6
# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

# Function Description

# Complete the function hourglassSum in the editor below.

# hourglassSum has the following parameter(s):

# int arr[6][6]: an array of integers
# Returns

# int: the maximum hourglass sum
# Input Format

# Each of the  lines of inputs  contains  space-separated integers .

# Constraints

# Output Format

# Print the largest (maximum) hourglass sum found in .

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19
# Explanation

#  contains the following hourglasses:

# image

# The hourglass with the maximum sum () is:

# 2 4 4
#   2
# 1 2 4