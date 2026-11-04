class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 

        jumps = 1
        max_range = nums[0]
        curr_range = nums[0]
        for i in range(len(nums)): 
            if i > curr_range: 
                curr_range = max_range
                jumps += 1
            max_range = max(max_range, i + nums[i])
        return jumps