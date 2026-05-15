class Solution(object):

    def divideArray(self, nums):

        dem = {}

        # Đếm số lần xuất hiện
        for i in nums:

            if i in dem:
                dem[i] += 1
            else:
                dem[i] = 1

        # Kiểm tra số lần xuất hiện
        for i in dem:

            if dem[i] % 2 != 0:

                return False

        return True