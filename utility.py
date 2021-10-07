
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            
    def __str__(self) -> str:
        if self.left is None and self.right is None:
            return "{} val: {} {}".format('{', self.val or "-", '}') 
        return "{} val: {}, left: {}, right: {} {}".format('{', self.val, self.left or "-", self.right or "-", '}')   

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)

# Linked List node
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Method to print linked list
    def printList(self):
        temp = self.head
         
        while temp :
            print(temp.data, end="->")
            temp = temp.next
            
    def __str__(self) -> str:
        result = ""
        temp = self.head
         
        while temp :
            result += str(temp.data) + "->"
            temp = temp.next
        return result
    
    def __eq__(self, o: object) -> bool:
        result = True
        temp = self.head
        ohead = o.head
        
        while temp and ohead:
            result = result and (temp.data == ohead.data)
            temp = temp.next
            ohead = ohead.next
        
        if temp is not None or ohead is not None:
            return False
        return result

    # Function to add of node at the end.
    def append(self, new_data):
        new_node = Node(new_data)
         
        if self.head is None:
            self.head = new_node
            return
        last = self.head
         
        while last.next:
            last = last.next
        last.next = new_node 
        
def list_to_linked_list(list):
    if list is None: 
        return None

    result = LinkedList()
    for data in list:
        result.append(data)

    return result
 