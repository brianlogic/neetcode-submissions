class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n)
        # loop through array, keep set of seen elements
        seen = set() 

        for num in nums:
            if num in seen:
                return True
            else: 
                seen.add(num)
        return False