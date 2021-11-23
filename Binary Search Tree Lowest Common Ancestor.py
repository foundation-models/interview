from unittest import TestCase, main

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 
    
    
    def __repr__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def lca(root, v1, v2):
    
    # Base Case
    if root is None:
        return None
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
    return root    
    

def solution(arr, v1, v2):
    tree = BinarySearchTree()
    for i in range(len(arr)):
        tree.create(arr[i])
    return lca(tree.root, v1, v2).info


class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([4,2,3,1,7,6], 1, 7),4)
        self.assertEqual(solution([2,1,4,3,5,6], 3, 6),4)


if __name__ == "__main__":
    main()