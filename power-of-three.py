class Solution(object):

    def isPowerOfThree(self, n):

        # Số <=0 không hợp lệ
        if n <= 0:

            return False

        # Chia liên tục cho 3
        while n % 3 == 0:

            n //= 3

        # Nếu còn 1
        return n == 1