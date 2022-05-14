class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices)==1:
            return profit
        left = 0
        right = 1
        while right<len(prices):
            if prices[right]>prices[left]:
                profit = max(profit, prices[right]-prices[left])
            else:
                left=right
            right+=1
        return profit
