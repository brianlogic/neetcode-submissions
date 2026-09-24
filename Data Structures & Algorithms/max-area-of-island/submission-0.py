class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (1,0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        max_area = 0 
        
        def dfs(r, c): 
            if (
                r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == 0
            ):
                return 0 
            else: 
                grid[r][c] = 0
                count = 1
                for dr, dc in directions: 
                    count += dfs(r + dr, c + dc)
                return count 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        return max_area 