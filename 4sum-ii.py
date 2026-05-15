class Solution(object):

    def fourSumCount(self, A, B, C, D):

        dem = {}

        # Tổng A+B
        for a in A:

            for b in B:

                tong = a + b

                if tong in dem:
                    dem[tong] += 1
                else:
                    dem[tong] = 1

        ketqua = 0

        # Tìm số đối
        for c in C:

            for d in D:

                tong = c + d

                if -tong in dem:

                    ketqua += dem[-tong]

        return ketqua