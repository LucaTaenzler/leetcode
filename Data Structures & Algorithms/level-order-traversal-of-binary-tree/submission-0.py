# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque()
        stack.append(root)
        result = list()

        if not root:
            return list()

        while stack:
            sublist = list()
            for _ in range(len(stack)):
                temp = stack.popleft()
                sublist.append(temp.val)

                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)

            result.append(sublist)
        
        return result
