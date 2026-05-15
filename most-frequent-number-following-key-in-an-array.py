class Solution(object):

    def mostFrequent(self, nums, key):

        dem = {}

        # Duyệt tới phần tử kế cuối
        for i in range(len(nums) - 1):

            # Nếu gặp key
            if nums[i] == key:

                target = nums[i + 1]

                if target in dem:
                    dem[target] += 1
                else:
                    dem[target] = 1

        # Tìm số xuất hiện nhiều nhất
        ketqua = 0
        lon_nhat = 0

        for i in dem:

            if dem[i] > lon_nhat:

                lon_nhat = dem[i]
                ketqua = i

        return ketqua