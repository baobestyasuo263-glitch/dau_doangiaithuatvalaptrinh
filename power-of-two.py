class Solution(object):

    def isPowerOfTwo(self, n):

        # n phải > 0
        # power of two chỉ có 1 bit 1
        return n > 0 and (n & (n - 1)) == 0