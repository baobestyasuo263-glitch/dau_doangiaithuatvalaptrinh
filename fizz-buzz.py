class Solution(object):

    def fizzBuzz(self, n):

        ketqua = []

        # Duyệt từ 1 -> n
        for i in range(1, n + 1):

            # Chia hết cho cả 3 và 5
            if i % 3 == 0 and i % 5 == 0:

                ketqua.append("FizzBuzz")

            # Chia hết cho 3
            elif i % 3 == 0:

                ketqua.append("Fizz")

            # Chia hết cho 5
            elif i % 5 == 0:

                ketqua.append("Buzz")

            # Không chia hết
            else:

                # Đổi số thành chuỗi
                ketqua.append(str(i))

        return ketqua