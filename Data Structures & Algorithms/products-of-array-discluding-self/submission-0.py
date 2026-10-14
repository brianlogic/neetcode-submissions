class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [48 24 6 1] suffix, except itself
        # [1 1 2 8]prefix, except itself

        suffix = [0] * len(nums)
        prefix = [0] * len(nums)

        # create suffix
        for i in range(len(nums) - 1, -1, -1): 
            if i == len(nums) - 1: 
                suffix[i] = 1
            else:
                suffix[i] = nums[i + 1] * suffix[i + 1]
            
        # create prefix
        for i in range(len(nums)): 
            if i == 0: 
                prefix[i] = 1
            else:
                prefix[i] = nums[i - 1] * prefix[i - 1] 

        for i in range(len(nums)): 
            prefix[i] = prefix[i] * suffix[i]
        
        return prefix

        # [0 6 6 3 1]
        # [1 -1 0 0 0]