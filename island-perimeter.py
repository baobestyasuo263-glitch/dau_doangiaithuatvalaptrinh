class Solution(object):

    def islandPerimeter(self, grid):

        # Chu vi
        chuvi = 0

        # Duyệt từng ô
        for r in range(len(grid)):

            for c in range(len(grid[0])):

                # Nếu là đất
                if grid[r][c] == 1:

                    # Mỗi ô có 4 cạnh
                    chuvi += 4

                    # Nếu phía trên là đất
                    # trừ 2 cạnh
                    if r > 0 and grid[r - 1][c] == 1:

                        chuvi -= 2

                    # Nếu bên trái là đất
                    # trừ 2 cạnh
                    if c > 0 and grid[r][c - 1] == 1:

                        chuvi -= 2

        return chuvi