class Solution(object):

    def addBinary(self, a, b):

        # Chuyển sang decimal
        x = int(a, 2)

        y = int(b, 2)

        # Cộng rồi đổi lại binary
        return bin(x + y)[2:]
        