class Solution(object):

    def buyChoco(self, prices, money):

        # Sort tăng dần
        prices.sort()

        # Giá 2 viên rẻ nhất
        tong = prices[0] + prices[1]

        # Nếu đủ tiền
        if tong <= money:

            return money - tong

        return money