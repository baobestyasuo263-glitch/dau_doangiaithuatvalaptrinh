class Solution(object):

    def decrypt(self, code, k):

        n = len(code)

        ketqua = [0] * n

        # Nếu k = 0
        if k == 0:

            return ketqua

        # Duyệt từng phần tử
        for i in range(n):

            tong = 0

            # k dương
            if k > 0:

                for j in range(1, k + 1):

                    tong += code[(i + j) % n]

            # k âm
            else:

                for j in range(1, abs(k) + 1):

                    tong += code[(i - j) % n]

            ketqua[i] = tong

        return ketqua