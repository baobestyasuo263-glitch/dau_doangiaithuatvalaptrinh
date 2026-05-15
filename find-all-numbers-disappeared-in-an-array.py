class Solution(object):

    def findDisappearedNumbers(self, nums):

        # Set để lưu các số đã xuất hiện
        da_co = set(nums)

        ketqua = []

        # Duyệt từ 1 -> n
        for i in range(1, len(nums) + 1):

            # Nếu số chưa xuất hiện
            if i not in da_co:

                ketqua.append(i)

        return ketqua
        