class Solution:
    def countMatches(self, items: [[str]], ruleKey: str, ruleValue: str) -> int:
        index = 0
        if ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2

        count = 0
        for i in range(len(items)):
            if items[i][index] == ruleValue:
                count+=1

        return count




s = Solution()


print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color","silver"))
        
print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type","phone"))
