class Solution(object):

    def mostCommonWord(self, paragraph, banned):

        # Đổi về chữ thường
        paragraph = paragraph.lower()

        # Thay ký tự đặc biệt thành khoảng trắng
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        words = paragraph.split()

        dem = {}

        for w in words:

            if w not in banned:

                if w in dem:
                    dem[w] += 1
                else:
                    dem[w] = 1

        # Tìm từ xuất hiện nhiều nhất
        lon_nhat = ""
        max_dem = 0

        for w in dem:

            if dem[w] > max_dem:

                max_dem = dem[w]
                lon_nhat = w

        return lon_nhat