class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        maximum = sum(accounts[0])
        for i in range(1, len(accounts), 1):
            if sum(accounts[i]) > maximum:
                maximum = sum(accounts[i])
        return maximum


s = Solution()


print(s.maximumWealth([[1,2,3],[3,2,1]]) == 6)
print(s.maximumWealth([[1,5],[7,3],[3,5]]) == 10)
print(s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])== 17)
