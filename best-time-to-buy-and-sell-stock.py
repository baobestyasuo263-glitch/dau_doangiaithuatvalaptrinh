class Solution(object):

    def maxProfit(self, prices):

        min_price = prices[0]

        max_profit = 0

        for p in prices:

            # Cập nhật giá nhỏ nhất
            min_price = min(min_price, p)

            # Tính lợi nhuận
            max_profit = max(max_profit, p - min_price)

        return max_profit