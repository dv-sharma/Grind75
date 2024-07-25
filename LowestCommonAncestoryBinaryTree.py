# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r

##STEPS
'''
If the root is empty return the root
If the root is equal to the left or right node whose common ancestor we have to find, return the root

Call this function with .self on the left and right children nodes
If both left and right come non empty:
It means the root is the ancestor
Else
either left node contains both p & q so return left, or return right
'''


