class Solution(object):

    def convertTime(self, current, correct):

        # Đổi sang phút
        h1, m1 = map(int, current.split(":"))
        h2, m2 = map(int, correct.split(":"))

        now = h1 * 60 + m1
        target = h2 * 60 + m2

        # Hiệu phút
        diff = target - now

        dem = 0

        # Các bước cho phép
        arr = [60, 15, 5, 1]

        for i in arr:

            # Lấy được bao nhiêu lần
            dem += diff // i

            # Phần còn lại
            diff %= i

        return dem
        