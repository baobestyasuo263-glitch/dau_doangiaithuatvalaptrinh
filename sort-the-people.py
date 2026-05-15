class Solution(object):

    def sortPeople(self, names, heights):

        pairs = zip(heights, names)

        pairs.sort(reverse=True)

        ketqua = []

        for h, n in pairs:

            ketqua.append(n)

        return ketqua