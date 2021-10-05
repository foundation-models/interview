from unittest import TestCase, main

from utility import TreeNode

def list_to_list_node(list1):
    head = ListNode(list1[0])
    tail = head
    index = 1
    while index < len(list1):
      tail.next = ListNode(list1[index])
      tail = tail.next
      index += 1
    
    return head
 
 
# Linked List node
class ListNode:
 
        # Constructor to create a new node
        def __init__(self, data):
            self.data = data
            self.next = None
 
 
# Class to convert the linked list to Binary Tree
class ListToBST:
 
    # Constructor for storing head of linked list
    # and root for the Binary Tree
    def __init__(self, list):
        self.head = list_to_list_node(list)
        self.root = None
 
    def push(self, new_data):
 
        # Creating a new linked list node and storing data
        new_node = ListNode(new_data)
 
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


class TestPractice(TestCase):
    
    def test_list_to_BST(self):
        conversion = ListToBST([5,1,4,None,None,3,6])
        print(conversion.convertList2Binary())



if __name__ == "__main__":
    main()