class Solution(object):

    def plusOne(self, digits):

        # Duyệt từ cuối
        for i in range(len(digits)-1, -1, -1):

            # Nếu nhỏ hơn 9
            if digits[i] < 9:

                digits[i] += 1

                return digits

            # Nếu là 9
            digits[i] = 0

        # Nếu toàn số 9
        return [1] + digits