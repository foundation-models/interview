from unittest import TestCase, main

from utility import LinkedList, TreeNode, list_to_linked_list


# Class to convert the linked list to Binary Tree
class ListToBST:
 
    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, list):
        self.head = list_to_linked_list(list).head
        self.root = None
 
    def push(self, new_data):
 
        # Creating a new linked list node and storing data
        new_node = LinkedList(new_data)
 
        # Make next of new node as head
        new_node.next = self.head
 
        # Move the head to point to new node
        self.head = new_node
 
    def convertList2Binary(self):
 
        # Queue to store the parent nodes
        q = []
 
        # Base Case
        if self.head is None:
            self.root = None
            return
 
        # 1.) The first node is always the root node,
        # and add it to the queue
        self.root = TreeNode(val = self.head.data)
        q.append(self.root)
 
        # Advance the pointer to the next node
        self.head = self.head.next
 
        # Until th end of linked list is reached, do:
        while(self.head):
 
            # 2.a) Take the parent node from the q and
            # and remove it from q
            parent = q.pop(0) # Front of queue
 
            # 2.c) Take next two nodes from the linked list.
            # We will add them as children of the current
            # parent node in step 2.b.
            # Push them into the queue so that they will be
            # parent to the future node
            leftChild= None
            rightChild = None
 
            if self.head.data is not None:
                leftChild = TreeNode(self.head.data)
                q.append(leftChild)
            self.head = self.head.next
            if(self.head):
                if self.head.data is not None:
                    rightChild = TreeNode(self.head.data)
                    q.append(rightChild)
                self.head = self.head.next
 
            #2.b) Assign the left and right children of parent
            parent.left = leftChild
            parent.right = rightChild
        return self.root

def convertArr(head):
 
    # Create an array of the
    # required length
    arr = []
    curr = head
 
    # Traverse the Linked List and add the
    # elements to the array one by one
    while (curr != None):
        arr.append( curr.data)
        curr = curr.next
    return arr
 
def removeNthFromEnd(head, n):
        keep_head = head
        for i in range(n):
            head = head.next
            if head is None and i < n-1:
                return keep_head
        if head == None:
            return keep_head.next
        candidate = keep_head
        while(head.next is not None):
            candidate = candidate.next
            head = head.next
        candidate.next = candidate.next.next
        return keep_head
    

class TestPractice(TestCase):
    
    def test_list_to_BST(self):
        self.assertEqual(convertArr(removeNthFromEnd(list_to_linked_list([1,2,3,4,5]).head, 2)),[1,2,3,5])
        self.assertEqual(convertArr(removeNthFromEnd(list_to_linked_list([1]).head, 1)),[])
        self.assertEqual(convertArr(removeNthFromEnd(list_to_linked_list([1,2]).head, 1)),[1])
        self.assertEqual(convertArr(removeNthFromEnd(list_to_linked_list([1,2]).head, 2)),[2])
        self.assertEqual(convertArr(removeNthFromEnd(list_to_linked_list([1,2]).head, 3)),[1,2])



if __name__ == "__main__":
    main()