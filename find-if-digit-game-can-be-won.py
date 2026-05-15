class Solution(object):

    def canAliceWin(self, nums):

        # Tổng số có 1 chữ số
        a = 0

        # Tổng số có 2 chữ số
        b = 0

        for i in nums:

            # 1 chữ số
            if i < 10:

                a += i

            # 2 chữ số
            else:

                b += i

        # Alice thắng nếu tổng khác nhau
        return a != b
        