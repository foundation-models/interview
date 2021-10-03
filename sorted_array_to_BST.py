from unittest import TestCase, main

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
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
        node.left = self.sortedArrayToBST(nums[:n//2])
        node.right = self.sortedArrayToBST(nums[n//2+1:])
        return node
        
        
        
class TreeNode:
    def __init__(self) -> None:
        self.data = None
        self.left = None
        self.right = None  
        
    def __str__(self) -> str:
        if self.left is None and self.right is None:
            return "{} data: {} {}".format('{', self.data or "-", '}') 
        return "{} data: {}, left: {}, right: {} {}".format('{', self.data or "-", self.left or "-", self.right or "-", '}')      

class TestPractice(TestCase):
    
    def test_sorted_array_to_BST(self):
        ob1 = Solution()
        print(ob1.sortedArrayToBST([]))
        print(ob1.sortedArrayToBST([1]))
        print(ob1.sortedArrayToBST([1,2]))
        print(ob1.sortedArrayToBST([1,2,3,4,5,6,7]))
        print(ob1.sortedArrayToBST([1,2,3,4,5,6]))
        print(ob1.sortedArrayToBST([2,8,12,15,22,35,56,78]))


if __name__ == "__main__":
    main()