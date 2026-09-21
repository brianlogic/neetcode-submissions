class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # normal 2 sum? 
        l = 0
        r = len(numbers) - 1 
        while l < r: 
            if numbers[r] > target - numbers[l]: 
                r -= 1
            elif numbers[l] < target - numbers[r]: 
                l += 1 
            else: 
                return [l + 1, r + 1]