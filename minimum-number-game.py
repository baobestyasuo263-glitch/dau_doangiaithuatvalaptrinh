class Solution(object):

    def numberGame(self, nums):

        nums.sort()

        ketqua = []

        for i in range(0, len(nums), 2):

            ketqua.append(nums[i + 1])
            ketqua.append(nums[i])

        return ketqua