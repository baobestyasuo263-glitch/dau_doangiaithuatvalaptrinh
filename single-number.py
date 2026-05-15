class Solution(object):

    def singleNumber(self, nums):

        ketqua = 0

        # XOR toàn bộ
        for i in nums:

            ketqua ^= i

        return ketqua