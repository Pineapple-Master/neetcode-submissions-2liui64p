class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        wordOne = {}
        wordTwo = {}

        for i in s:
            if i in wordOne:
                wordOne[i] = wordOne[i] + 1
            else:
                wordOne[i] = 1
    
        for i in t:
            if i in wordOne:
                wordOne[i] = wordOne[i] - 1
                if wordOne[i] < 0:
                    return False
            else:
                return False
        
        for key in wordOne:
            if wordOne[key] != 0:
                return False

        return True


        