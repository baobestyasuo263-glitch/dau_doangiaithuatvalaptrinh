class Solution(object):

    def checkPerfectNumber(self, num):

        # 1 không phải perfect
        if num == 1:

            return False

        # Tổng ước
        tong = 1

        # Duyệt tới căn bậc 2
        for i in range(2, int(num**0.5) + 1):

            # Nếu là ước
            if num % i == 0:

                tong += i

                # Thêm ước còn lại
                tong += num // i

        return tong == num