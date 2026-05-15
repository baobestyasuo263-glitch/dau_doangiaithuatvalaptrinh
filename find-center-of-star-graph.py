class Solution(object):

    def findCenter(self, edges):

        # Lấy 2 cạnh đầu
        a, b = edges[0]
        c, d = edges[1]

        # Node chung là center
        if a == c or a == d:
            return a

        return b