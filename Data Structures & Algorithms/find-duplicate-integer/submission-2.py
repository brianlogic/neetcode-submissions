class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # loop through list
        # place numbers in their n - 1 index
        # keep swapping till all numbers are found
        # modifys the array

        # 3 1 2 1

        for i in range(len(nums)): 
            while nums[i] - 1 != i:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                temp = nums[i]
                nums[i] = nums[nums[i] - 1] 
                nums[temp - 1] = temp
        
        # two phase algorithm to find start of cycle/duplicate number
        # treat numbers as pointers, nums[i] - 1 as an index
        # there will be a cycle 
        

        
