class Solution(object):

    def moveZeroes(self, nums):

        k = 0

        # Đưa số khác 0 lên trước
        for i in nums:

            if i != 0:

                nums[k] = i
                k += 1

        # Điền 0 vào cuối
        while k < len(nums):

            nums[k] = 0
            k += 1