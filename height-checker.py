class Solution(object):

    def heightChecker(self, heights):

        # Mảng đã sắp xếp
        sapxep = sorted(heights)

        dem = 0

        # So sánh từng vị trí
        for i in range(len(heights)):

            if heights[i] != sapxep[i]:

                dem += 1

        return dem