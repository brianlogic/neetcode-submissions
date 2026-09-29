class Solution:
    def findMin(self, nums: List[int]) -> int:
        # half of the list is always going to be sorted 
        # so we can find the min of that half by checking the first index 
        # find the sorted half by comparing first and left elements of it
        # then we unsorted half, and again split it 

        l = 0
        r = len(nums)
        min_value = 1001
        while l < r: 
            mid = (l + r) // 2 
            if nums[l] <= nums[mid]: # left half is sorted 
                min_value = min(min_value, nums[l])
                l = mid + 1 # now we examine unsorted half
            else: # right half is sorted
                min_value = min(min_value, nums[mid])
                r = mid
        return min_value

        
