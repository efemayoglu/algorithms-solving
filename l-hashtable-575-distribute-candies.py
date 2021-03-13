class Solution:
    def distributeCandies(self, candyType: [int]) -> int:
        candyType.sort()
        counter = 1
        lenOfCandyType = len(candyType)/2
        for i in range(1,len(candyType)):
            if candyType[i] != candyType[i-1]:
                counter+= 1

            if counter>= lenOfCandyType:
                break
        
        return min(counter, lenOfCandyType)
























    #     candies = len(candyType)
    #     canEat = int(candies // 2)
    #     types = self.findDistinctType(candyType)
    #     return types if types < canEat else canEat

    # def findDistinctType(self, candyType):
    #     result = set()
    #     for i in candyType:
    #         if i not in result:
    #             result.add(i)
    #     return len(result)




s = Solution()
case1 = s.distributeCandies([1,1,2,2,3,3]) == 3
case2 = s.distributeCandies([1,1,2,3]) == 2
case3 = s.distributeCandies([6,6,6,6]) == 1


print(f"case1: {case1}")
print(f"case2: {case2}")
print(f"case3: {case3}")