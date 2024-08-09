from typing import List, Optional
from unittest import main, TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        
        current = new_head = head
        while(current.next):
            new_head = x = current.next
            for i in range(k):
                if x.next is None:
                    x.next = head
                    for j in range(k-i-1):
                        current = new_head
                        new_head = current.next
                    current.next = None                         
                    return new_head
                else:
                    x = x.next
            current = current.next

        return new_head
        
def get_liked_node(l: list):
     x = None
     for i in range(len(l)):
        if x:
            x.next = ListNode(l[i])
            x = x.next
        else:
            x = ListNode(l[i])
            head = x      
     return head
        
if __name__ == "__main__":
    x = Solution()
    assert(x.rotateRight(head = get_liked_node([0,1,2]), k = 4) == [])
    assert(x.rotateRight(head = get_liked_node([1,2,3,4,5]), k = 2) == [])
    assert(x.rotateRight(head = get_liked_node([0,1,2,3,4,5]), k = 6) == [])
    # assert(x.merge([0], 1, [1], 1) == [1])
    assert(x.maxProfit([7,1,5,3,6,4]) == 7)

