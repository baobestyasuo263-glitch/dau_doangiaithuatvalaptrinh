class Solution(object):

    def minimumSum(self, num):

        nums = sorted(str(num))

        a = int(nums[0] + nums[2])
        b = int(nums[1] + nums[3])

        return a + b
        