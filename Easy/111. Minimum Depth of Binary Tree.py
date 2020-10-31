# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        left = self.minDepth(root.left) if root.left != None else sys.maxsize
        right = self.minDepth(root.right) if root.right != None else sys.maxsize
        return min(left, right) + 1