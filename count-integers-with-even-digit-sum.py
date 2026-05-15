class Solution(object):

    def countEven(self, num):

        dem = 0

        for i in range(1, num + 1):

            tong = 0

            for c in str(i):

                tong += int(c)

            if tong % 2 == 0:

                dem += 1

        return dem