class Solution(object):

    def sumOfLeftLeaves(self, root):

        if not root:
            return 0

        tong = 0

        # Nếu có lá trái
        if root.left and not root.left.left and not root.left.right:

            tong += root.left.val

        tong += self.sumOfLeftLeaves(root.left)

        tong += self.sumOfLeftLeaves(root.right)

        return tong