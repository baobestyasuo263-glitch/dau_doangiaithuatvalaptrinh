class Solution(object):

    def findMode(self, root):

        dem = {}

        def dfs(node):

            if not node:
                return

            dem[node.val] = dem.get(node.val, 0) + 1

            dfs(node.left)

            dfs(node.right)

        dfs(root)

        maxf = max(dem.values())

        return [k for k in dem if dem[k] == maxf]