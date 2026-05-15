class Solution(object):

    def findClosestElements(self, arr, k, x):

        arr.sort(key=lambda n: (abs(n - x), n))

        ketqua = arr[:k]

        return sorted(ketqua)