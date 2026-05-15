class Solution(object):

    def prefixCount(self, words, pref):

        dem = 0

        for w in words:

            if w.startswith(pref):

                dem += 1

        return dem
        