class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r: 
            mid = (l + r) // 2 
            # we have to find the sorted side 
            if nums[mid] == target:
                return mid 
            if nums[mid] >= nums[l]: # left sorted
                if nums[l] <= target < nums[mid]:
                    r = mid 
                else:
                    l = mid + 1
            else: # right sorted
                if nums[mid] <= target <= nums[r - 1]:  # can't be in right side
                    l = mid + 1
                else:
                    r = mid

        return -1 