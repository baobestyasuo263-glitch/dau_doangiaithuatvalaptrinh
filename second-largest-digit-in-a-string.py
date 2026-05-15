class Solution(object):

    def secondHighest(self, s):

        nums = set()

        for c in s:

            if c.isdigit():
                nums.add(int(c))

        nums = list(nums)

        if len(nums) < 2:
            return -1

        nums.sort()

        return nums[-2]
        