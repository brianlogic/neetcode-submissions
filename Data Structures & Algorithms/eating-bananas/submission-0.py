import math
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateEatingTime(rate):
            time = 0
            for pile in piles:
                time += (pile + rate - 1) // rate
            return time

        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2

            if calculateEatingTime(mid) <= h:
                r = mid
            else:
                l = mid + 1

        return l

    

        