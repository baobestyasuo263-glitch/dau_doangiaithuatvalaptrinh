class Solution(object):

    def findJudge(self, n, trust):

        # Mảng đếm điểm
        diem = [0] * (n + 1)

        # Duyệt trust
        for a, b in trust:

            # a tin người khác
            diem[a] -= 1

            # b được tin
            diem[b] += 1

        # Tìm judge
        for i in range(1, n + 1):

            # Judge phải có n-1 điểm
            if diem[i] == n - 1:

                return i

        return -1
        