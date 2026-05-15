class Solution(object):

    def fib(self, n):

        # Nếu n nhỏ
        if n <= 1:

            return n

        a = 0
        b = 1

        # Tính fibonacci
        for i in range(2, n + 1):

            a, b = b, a + b

        return b