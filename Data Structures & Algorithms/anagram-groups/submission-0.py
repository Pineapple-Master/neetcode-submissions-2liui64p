class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}

        for word in strs:
            sortedWord = str(sorted(word))

            if sortedWord in map:
                map[sortedWord].append(word)
            else:
                map[sortedWord] = [word]
        
        answer = []

        for key in map:
            answer.append(map[key])
            
        return answer
            
       
        