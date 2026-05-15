class Solution(object):

    def pivotInteger(self, n):

        tong = n * (n + 1) // 2

        trai = 0

        for x in range(1, n + 1):

            trai += x

            if trai == tong - trai + x:

                return x

        return -1