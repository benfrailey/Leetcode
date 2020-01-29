class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charList = []
        longest = 0
        test = 0
        x = 0
        while x < len(s):
            if not charList:
                start = x + 1
            char = s[x]

            if char in charList:
                charList.clear()
                x = start
                if longest < test:
                    longest = test
                test = 0
                continue

            else:
                test = test + 1
                charList.append(char)
                x = x+1



        else:
            if longest < test:
                longest = test
            return longest

            
