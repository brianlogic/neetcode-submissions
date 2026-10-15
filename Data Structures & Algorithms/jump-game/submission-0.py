class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O (n ^ 2) brute force solution: at each index, jump all possible distances and see if you can reach the end 

        # better solution: repeated calculations. we can use dp, store a boolean to see if each index can reach the end with memoization stops us from calculating every jump each time. 
        # goal is to get a path of jumps from start to end 

        # let's start from end 
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True 

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, i + nums[i] + 1): 
                if j >= len(nums): 
                    break 
                if dp[j]:
                    dp[i] = True 
                    break 
        return dp[0] 