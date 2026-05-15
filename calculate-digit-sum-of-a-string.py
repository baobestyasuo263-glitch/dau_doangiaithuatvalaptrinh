class Solution(object):

    def digitSum(self, s, k):

        # Lặp tới khi đủ ngắn
        while len(s) > k:

            moi = ""

            # Chia nhóm k ký tự
            for i in range(0, len(s), k):

                # Lấy nhóm
                group = s[i:i+k]

                tong = 0

                # Tính tổng chữ số
                for c in group:

                    tong += int(c)

                # Ghép vào chuỗi mới
                moi += str(tong)

            s = moi

        return s
        