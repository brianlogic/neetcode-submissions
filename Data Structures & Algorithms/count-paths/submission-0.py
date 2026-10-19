class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # d[m][n] = dp[m - 1][n] + dp[m][n - 1] + 2

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        def getCost(r, c): 
            if r < 0 or r >= m or c < 0 or c >= n: # out of bounds, contributes nothing
                return 0 
            elif dp[r][c] > 0: # already memoized 
                return dp[r][c]
            else:
                dp[r][c] = getCost(r - 1, c) + getCost(r, c - 1)
                return dp[r][c] 
        
        return getCost(m - 1, n - 1)