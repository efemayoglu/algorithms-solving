class Solution:
    def findNumbers(self, nums: [int]) -> int:
        counter = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                counter+=1
        return counter
        
s = Solution()
print(s.findNumbers([12,345,2,6,7896]) == 2) 
print(s.findNumbers([555,901,482,1771]) == 1) 




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        # counter = 0
        # for i in range(len(nums)):
            # if int(len(str(nums[i]))) %2 == 0:
                # counter = counter +1

        # return counter

# s = Solution()


# print(s.findNumbers([12,345,2,6,7896]) == 2)
# print(s.findNumbers([555,901,482,1771]) == 1)