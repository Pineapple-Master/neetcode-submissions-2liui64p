class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ledger = set()
        left = 0;
        right = 0;
        maxLength = 0;

        for i in range (0, len(s)):
           
            while s[i] in ledger:

                ledger.remove(s[left])
                left = left + 1
            
            right = right + 1
            ledger.add(s[i])
            maxLength = max(maxLength, right - left)
        
        return maxLength



