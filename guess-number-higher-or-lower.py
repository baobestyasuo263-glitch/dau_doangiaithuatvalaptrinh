class Solution(object):

    def guessNumber(self, n):

        left = 1
        right = n

        while left <= right:

            mid = (left + right) // 2

            kq = guess(mid)

            if kq == 0:

                return mid

            elif kq == 1:

                left = mid + 1

            else:

                right = mid - 1