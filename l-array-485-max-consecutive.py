class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        count = 1 if nums[0] == 1 else 0
        result = 0
        for i,n in enumerate(nums):
            if i == 0:
                continue
            if n == 1:
                count+=1
            else:
                result = max(result, count)
                count = 0

        return max(result, count)
        

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3)



























#         key = 1
#         counter = 0
#         counterTemp = 0
#         for i in range(0,len(nums)):
#             if nums[i] != key:
#                 if counterTemp >= counter:
#                     counter = counterTemp
#                     counterTemp = 0
#                 else:
#                     counterTemp = 0
#             else:
#                 counterTemp = counterTemp+1
        
#         if counterTemp>counter:
#             counter = counterTemp
        
#         return counter

# s = Solution()
 