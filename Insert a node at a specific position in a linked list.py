class Node:
    def __init__(self, dataval=None):
      self.data = dataval
      self.next = None
      
    def __repr__(self) -> str:
        return str(self.data)
      
def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if llist is None or llist.next is None:
        return
    x = Node(data)
    if position == 0:
        first = x
        x.next = llist
    else:
        first = llist
        for i in range(position - 1):
            llist = llist.next
        tmp = llist.next

        llist.next = x
        x.next = tmp
        
        
    xx = first
    print("-----------")
    while xx is not None:
        print(xx)
        xx = xx.next
    return first





if __name__ == '__main__':
    xx = first = None
    for x in [1, 2, 3, 4]:
        y = Node(x)
        if xx is not None:
            xx.next = y
        else:
            first = y
        xx = y
    xx = first
    while xx is not None:
        print(xx)
        xx = xx.next
    insertNodeAtPosition(first, 8, 0)
    insertNodeAtPosition(first, 8, 1)
    insertNodeAtPosition(first, 8, 4)

    
    