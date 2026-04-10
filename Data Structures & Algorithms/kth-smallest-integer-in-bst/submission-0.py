# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(node):
            nonlocal count, result
            
            if not node:
                return
            else:
                search(node.left)
                count += 1
                if count == k:
                    result = node.val
                    return
                search(node.right)

        count, result = 0, 0
        search(root)
        return result
