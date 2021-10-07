from unittest import TestCase, main
import sys

from list_to_BST import ListToBST
from utility import TreeNode

def list_to_BST(list):
    return ListToBST(list).convertList2Binary()

def isValidBinarySearchTree(root, min, max):
    if root is None:
        return True
    elif root.val <= min or root.val >= max:
            return False
    else:
        is_left_BST = is_right_BST = True
        if root.left is not None:
            is_left_BST = isValidBinarySearchTree(root.left, min, root.val)
        if root.right is not None:
            is_right_BST = isValidBinarySearchTree(root.right, root.val, max)
        return is_left_BST and is_right_BST
            
def isValidBST(root):
    return isValidBinarySearchTree(root, float('-inf'), float('inf'))
        
class TestPractice(TestCase):
    
    def test_is_valis_BST(self):
        self.assertTrue(isValidBST( list_to_BST([5,1,7,None,None,6,9])))
        self.assertFalse(isValidBST( list_to_BST([5,1,6,None,None,8,9])))
        self.assertFalse(isValidBST(list_to_BST([5,1,4,None,None,3,6])))


if __name__ == "__main__":
    main()