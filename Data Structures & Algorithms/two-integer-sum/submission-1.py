class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        if len(nums) == 0:
            return []

        for i in range (0, len(nums)):
            currNum = nums[i]
            searchNum = target - currNum
            if searchNum in table:
                if i > table[searchNum]:
                    return [table[searchNum], i]
                else:
                    return [i, table[searchNum]]
                
                
            else:
                table[currNum] = i

            