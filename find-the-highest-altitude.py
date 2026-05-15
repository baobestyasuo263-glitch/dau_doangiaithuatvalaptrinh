class Solution(object):

    def largestAltitude(self, gain):

        cao = 0
        max_cao = 0

        for i in gain:

            cao += i

            if cao > max_cao:
                max_cao = cao

        return max_cao