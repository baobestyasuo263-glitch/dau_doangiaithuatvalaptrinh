class Solution(object):

    def binaryTreePaths(self, root):

        ketqua = []

        def dfs(node, path):

            if not node:
                return

            path += str(node.val)

            # Nếu là lá
            if not node.left and not node.right:

                ketqua.append(path)

                return

            path += "->"

            dfs(node.left, path)

            dfs(node.right, path)

        dfs(root, "")

        return ketqua