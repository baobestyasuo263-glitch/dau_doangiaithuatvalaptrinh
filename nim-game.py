class Solution(object):

    def canWinNim(self, n):

        # Nếu chia hết cho 4
        # sẽ thua
        return n % 4 != 0