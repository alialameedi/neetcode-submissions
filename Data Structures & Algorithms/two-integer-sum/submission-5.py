class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        arr = []

        for i, num in enumerate(nums):
            arr.append([num, i])
        
        arr.sort()
        # [[2, 1], [3, 0], [3, 2]]

        i, j = 0, len(arr) - 1

        while i < j:

            if arr[i][0] + arr[j][0] == target:
                return [min(arr[i][1], arr[j][1]),
                        max(arr[i][1], arr[j][1])]
            
            if (arr[i][0] + arr[j][0] > target):
                j -= 1
            else:
                i += 1
        



        