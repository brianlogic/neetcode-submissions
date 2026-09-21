import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # no sorting, use a max heap, pop k elements 
        for i in range(len(nums)): # O (n) 
            nums[i] = -nums[i] # convert values to negative for max heap
        heapq.heapify(nums)

        value = 0
        for _ in range(k): 
            value = heapq.heappop(nums)
        return -value 


        