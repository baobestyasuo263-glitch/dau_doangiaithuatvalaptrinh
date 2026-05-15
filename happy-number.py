class Solution(object):

    def isHappy(self, n):

        # Set lưu số đã gặp
        seen = set()

        # Lặp tới khi gặp 1
        while n != 1 and n not in seen:

            # Đánh dấu đã gặp
            seen.add(n)

            tong = 0

            # Tính tổng bình phương chữ số
            for c in str(n):

                tong += int(c) ** 2

            n = tong

        return n == 1