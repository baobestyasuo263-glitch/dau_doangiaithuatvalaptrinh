class Solution(object):

    def sumZero(self, n):

        ketqua = []

        # Thêm từng cặp đối nhau
        for i in range(1, n // 2 + 1):

            ketqua.append(i)
            ketqua.append(-i)

        # Nếu n lẻ thì thêm 0
        if n % 2 == 1:

            ketqua.append(0)

        return ketqua