class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        maximum = candies[0]
        for i in range(len(candies)):
            if candies[i] > maximum:
                maximum = candies[i]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                candies[i] = True
            else:
                candies[i] = False
        return candies

s = Solution()

print(s.kidsWithCandies([2,3,5,1,3], 3))
print(s.kidsWithCandies([4,2,1,1,2], 1))
print(s.kidsWithCandies([12,1,12], 10))
