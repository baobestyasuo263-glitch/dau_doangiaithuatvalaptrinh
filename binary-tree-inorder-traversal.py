class Solution(object):

    def inorderTraversal(self, root):

        ketqua = []

        def dfs(node):

            if not node:
                return

            dfs(node.left)

            ketqua.append(node.val)

            dfs(node.right)

        dfs(root)

        return ketqua