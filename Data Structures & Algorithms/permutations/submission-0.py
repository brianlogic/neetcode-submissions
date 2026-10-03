class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking problem

        result = [] 

        def backtrack(path, choices): 
            if len(path) == len(nums):
                result.append(path)
                return 

            for i in range(len(nums)): 
                if not choices[i]: # element not used
                    # choice 1: add element
                    path.append(nums[i])
                    choices[i] = True 
                    backtrack(path[:], choices[:])

                    choices[i] = False 
                    path.pop() 
            
        choices = [False] * len(nums) 
        backtrack([], choices)
        return result 
        