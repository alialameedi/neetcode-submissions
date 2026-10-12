class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # each index is the freq, the numbers r in the array
        bucket = [[] for _ in range(len(nums) + 1)]
        seen = {}

        for i, num in enumerate(nums):
            seen[num] = seen.get(num, 0) + 1

        # number to freq
        for i in seen:
            bucket[seen[i]].append(i)
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):

            for j in bucket[i]:

                if len(res) < k:
                    res.append(j)
        
        return res
        



        


