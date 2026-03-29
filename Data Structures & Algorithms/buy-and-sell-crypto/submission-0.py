class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for i, p in enumerate(prices):
            if prices[:i]:
                profit = p - min(prices[:i])
                if profit > result:
                    result = profit

        return result    