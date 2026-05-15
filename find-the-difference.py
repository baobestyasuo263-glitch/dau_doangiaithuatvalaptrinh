class Solution(object):

    def findTheDifference(self, s, t):

        # Dictionary đếm ký tự
        dem = {}

        # Đếm ký tự trong s
        for c in s:

            if c in dem:
                dem[c] += 1
            else:
                dem[c] = 1

        # Duyệt chuỗi t
        for c in t:

            # Nếu ký tự không tồn tại
            # hoặc đã dùng hết
            if c not in dem or dem[c] == 0:

                return c

            # Giảm số lần xuất hiện
            dem[c] -= 1