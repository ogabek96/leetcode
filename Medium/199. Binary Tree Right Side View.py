# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        hmap = {}
        def DFS(t, level):
            if t == None:
                return t
            hmap[level] = t.val
            DFS(t.left, level + 1)
            DFS(t.right, level + 1)
        DFS(root, 1)
        return hmap.values()