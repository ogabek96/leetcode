# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        minVal = 10**5 + 1
        for i in range(len(res) - 1):
            minVal = min(minVal, abs(res[i + 1] - res[i]))
        return minVal