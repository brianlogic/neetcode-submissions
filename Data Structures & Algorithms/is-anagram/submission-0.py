class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O (n + m) 
        # loop through one and create a seen dictionary (character, count), then loop through the other 
        # if a char not in seen, return false
        # subtract every time you see a letter
        # if count of any character > 0, then you have a mismatch return false
        # else return true 
        seen = {}
        
        for char in s: 
            if char in seen: 
                seen[char] += 1
            else:
                seen[char] = 1 
        
        for char in t: 
            if char in seen: 
                seen[char] -= 1
            else: 
                return False 
        
        for key in seen.keys(): 
            if seen[key] != 0: 
                return False

        return True 

        