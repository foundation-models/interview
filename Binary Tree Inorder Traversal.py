# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traverse(result, node):
            if node is None:
                return result
            if node.left is None and node.right is None:
                result.append(node.val)
                return result
            traverse(result, node.left)
            result.append(node.val)
            return traverse(result, node.right)
        print(root)
        if root is None:
            return []
        result = []
        return traverse(result, root)