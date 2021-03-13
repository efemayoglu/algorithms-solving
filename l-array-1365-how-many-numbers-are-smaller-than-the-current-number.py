class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        s = sorted(nums)     #1,2,2,3,8
        index = len(s) - 1   #4
        lastVal = s[index]   #8
        a={}                 #{}

        while index  >= 0:
            
            if s[index] not in a:
                a[
                    s[index]
                ] = 0

            if s[index] != lastVal:   #index=4, s[4] = 8, lastVal = 8
                                      #index=3, s[3] = 3, lastVal = 8
                a[                    #a[8] = 3 + 1
                    lastVal           #lastVal = s[3] => 3
                ] = index + 1

                lastVal = s[index]

            index-=1

        
        b = []
        for i in nums:
            b.append(a[i])


        return b



s = Solution()


print(s.smallerNumbersThanCurrent([8,1,2,2,3]))


print(s.smallerNumbersThanCurrent([6,5,4,8]))
print(s.smallerNumbersThanCurrent([7,7,7,7]))
