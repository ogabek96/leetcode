"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        queue = deque()
        queue.append((root, 1))
        visited = set()
        res = 0
        while len(queue) > 0:
            node, val = queue.popleft()
            res = val
            if node not in visited:
                for n in node.children:
                    queue.append((n, val + 1))
                visited.add(node)
        return res