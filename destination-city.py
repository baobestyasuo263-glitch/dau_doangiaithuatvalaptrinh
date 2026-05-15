class Solution(object):

    def destCity(self, paths):

        di = set()

        # Lưu các thành phố xuất phát
        for a, b in paths:
            di.add(a)

        # Thành phố không xuất phát là đích
        for a, b in paths:

            if b not in di:
                return b