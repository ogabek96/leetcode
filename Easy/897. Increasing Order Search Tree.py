# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.newNode = TreeNode(-1)
        self.currNode = self.newNode
        def fillInOrder(curr):
            if curr.left != None:
                fillInOrder(curr.left)
            self.currNode.right = TreeNode(curr.val)
            self.currNode = self.currNode.right
            if curr.right != None:
                fillInOrder(curr.right)               
        fillInOrder(root)
        return self.newNode.right