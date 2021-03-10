class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[lastNonZeroFoundAt] = nums[lastNonZeroFoundAt], nums[i]
                lastNonZeroFoundAt = lastNonZeroFoundAt+1

        print(nums)
        # iterator1 = 0
        # iterator2 = len(nums) -1

        # while i < len(nums) -2:
        #     if nums[i] == 0:
        #         temp = nums[i+1]
        #         nums[i+1] = temp
        #         nums[i] = 0 







    # def moveZeroes(self, nums: [int]) -> None:
    #     lastIndex = len(nums) -1 
    #     i = 0
    #     while i <  int (len(nums) / 2) + 1:
    #         if nums[i] == 0:
    #             if nums[lastIndex] != 0:
    #                 temp = nums[lastIndex]
    #                 nums[lastIndex] = 0
    #                 nums[i] = temp
    #                 lastIndex = lastIndex -1
    #             else:
    #                 lastIndex = lastIndex - 1
    #                 i = i - 1
    #         i = i + 1
    #     print(nums)

s = Solution()

s.moveZeroes([0,1,0,3,12,0,34,0,123,234,])
            