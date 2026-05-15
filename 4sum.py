class Solution(object):

    def fourSum(self, nums, target):

        nums.sort()

        ketqua = []

        n = len(nums)

        # Chọn số thứ nhất
        for i in range(n - 3):

            # Bỏ trùng
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Chọn số thứ hai
            for j in range(i + 1, n - 2):

                # Bỏ trùng
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 2 con trỏ
                left = j + 1
                right = n - 1

                while left < right:

                    tong = nums[i] + nums[j] + nums[left] + nums[right]

                    # Nếu bằng target
                    if tong == target:

                        ketqua.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Bỏ trùng bên trái
                        while left < right and nums[left] == nums[left - 1]:

                            left += 1

                        # Bỏ trùng bên phải
                        while left < right and nums[right] == nums[right + 1]:

                            right -= 1

                    # Nếu tổng nhỏ hơn target
                    elif tong < target:

                        left += 1

                    # Nếu tổng lớn hơn
                    else:

                        right -= 1

        return ketqua