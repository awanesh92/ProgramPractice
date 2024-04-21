from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<2:
            return 0

        maxProfit = 0

        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxProfit += prices[i]-prices[i-1]

        return maxProfit