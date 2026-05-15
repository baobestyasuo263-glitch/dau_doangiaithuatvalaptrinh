class Solution(object):

    def countElements(self, nums):

        nho = min(nums)
        lon = max(nums)

        dem = 0

        for i in nums:

            if i > nho and i < lon:

                dem += 1

        return dem
        