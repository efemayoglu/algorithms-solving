class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        a = {}

        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        
        s = 0
        for i in a.keys():
            s += ( self.calculator( a[i] ))

        return s

    def calculator(self, n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 3
        
        return (n-1) + self.calculator(n-1)



s = Solution()

print(s.numIdenticalPairs([1,2,3,1,1,3]) == 4)

print(s.numIdenticalPairs([1,1,1,1]) ==6)

print(s.numIdenticalPairs([1,2,3])==0)









# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100