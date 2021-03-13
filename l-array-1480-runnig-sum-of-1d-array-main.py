class Solution:
    def runningSum(self, nums: [int]) -> [int]:
        for i in range(len(nums)):
            if i != 0:
                nums[i] = nums[i] + nums[i-1]
        return nums


s = Solution()

print(s.runningSum([3,1,2,10,1]) == [3,4,6,16,17])
print(s.runningSum([1,1,1,1,1]) == [1,2,3,4,5])
print(s.runningSum([1,2,3,4]) == [1,3,6,10])
