"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def traverse(root):
            if not root:
                return root
            for r in root.children:
                traverse(r)
            res.append(root.val)
        traverse(root)
        return res