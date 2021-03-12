class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        total = nums[0]#-2
        total2 = nums[0]
        for i in range(1, len(nums),1): #-1,  
            if total < 0:
                total = 0
            total += nums[i]
            total2 = max(total , total2)
        return total2


# i = 1 => nums[1] =  1, total = 1
# i = 2 => nums[2] = -3, total = 0
# i = 3 => nums[3] =  4, total = 4
# i = 4 => nums[4] = -1, total = 3
# i = 5 => nums[5] =  2, total = 5
# i = 6 => nums[6] =  1, total = 0
# i = 7 => nums[7] = -5, total = 0
# i = 8 => nums[8] =  4, total = 0



s = Solution()

case1 = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
case2 = s.maxSubArray([1])
case3 = s.maxSubArray([0])
case4 = s.maxSubArray([-1])
case5 = s.maxSubArray([-100000])

print(case1 == 6)
print(case2 == 1)
print(case3 == 0)
print(case4 == -1)
print(case5 == -100000)
