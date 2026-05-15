class Solution(object):

    def minimumMoves(self, s):

        dem = 0

        i = 0

        while i < len(s):

            # Nếu gặp X
            if s[i] == 'X':

                dem += 1

                # Skip 3 ký tự
                i += 3

            else:

                i += 1

        return dem