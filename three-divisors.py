class Solution(object):

    def isThree(self, n):

        # Tìm căn
        root = int(n ** 0.5)

        # Phải là số chính phương
        if root * root != n:

            return False

        # Kiểm tra nguyên tố
        for i in range(2, root):

            if root % i == 0:

                return False

        return root > 1