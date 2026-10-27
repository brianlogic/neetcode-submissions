class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        state = []

        def backtrack(index, total):
            if total > target: 
                return 
            elif total == target: 
                if not state in result: 
                    result.append(state.copy())
                return 

            for i in range(index, len(nums)):
                state.append(nums[i])

                backtrack(i, total + nums[i])

                state.pop()

        backtrack(0, 0) 
        return result 