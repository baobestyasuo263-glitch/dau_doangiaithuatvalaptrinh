class Solution(object):

    def numIslands(self, grid):

        # Nếu grid rỗng
        if not grid:
            return 0

        # Số hàng
        rows = len(grid)

        # Số cột
        cols = len(grid[0])

        # Đếm số đảo
        dem = 0

        # Hàm DFS để xóa đảo
        def dfs(r, c):

            # Nếu ra ngoài ma trận
            # hoặc gặp nước
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                grid[r][c] == "0"
            ):
                return

            # Đánh dấu đã thăm
            grid[r][c] = "0"

            # Đi 4 hướng
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Duyệt toàn bộ ma trận
        for r in range(rows):

            for c in range(cols):

                # Nếu gặp đất
                if grid[r][c] == "1":

                    # Tăng số đảo
                    dem += 1

                    # Xóa cả đảo
                    dfs(r, c)

        return dem