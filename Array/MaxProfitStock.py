from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        n = len(prices)
        maxprofit = 0
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                maxprofit += prices[i+1] - prices[i]
            
        return maxprofit