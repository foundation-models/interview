from unittest import TestCase, main

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sorted_array_to_BST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    
    if nums is None or len(nums) == 0:
        return None
    
    node = TreeNode()
    if len(nums) == 1:     
        node.data = nums[0]
        return node
    
    n = len(nums)
    node.data = nums[n//2]
    node.left = sorted_array_to_BST(nums[:n//2])
    node.right = sorted_array_to_BST(nums[n//2+1:])
    return node
    
class Binary_Search_Tree(object):
    def __init__(self, nums) -> None:
        super().__init__()
        self.root = sorted_array_to_BST(nums)
    

        
        
class TreeNode:
    def __init__(self) -> None:
        self.data = None
        self.left = None
        self.right = None  
        
    def __str__(self) -> str:
        if self.left is None and self.right is None:
            return "{} data: {} {}".format('{', self.data or "-", '}') 
        return "{} data: {}, left: {}, right: {} {}".format('{', self.data, self.left or "-", self.right or "-", '}')      

class TestPractice(TestCase):
    
    def test_sorted_array_to_BST(self):
        print(Binary_Search_Tree([]).root)
        print(Binary_Search_Tree([1]).root)
        print(Binary_Search_Tree([1,2]).root)
        print(Binary_Search_Tree([1,2,3,4,5,6,7]).root)
        print(Binary_Search_Tree([1,2,3,4,5,6]).root)
        print(Binary_Search_Tree([2,8,12,15,22,35,56,78]).root)


if __name__ == "__main__":
    main()