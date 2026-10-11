class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):

            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
            
        res = []

        for i in seen:
            res.append([seen[i], i])

        res.sort()
        res.reverse()

        # [3,1], [2,2], [1,1]

        final = []

        for i in range(k):
            final.append(res[i][1])
        
        return final


