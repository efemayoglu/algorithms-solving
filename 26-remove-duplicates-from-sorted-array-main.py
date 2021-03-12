class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        count = 0
        founded = 0
        for i in range(1, len(nums), 1):
            if nums[count] != nums[i]:
                founded = founded+1
            count = count + 1

        return founded+1



s = Solution()

print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
