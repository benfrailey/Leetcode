class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 1
        index = 0
        for i in range(len(s)):
            x = 0
            char = s[i]
            while i-x >= 0 and i+x < len(s) and s[i-x] == s[i+x]:
                if x == 0:
                    length = 1
                else:
                    length = length + 2
                x = x + 1
                if maxLength < length:
                    maxLength = length
                    index = i - x + 1

            x = 0

            while i+1+x < len(s) and i+1 < len(s) and i-x >= 0 and s[i] == s[i+1] and s[i-x] == s[i+1+x]:
                if x == 0:
                    length = 2
                else:
                    length = length + 2
                x = x + 1
                if maxLength < length:
                    maxLength = length
                    index = i - x + 1
        return s[index:index + maxLength]
                
