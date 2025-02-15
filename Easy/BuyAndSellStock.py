from typing import List


class Solution:

    #####BRUTE FORCE####

    """ def maxProfit(self, prices: List[int]) -> int:

        #BruteForce
        max_profit = 0

        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(i+1,len(prices)):
                sell_price = prices[j]
                max_profit = max(max_profit,sell_price-buy_price)
        return max_profit """

    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:               #SellPrice should always be greater than BuyPrice to calculate profit
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:                                   #No Profit 
                l = r                               
            r += 1
        return maxP