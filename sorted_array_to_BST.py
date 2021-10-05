from unittest import TestCase, main
from utility import TreeNode

# Definition for a binary tree node.
   
def sorted_array_to_BST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    
    if nums is None or len(nums) == 0:
        return None
    
    node = TreeNode()
    if len(nums) == 1:     
        node.val = nums[0]
        if node.val == None:
            return None
        return node
    
    n = len(nums)
    node.val = nums[n//2]
    node.left = sorted_array_to_BST(nums[:n//2])
    node.right = sorted_array_to_BST(nums[n//2+1:])
    return node
    
class Binary_Search_Tree(object):
    def __init__(self, nums) -> None:
        super().__init__()
        self.root = sorted_array_to_BST(nums)
    
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