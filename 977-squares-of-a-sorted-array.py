class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        for i in range(len(nums)):
            nums[i]*=nums[i]

        nums.sort()
        
        return nums


































s = Solution()

print(s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100])


print(s.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121])
