class Solution(object):

    def threeSumClosest(self, nums, target):

        nums.sort()

        gan_nhat = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                tong = nums[i] + nums[left] + nums[right]

                # Cập nhật gần nhất
                if abs(target - tong) < abs(target - gan_nhat):

                    gan_nhat = tong

                if tong < target:

                    left += 1

                elif tong > target:

                    right -= 1

                else:
                    return tong

        return gan_nhat