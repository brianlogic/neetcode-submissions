class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} 

        def helper(index, current): 
            if index >= len(nums): 
                return 1 if current == 0 else 0
            if (index, current) in dp:
                return dp[(index, current)]
            else: 
                dp[(index, current)] = (
                    helper(index + 1, current - nums[index]) + 
                    helper(index + 1, current + nums[index])
                )
                return dp[(index, current)]
        
        return helper(0, target)