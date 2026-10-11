class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        seen = {}

        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        for i in seen:
            heapq.heappush(heap, [seen[i], i])
        
        while len(heap) > k:
            heapq.heappop(heap)

        final_arr = []

        for i in heap:
            final_arr.append(i[1])

        return final_arr


        

