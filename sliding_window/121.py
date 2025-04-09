# 121. Best Time to Buy and Sell Stock
# Easy
# 2025/04/05

class Solution:
    # TC: O(n), SC: O(1)
    def maxProfit(self, prices) -> int:
        max_profit = 0
        min_price = prices[0]

        for p in prices:   # 若寫成 for p in prices[1:], TC 變為 O(2n), SC 變為 O(n), 因為 list 切片為從切的 index 複製一份新的 list
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)
        
        return max_profit