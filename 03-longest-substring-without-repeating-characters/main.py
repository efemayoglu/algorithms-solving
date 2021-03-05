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


                       
        #queue = collections.deque([])        
        #window = set()
        #result = 0
        #
        #for c in s:            
        #    if c in window:
        #        while queue:
        #            prev = queue.popleft()
        #            window.remove(prev)
        #            if prev == c:
        #                break
        #                    
        #    queue.append(c)
        #    window.add(c)
        #    result = max(result, len(window))
        #    
        #return result
        