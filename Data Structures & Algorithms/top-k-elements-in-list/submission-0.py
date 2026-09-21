import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency: 
                frequency[num] += 1 
            else:
                frequency[num] = 1 

        heap = [(-frequency[value], value) for value in frequency]
        heapq.heapify(heap)

        output = [] 
        for _ in range(k): 
            output.append(heapq.heappop(heap)[1])
        return output 