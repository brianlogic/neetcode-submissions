class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # each digit is tied to 3 or 4 letters.
        # loop through the digits, and their respective letters to create
        # every combination possible

        # list, 
        results = [] 

        mapping = {}
        mapping["2"] = "abc"
        mapping["3"] = "def"
        mapping["4"] = "ghi"
        mapping["5"] = "jkl"
        mapping["6"] = "mno"
        mapping["7"] = "pqrs"
        mapping["8"] = "tuv"
        mapping["9"] = "wxyz"

        state = [] 

        def backtrack(index): 
            if index == len(digits): 
                results.append("".join(state))
                return 
            
            for char in mapping[digits[index]]:
                state.append(char)
                backtrack(index + 1)
                state.pop() 
        
        backtrack(0)
        return results if len(digits) > 0 else [] 


