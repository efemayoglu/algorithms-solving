class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        myDict = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference not in myDict:
                myDict[n] = i    #myDict[5] = 0   myDict[8] = 1
            else:
                return [myDict[difference], i]
        return []





s = Solution()



print(s.twoSum([2,7,11,15] , 9))
print(s.twoSum([3,2,4] , 6))
print(s.twoSum([3,3] , 6))

case1= s.twoSum([2,7,11,15] , 9) == [0,1]
case2= s.twoSum([3,2,4] , 6) == [1,2]
case3= s.twoSum([3,3] , 6) == [0,1]

print(case1)
print(case2)
print(case3)