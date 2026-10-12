class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product, zeroes = 1, 0

        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num
            
            if zeroes > 1:
                return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, num in enumerate(nums):

            if num == 0:
                res = [0] * len(nums)
                res[i] = product
                return res

            else:
                res[i] = product // num
        
        return res

        

        