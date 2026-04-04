class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        map = {}
        answer = []
        
        for i in range(0, len(nums)):

            if (target - nums[i]) in map:
                answer = [map[target - nums[i]], i]
                break
            
            map[nums[i]] = i

        return answer




            
            