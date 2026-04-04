class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hMap = {}

        

        for i in range (0, len(s)):

            if s[i] in hMap:
                hMap[s[i]] += 1
            else:
                hMap[s[i]] = 1
        
        for i in range (0, len(t)):

            if t[i] in hMap and hMap[t[i]] == 1:
                hMap.pop(t[i])
            elif t[i] in hMap:
                hMap[t[i]] -= 1
            else:
                return False

        if len(hMap) == 0:
            return True
        else: 
            return False







        