class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # normal 2 sum? 
        hashmap = {}
        for i in range(len(numbers)): 
            if target - numbers[i] in hashmap: 
                return [hashmap[target - numbers[i]] + 1, i + 1] 
            hashmap[numbers[i]] = i
        