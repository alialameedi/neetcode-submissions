class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            seeking = target - nums[i]

            if seeking in seen:
                return [seen[seeking], i]
            else:
                seen[nums[i]] = i

        
        