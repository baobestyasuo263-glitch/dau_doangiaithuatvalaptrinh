class Solution(object):

    def reverse(self, x):

        # Lưu dấu âm
        dau = -1 if x < 0 else 1

        # Lấy trị tuyệt đối
        x = abs(x)

        # Đảo chuỗi
        x = int(str(x)[::-1])

        # Gắn lại dấu
        x *= dau

        # Kiểm tra overflow
        if x < -2**31 or x > 2**31 - 1:

            return 0

        return x