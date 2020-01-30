class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        lastRepeat = 0
        hashTable = {}
        for x in range(len(s)):
            if s[x] in hashTable:
                if hashTable[s[x]] >= lastRepeat:
                    lastRepeat = hashTable[s[x]] + 1
                else:
                    del hashTable[s[x]]
            hashTable[s[x]] = x
            maxLength = max(maxLength, x - lastRepeat + 1)
        return maxLength
            
