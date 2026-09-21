class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1 
        highest_profit = 0 
        while r < len(prices): # sliding window, move left pointer if there is elmement smaller on the right 
            highest_profit = max(highest_profit, prices[r] - prices[l])
            if prices[r] < prices[l]: 
                l = r 
            r += 1
        return highest_profit 