import math

class Solution(object):

    def pickGifts(self, gifts, k):

        for i in range(k):

            # Tìm đống lớn nhất
            lon_nhat = max(gifts)

            idx = gifts.index(lon_nhat)

            # Thay bằng căn bậc 2
            gifts[idx] = int(math.sqrt(lon_nhat))

        return sum(gifts)
        