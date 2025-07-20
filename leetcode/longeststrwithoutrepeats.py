class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        possible = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                possible.append(s[i:j])

        for i in possible:
            #return max(possible, key=len)
            if len(i) == len(set(i)): #and above:
                pass

    
c = Solution()
print(c.lengthOfLongestSubstring("pwwkew"))
