# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumOfLeaves = 0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                self.sumOfLeaves+= root.left.val
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)      
        return self.sumOfLeaves