class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # at each index we choose whether to include the number or not

        result = []

        state = []

        def backtrack(index, total): # we use index to track what position we're on and total to avoid summing up the set everytime. 
            if index >= len(nums):
                return 
            elif total > target: # all nums positive so we can't subtract anything
                return 
            elif total == target: 
                if not state in result: 
                    result.append(state.copy())
                return 

            # choice 1 include the number at index
            total += nums[index]

            state.append(nums[index])

            backtrack(index, total)

            # undo inclusion

            state.pop()
            total -= nums[index]

            # choice 2 skip the number at index

            backtrack(index + 1, total)

        backtrack(0, 0) 
        return result 