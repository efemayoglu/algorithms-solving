class Solution:
    def twoSum(self, nums, target):
        arr = set() # used set because i want to store only unique index
        for i,n in enumerate(nums): # used enumerate due to index=i and value=n
            for j,m in enumerate(nums): # used enumerate due to index=j and value=k
                if i != j: # check if i and j is not the same index 
                    if n+m  == target: # if n + m equals to target 
                        arr.add(i)          # then add i 
                        arr.add(j)          # then add j into the set which i defined on the top
        return arr  # return my set

a = Solution()

print(a.twoSum([3,2,4], 6))
         
for i,n in enumerate([3,2,4]):
    print(f"i={i}, n={n}")

