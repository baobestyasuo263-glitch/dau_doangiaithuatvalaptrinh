class Solution(object):

    def sumOfMultiples(self, n):

        tong = 0

        # Duyệt từ 1 -> n
        for i in range(1, n + 1):

            # Nếu chia hết
            if (
                i % 3 == 0 or
                i % 5 == 0 or
                i % 7 == 0
            ):

                tong += i

        return tong