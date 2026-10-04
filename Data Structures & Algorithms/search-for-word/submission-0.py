class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        found = False 

        def backtrack(path, string, r, c, index):
            nonlocal found
            if found:
                return
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return # out of bounds
            elif board[r][c] != word[index] or path[r][c]: 
                return # wrong letter or we've already used this index
            
            if index == len(word) - 1:
                found = True
                return

            path[r][c] = True 
            for row, col in directions: 
                backtrack(path, string, r + row, c + col, index + 1)
            path[r][c] = False

        path = [([False] * len(board[0])) for _ in range(len(board))]

        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if board[i][j] == word[0]: 
                    backtrack(path, "", i, j, 0)
        return found