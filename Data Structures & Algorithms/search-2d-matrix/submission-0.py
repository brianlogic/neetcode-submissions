class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0 
        b = len(matrix)

        while t < b: 
            mid = (t + b) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target: # find first element greater than target 
                b = mid 
            else: 
                t = mid + 1
        
        # we use b - 1

        l = 0
        r = len(matrix[0]) 

        while l < r: 
            mid = (l + r) // 2
            if matrix[b - 1][mid] == target:
                return True
            elif matrix[b - 1][mid] > target: 
                r = mid
            else:
                l = mid + 1
        
        return False 
        




