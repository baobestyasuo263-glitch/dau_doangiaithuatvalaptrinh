class Solution(object):

    def distributeCandies(self, candyType):

        # Số loại kẹo khác nhau
        loai = len(set(candyType))

        # Số kẹo được ăn
        duoc_an = len(candyType) // 2

        return min(loai, duoc_an)