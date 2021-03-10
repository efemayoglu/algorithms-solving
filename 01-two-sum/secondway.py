class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        mySet = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in mySet:
                mySet[nums[i]] = i
            else:
                return [mySet[complement], i ]

        return []



s = Solution()


case1= s.twoSum([2,7,11,15] , 9) == [0,1]
case2= s.twoSum([3,2,4] , 6) == [1,2]
case3= s.twoSum([3,3] , 6) == [0,1]

print(case1)
print(case2)
print(case3)