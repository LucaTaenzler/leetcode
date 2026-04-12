# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def search(root):
            if not root:
                return 0

            leftMax = max(search(root.left), 0)
            rightMax = max(search(root.right), 0)

            nonlocal result
            result = max(root.val + leftMax + rightMax, result)

            return root.val + max(leftMax, rightMax)

        result = root.val
        search(root)
        return result
