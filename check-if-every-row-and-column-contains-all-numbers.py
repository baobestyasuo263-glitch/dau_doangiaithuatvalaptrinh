class Solution(object):

    def checkValid(self, matrix):

        n = len(matrix)

        dung = set(range(1, n + 1))

        # Kiểm tra hàng
        for row in matrix:

            if set(row) != dung:
                return False

        # Kiểm tra cột
        for c in range(n):

            cot = []

            for r in range(n):

                cot.append(matrix[r][c])

            if set(cot) != dung:
                return False

        return True