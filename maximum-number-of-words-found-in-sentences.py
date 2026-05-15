class Solution(object):

    def mostWordsFound(self, sentences):

        lon_nhat = 0

        for s in sentences:

            # split để đếm số từ
            so_tu = len(s.split())

            lon_nhat = max(lon_nhat, so_tu)

        return lon_nhat