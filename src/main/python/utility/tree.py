# Created by Jiehan Zhu at 10/16/20

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Create a binary tree based a list of values
def initial_tree(val_list):
    """
    Create a binary tree based a list of values
    :param val_list: List[int]
    :return:
    """
    root = TreeNode(val_list.pop(0))
    currentNodes = [root]
    nextNodes = list()
    i = 0
    while i < len(val_list):
        for node in currentNodes:
            val_left = val_list[i]
            if val_left:
                node.left = TreeNode(val_left)
                nextNodes.append(node.left)
            val_right = val_list[i + 1]
            if val_right:
                node.right = TreeNode(val_right)
                nextNodes.append(node.right)
            i += 2
        currentNodes = nextNodes
        nextNodes = list()
    return root
