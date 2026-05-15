class Solution(object):

    def isUgly(self, n):

        # Số <=0 không phải ugly
        if n <= 0:

            return False

        # Chia liên tục cho 2
        while n % 2 == 0:

            n //= 2

        # Chia liên tục cho 3
        while n % 3 == 0:

            n //= 3

        # Chia liên tục cho 5
        while n % 5 == 0:

            n //= 5

        # Nếu còn 1
        return n == 1