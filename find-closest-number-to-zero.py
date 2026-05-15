class Solution(object):

    def findClosestNumber(self, nums):

        ketqua = nums[0]

        for i in nums:

            # Nếu gần 0 hơn
            if abs(i) < abs(ketqua):

                ketqua = i

            # Nếu khoảng cách bằng nhau
            elif abs(i) == abs(ketqua):

                ketqua = max(i, ketqua)

        return ketqua