class Solution(object):

    def findMaxConsecutiveOnes(self, nums):

        # Đếm số 1 liên tiếp hiện tại
        dem = 0

        # Lưu kết quả lớn nhất
        lon_nhat = 0

        # Duyệt từng phần tử
        for i in nums:

            # Nếu gặp số 1
            if i == 1:

                # Tăng số lượng liên tiếp
                dem += 1

                # Cập nhật max
                if dem > lon_nhat:
                    lon_nhat = dem

            else:
                # Nếu gặp 0 thì reset
                dem = 0

        return lon_nhat