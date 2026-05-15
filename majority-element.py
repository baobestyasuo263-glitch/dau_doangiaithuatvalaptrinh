class Solution(object):

    def majorityElement(self, nums):

        # Sort
        nums.sort()

        # Phần tử giữa luôn là majority
        return nums[len(nums)//2]