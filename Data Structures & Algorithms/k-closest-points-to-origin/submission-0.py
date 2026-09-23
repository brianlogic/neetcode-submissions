import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: 
        heap = [] 
        for point in points: 
            heap.append((self.distance(point[0], point[1]), point))
        heapq.heapify(heap)

        result = [] 
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result 
        
    def distance(self, x, y): 
        return ( (0 - x) ** 2 + (0 - y) ** 2 ) ** (1/2)