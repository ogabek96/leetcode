# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return ''
        res = []
        def dfs(t, path):
            if t.left == None and t.right == None:
                res.append(path)
                return t
            if t.left:
                dfs(t.left, path + '->' + str(t.left.val))
            if t.right:
                dfs(t.right, path + '->' + str(t.right.val))
        dfs(root, str(root.val))
        return res