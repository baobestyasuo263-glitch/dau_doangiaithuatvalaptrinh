class Solution(object):

    def threeSum(self, nums):

        nums.sort()

        ketqua = []

        for i in range(len(nums)):

            # Bỏ trùng
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                tong = nums[i] + nums[left] + nums[right]

                if tong == 0:

                    ketqua.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Bỏ trùng
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif tong < 0:

                    left += 1

                else:

                    right -= 1

        return ketqua