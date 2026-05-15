class Solution(object):

    def addDigits(self, num):

        # Lặp tới khi còn 1 chữ số
        while num >= 10:

            tong = 0

            # Tính tổng chữ số
            for c in str(num):

                tong += int(c)

            num = tong

        return num