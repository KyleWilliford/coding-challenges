"""
Created by Jiehan Zhu at 10/17/20

Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
from src.main.python.utility.tree import TreeNode, initial_tree


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        ind = len(nums) // 2
        node = TreeNode(nums[ind])
        node.left = self.sortedArrayToBST(nums[:ind])
        node.right = self.sortedArrayToBST(nums[ind+1:])
        return node