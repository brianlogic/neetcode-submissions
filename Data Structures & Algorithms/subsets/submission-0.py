class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        def backtrack(index, choices): 
            if index == len(nums): 
                result.append(choices[:])
                return 
            
            # include index 
            choices.append(nums[index])
            backtrack(index + 1, choices)
            choices.pop() 

            # skip 
            backtrack(index + 1, choices)
            
        backtrack(0, [])

        return result 