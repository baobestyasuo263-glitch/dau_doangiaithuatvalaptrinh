class Solution(object):

    def increasingBST(self, root):

        vals = []

        def inorder(node):

            if not node:
                return

            inorder(node.left)

            vals.append(node.val)

            inorder(node.right)

        inorder(root)

        dummy = TreeNode(0)

        curr = dummy

        for v in vals:

            curr.right = TreeNode(v)

            curr = curr.right

        return dummy.right