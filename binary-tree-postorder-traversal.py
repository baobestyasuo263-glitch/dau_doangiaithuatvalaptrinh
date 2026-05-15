class Solution(object):

    def postorderTraversal(self, root):

        ketqua = []

        def dfs(node):

            if not node:
                return

            dfs(node.left)

            dfs(node.right)

            ketqua.append(node.val)

        dfs(root)

        return ketqua