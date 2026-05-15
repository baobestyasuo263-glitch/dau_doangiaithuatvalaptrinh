class Solution(object):

    def passThePillow(self, n, time):

        # Chu kỳ đi-về
        vong = n - 1

        # Vị trí trong chu kỳ
        x = time % (2 * vong)

        # Đi tới
        if x <= vong:

            return x + 1

        # Đi ngược
        return 2 * vong - x + 1