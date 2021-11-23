from unittest import TestCase, main

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
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

def height(root):
    if root is None:
        return -1
    return max(height(root.left) + 1, height(root.right) + 1)
    
    

def solution(arr):
    tree = BinarySearchTree()
    for i in range(len(arr)):
        tree.create(arr[i])
    return height(tree.root)


class TestSolution(TestCase):
    
    def test_solution(self):
        self.assertEqual(solution([4,2,6,1,3,5,7]),2)
        self.assertEqual(solution([3,2,5,1,4,6,7]),3)
        self.assertEqual(solution([3,2,5,1,2,4,6,7]),3)

if __name__ == "__main__":
    main()