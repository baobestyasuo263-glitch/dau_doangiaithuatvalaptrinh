class Solution(object):

    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left < right:

            tong = numbers[left] + numbers[right]

            if tong == target:

                return [left + 1, right + 1]

            elif tong < target:

                left += 1

            else:

                right -= 1