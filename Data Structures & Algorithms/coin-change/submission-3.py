class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # greedy doesn't work 

        # 1 3 4, amount = 12, 

        # idea: at an amount subtract each possible coin to take you to a new value
        # then for that new value subtract again, until you're able to reach 0
        # keep count of the amount of coins you use
        # the repeated work is that you often end up at the same value, so rather than recalculating 
        # you memoize


        # we should go the other way, start at 0 and add coins to get to amounts, then see if you can reach the target
        if amount == 0:
            return 0

        dp = [-1] * (amount + 1) # 1 indexed to make it easier

        # stores the minimum coins need to reach that amount 

        # if value is -1, it is unreachable

        # bottom up approach

        for coin in coins: 
            if coin <= amount:
                dp[coin] = 1

        for i in range(amount + 1): 
            if i < coins[0] or dp[i] != -1: 
                pass
            else: # amount can be subtracted by a coin
                # subtract each coin value to see if it could be reached by a previous amount
                # take minimum of those
                for coin in coins: 
                    if i < coin: 
                        pass
                    elif dp[i - coin] >= 0: # path is valid
                        if dp[i] == -1:
                            dp[i] = dp[i - coin] + 1
                        else: 
                            dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount]



