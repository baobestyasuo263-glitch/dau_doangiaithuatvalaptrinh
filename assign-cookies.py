class Solution(object):

    def findContentChildren(self, g, s):

        # Sắp xếp tăng dần
        g.sort()
        s.sort()

        i = 0  # trẻ em
        j = 0  # bánh

        dem = 0

        while i < len(g) and j < len(s):

            # Nếu bánh đủ lớn
            if s[j] >= g[i]:

                dem += 1
                i += 1
                j += 1

            else:
                # bánh quá nhỏ
                j += 1

        return dem