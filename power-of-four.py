class Solution(object):

    def isPowerOfFour(self, n):

        # Số <=0
        if n <= 0:

            return False

        # Chia liên tục cho 4
        while n % 4 == 0:

            n //= 4

        # Nếu còn 1
        return n == 1