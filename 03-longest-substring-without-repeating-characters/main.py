class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        result = ''
        sbstr = []
        sLen = len(s)
        for i in range(sLen):
            for j in range(i,sLen):
                m = s[j]
                if len(result) == 0:
                    result+=m

                elif m not in result:
                    result += m
                else:
                    sbstr.append(result)
                    result = ''
                    break

        if len(sbstr) == 0:
            return len(result)

        a = len(list(sorted(sbstr, key=len)[len(sbstr)-1])) 
        return a if a>= len(result) else len(result)
        