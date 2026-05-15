class Solution(object):

    def leafSimilar(self, root1, root2):

        def leaves(node, arr):

            if not node:
                return

            if not node.left and not node.right:

                arr.append(node.val)

            leaves(node.left, arr)

            leaves(node.right, arr)

        a = []
        b = []

        leaves(root1, a)
        leaves(root2, b)

        return a == b