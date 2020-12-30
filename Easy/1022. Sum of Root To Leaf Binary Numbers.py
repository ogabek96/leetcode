from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        queue = deque()
        queue+=[(root, str(root.val))]
        res = []
        while len(queue) > 0:
            node, val = queue.popleft()
            if node.left == None and node.right == None:
                res.append(val)
            if node.left != None:
                queue.append((node.left, val + str(node.left.val)))
            if node.right != None:
                queue.append((node.right, val + str(node.right.val)))
        result = 0
        for b in res:
            result+= int(b, 2)
        return result