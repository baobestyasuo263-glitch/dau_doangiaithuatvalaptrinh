class Solution(object):

    def findPoisonedDuration(self, timeSeries, duration):

        # Nếu mảng rỗng
        if not timeSeries:
            return 0

        tong = 0

        # Duyệt các lần tấn công
        for i in range(len(timeSeries) - 1):

            # Khoảng cách giữa 2 lần đánh
            khoang = timeSeries[i + 1] - timeSeries[i]

            # Nếu chưa hết độc mà bị đánh tiếp
            tong += min(khoang, duration)

        # Cộng duration cuối cùng
        tong += duration

        return tong