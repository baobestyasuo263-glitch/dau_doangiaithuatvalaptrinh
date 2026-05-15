class Solution(object):

    def selfDividingNumbers(self, left, right):

        ketqua = []

        # Duyệt các số
        for num in range(left, right + 1):

            hop_le = True

            # Duyệt từng chữ số
            for c in str(num):

                # Nếu có số 0
                if c == '0':

                    hop_le = False
                    break

                # Nếu không chia hết
                if num % int(c) != 0:

                    hop_le = False
                    break

            # Nếu hợp lệ
            if hop_le:

                ketqua.append(num)

        return ketqua
        