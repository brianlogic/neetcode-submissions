class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, track elements with a seen set 
        # when we find a duplicate, increment left pointer until there's no duplicate 
        # keep max 
        l = 0
        r = 0 
        max_length = 0 
        seen = set()
        while r < len(s): 
            while s[r] in seen: 
                seen.discard(s[l])
                l += 1
            seen.add(s[r]) 
            r += 1 
            max_length = max(max_length, r - l)
        return max_length  
