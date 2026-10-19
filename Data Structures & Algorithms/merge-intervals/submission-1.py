from functools import cmp_to_key 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        # guarantees that the intervals are sorted by starting 

        # [1, 5], [2, 3]

        l = intervals[0][0] # tracks left bound of current interval
        r = intervals[0][1] # tracks right bound of current interval

        result = []

        for i in range(1, len(intervals) + 1): 
            if i == len(intervals): 
                result.append([l,r])
            elif intervals[i][0] > r: # current interval has no overlap
                result.append([l,r])
                l, r = intervals[i][0], intervals[i][1]
            else:
                r = max(intervals[i][1], r)
        
        return result 
        

