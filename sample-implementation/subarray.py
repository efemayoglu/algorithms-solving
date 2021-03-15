class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        maxSub, curSum = nums[0], 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

s = Solution()


case1 = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4,-1,-1,30]) == 6


case2 = s.maxSubArray([1]) == 1

case3 = s.maxSubArray([0]) == 0

case4 = s.maxSubArray([-1]) == -1

case5 = s.maxSubArray([-100000]) == -100000


print(case1)
print(case2)
print(case3)
print(case4)
print(case5)