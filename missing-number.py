class Solution(object):

    def missingNumber(self, nums):

        # Tổng từ 0 -> n
        tong = len(nums) * (len(nums) + 1) // 2

        # Trừ tổng hiện tại
        return tong - sum(nums)