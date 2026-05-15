class Solution(object):

    def containsNearbyDuplicate(self, nums, k):

        seen = {}

        for i in range(len(nums)):

            # Nếu đã xuất hiện
            if nums[i] in seen:

                # Kiểm tra khoảng cách
                if i - seen[nums[i]] <= k:

                    return True

            # Lưu vị trí mới nhất
            seen[nums[i]] = i

        return False