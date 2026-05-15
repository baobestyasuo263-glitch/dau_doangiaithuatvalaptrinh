class Solution(object):

    def preorderTraversal(self, root):

        ketqua = []

        def dfs(node):

            if not node:
                return

            ketqua.append(node.val)

            dfs(node.left)

            dfs(node.right)

        dfs(root)

        return ketqua