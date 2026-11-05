class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # add all values to a max heap, 
        # pop 2 values from the top, subtract the smaller from the larger
        # if a value is leftover add it back to the heap
        # repeat until we have 1 stone in the heap

        heap = [-num for num in stones] # negative to get max heap
        heapq.heapify(heap)

        while len(heap) > 1: 
            larger = heapq.heappop(heap)
            smaller = heapq.heappop(heap)
            if larger != smaller: 
                heapq.heappush(heap, larger - smaller)
                        
        return -heap[0] if len(heap) == 1 else 0