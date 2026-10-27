class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = [] 

        state = [] 

        def backtrack(l, r): # l is ( remaining, and r is ) remaining 
            if l == 0 and r == 0: 
                results.append("".join(state))
                return 

            if l > 0: 
                state.append("(")
                backtrack(l - 1, r + 1)
                state.pop() 
            if r > 0: 
                state.append(")")
                backtrack(l, r - 1)
                state.pop() 
            
        backtrack(n, 0)

        return results