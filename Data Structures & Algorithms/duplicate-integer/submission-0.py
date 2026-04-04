class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newMap = {}
        for index, value in enumerate(nums):
            if value in newMap: #key exists in hastable
                return True
            else:
                newMap[value] = index
        return False