class Solution(object):

    def floodFill(self, image, sr, sc, color):

        # Màu gốc
        old = image[sr][sc]

        # Nếu màu giống nhau
        if old == color:
            return image

        # DFS
        def dfs(r, c):

            # Nếu ra ngoài
            if (
                r < 0 or
                c < 0 or
                r >= len(image) or
                c >= len(image[0])
            ):
                return

            # Nếu khác màu gốc
            if image[r][c] != old:
                return

            # Tô màu mới
            image[r][c] = color

            # Đi 4 hướng
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image
        