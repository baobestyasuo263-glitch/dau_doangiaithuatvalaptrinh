class Solution(object):

    def sumOfTheDigitsOfHarshadNumber(self, x):

        tong = 0

        # Tính tổng chữ số
        for c in str(x):

            tong += int(c)

        # Nếu chia hết
        if x % tong == 0:

            return tong

        return -1