class Solution:
    def shuffle(self, nums: [int], n: int) -> [int]:
        a = []
        index = 0

        while index < n:
            a.append(nums[index])
            a.append(nums[ n + index ])
            index +=1
        return a

s = Solution()

print(s.shuffle([1,2,3,4,4,3,2,1], 4) == [1,4,2,3,3,2,4,1])
print(s.shuffle([1,1,2,2], 2) == [1,2,1,2])
print(s.shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7] )