class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = 0 
        majority = 0

        for num in nums:
            if majority_count == 0: 
                majority = num
                majority_count += 1
            elif num == majority: 
                majority_count += 1
            else: 
                majority_count -= 1
        
        return majority 