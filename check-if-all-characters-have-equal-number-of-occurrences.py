class Solution(object):

    def areOccurrencesEqual(self, s):

        dem = {}

        for c in s:

            if c in dem:
                dem[c] += 1
            else:
                dem[c] = 1

        values = dem.values()

        for i in values:

            if i != values[0]:
                return False

        return True