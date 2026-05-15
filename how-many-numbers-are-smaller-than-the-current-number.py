class Solution(object):

    def smallerNumbersThanCurrent(self, nums):

        ketqua = []

        # Duyệt từng số
        for i in nums:

            dem = 0

            # So sánh với toàn bộ mảng
            for j in nums:

                if j < i:
                    dem += 1

            ketqua.append(dem)

        return ketqua
        