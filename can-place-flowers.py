class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        dem = 0
        dodai = len(flowerbed)

        for i in range(dodai):

            # kiểm tra bên trái
            trai = (i == 0) or (flowerbed[i - 1] == 0)

            # kiểm tra bên phải
            phai = (i == dodai - 1) or (flowerbed[i + 1] == 0)

            # nếu ô hiện tại trống và 2 bên đều trống
            if flowerbed[i] == 0 and trai and phai:

                flowerbed[i] = 1
                dem += 1

        return dem >= n