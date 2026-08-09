class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price<min_price:
                min_price=price
            elif price-min_price>max_profit:
                max_profit=price-min_price
        return max_profit"""


        max_current = 0
        max_profit = 0
        for i in range(1, len(prices)):
            max_current = max(0, max_current + prices[i] - prices[i-1])
            max_profit = max(max_profit, max_current)
        return max_profit

        
    