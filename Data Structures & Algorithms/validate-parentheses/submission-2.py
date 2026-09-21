class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}": "{", "]": "[", ")": "("} # key is closing 

        stack = [] 

        for char in s: 
            if char in mapping.values(): 
                stack.append(char)
            else: 
                if len(stack) == 0 or stack.pop() != mapping[char]: 
                    return False
        return len(stack) == 0
