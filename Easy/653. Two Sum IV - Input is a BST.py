# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            arr.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        left = 0
        right = len(arr) - 1
        while left < right:
            sum = arr[left] + arr[right]
            if sum == k:
                return True
            if sum < k:
                left+=1
            else:
                right-=1
        return False