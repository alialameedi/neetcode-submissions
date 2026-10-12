class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        heap = []

        # Number:Frequency
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
                
        # Number:Frequency
        for i in seen:
            heapq.heappush(heap, [seen[i], i])

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for i in heap:
            res.append(i[1])

        return res


        


