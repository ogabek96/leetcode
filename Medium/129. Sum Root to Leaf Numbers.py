# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        def dfs(root, num):
            if root.left == None and root.right == None:
                res.append(num*10 + root.val)
                return root
            if root.left:
                dfs(root.left, num * 10 + root.val)
            if root.right:
                dfs(root.right, num * 10 + root.val)
        dfs(root, 0)
        return sum(res)