from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        visited = set()
        queue = deque()
        queue+= [(root, 0)]
        deepNodes = []
        maxDep = 0
        res = 0
        while len(queue) > 0:
            node, dep = queue.popleft()
            maxDep = max(maxDep, dep)
            if node.left == None and node.right == None:
                deepNodes.append((node, dep))
            if node not in visited:
                if node.left != None:
                    queue+=[(node.left, dep + 1)]
                if node.right != None:
                    queue+=[(node.right, dep + 1)]
                visited.add((node, dep))
        for node, dep in deepNodes:
            if dep == maxDep:
                res+=node.val
        return res