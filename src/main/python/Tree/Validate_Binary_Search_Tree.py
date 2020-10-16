# Created by Jiehan Zhu at 10/16/20
"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
from src.main.python.utility.tree import TreeNode, initialTree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        print(f'root = {root}')
        if not root or (not root.left and not root.right):
            return True
        if not root.left:
            if root.right.val <= root.val:
                return False
            else:
                return self.isValidBST(root.right)
        if not root.right:
            if root.left.val >= root.val:
                return False
            else:
                return self.isValidBST(root.left)
        if root.left.val >= root.val or root.right.val <= root.val:
            return False
        return all([self.isValidBST(root.left), self.isValidBST(root.right)])