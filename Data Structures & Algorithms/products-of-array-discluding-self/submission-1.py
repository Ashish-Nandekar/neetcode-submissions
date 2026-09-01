class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1] * size

        prefix = 1
        for i in range(size):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(size - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res