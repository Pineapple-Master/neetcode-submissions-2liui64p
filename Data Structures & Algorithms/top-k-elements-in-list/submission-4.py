class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        table = {}
        highestCount = 0
        kCount = k
        answer = []

        sortedList = sorted(nums)


        if len(sortedList) == 0:
            return []
        elif len(sortedList) == 1:
            return sortedList

        count = 0
        for i in range(0, len(sortedList)):
            if i == 0:
                count = count + 1
                continue
            else:
                if sortedList[i-1] == sortedList[i] and i != len(sortedList) - 1:
                    count = count + 1

                elif sortedList[i-1] == sortedList[i] and i == len(sortedList) - 1:
                    count = count + 1
                    if count not in table:
                        table[count] = [sortedList[i]]
                    else: 
                        table[count].append(sortedList[i])

                    if highestCount < count:
                        highestCount = count


                elif sortedList[i-1] != sortedList[i] and i == len(sortedList) - 1:
                    if count not in table:
                        table[count] = [sortedList[i - 1]]
                    else: 
                        table[count].append(sortedList[i - 1])

                    if highestCount < count:
                        highestCount = count

                    count = 1
                    if count not in table:
                        table[count] = [sortedList[i]]
                    else: 
                        table[count].append(sortedList[i])

                    if highestCount < count:
                        highestCount = count

                elif sortedList[i-1] != sortedList[i]:
                    if count not in table:
                        table[count] = [sortedList[i-1]]
                    else: 
                        table[count].append(sortedList[i-1])

                    if highestCount < count:
                        highestCount = count
                    count = 1
        
        print(table)

        while kCount > 0:

            if highestCount in table:
                for element in table[highestCount]:
                    answer.append(element)
                    kCount = kCount - 1
            
            highestCount = highestCount - 1
            if highestCount == 0:
                break;

        return answer

        
        

            

        