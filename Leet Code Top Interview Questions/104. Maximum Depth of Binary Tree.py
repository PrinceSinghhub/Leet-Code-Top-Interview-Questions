class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        Left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(Left, right) + 1