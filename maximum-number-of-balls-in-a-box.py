class Solution(object):

    def countBalls(self, lowLimit, highLimit):

        dem = {}

        for i in range(lowLimit, highLimit + 1):

            # Tổng chữ số
            tong = sum(map(int, str(i)))

            if tong in dem:
                dem[tong] += 1
            else:
                dem[tong] = 1

        return max(dem.values())