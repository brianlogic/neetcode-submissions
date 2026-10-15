class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        farthest = nums[l]

        while l <= farthest: 
            if l == len(nums) - 1: return True 
            farthest = max(farthest, l + nums[l])
            l += 1 
        return False