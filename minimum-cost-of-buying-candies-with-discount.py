class Solution(object):

    def minimumCost(self, cost):

        # Sort giảm dần
        cost.sort(reverse=True)

        tong = 0

        for i in range(len(cost)):

            # Mỗi viên thứ 3 miễn phí
            if (i + 1) % 3 != 0:

                tong += cost[i]

        return tong