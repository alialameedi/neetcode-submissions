class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # make a map to get the freq of each item
        count = {}

        # easy way to create an array within the array for each frequency category
        freq = [[] for i in range(len(nums) + 1)]

        # actually store the freq -- NUMBER : FREQUENCY
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Look through the frequency dictionary and append it to the freq position
        for num, cnt in count.items():
            freq[cnt].append(num)


        res = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

        

