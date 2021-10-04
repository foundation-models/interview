from unittest import TestCase, main
from sorted_array_to_BST import Binary_Search_Tree

def sum_tree_leaf(root):
    sum = 0
    if root == None:
        return None
    if root.left == None and root.right == None:
        return root.data
    if root.left is not None:
        sum += sum_tree_leaf(root.left)
    if root.right is not None:
        sum += sum_tree_leaf(root.right)
    return sum
    
class TestSolution(TestCase):
    
    def test_solution(self):
        root = Binary_Search_Tree([-6,-4,0,1,2,3,5,7,8,9]).root
        print(root)
        self.assertEqual(sum_tree_leaf(root), 9)
        


if __name__ == "__main__":
    main()