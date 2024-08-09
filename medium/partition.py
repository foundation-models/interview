from typing import List, Optional
from unittest import main, TestCase


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # scan all of nodes
        current = head
        before = None
        after = None
        head_after = None
        head_before = head
        while(current):
            if current.val < x:
                if before:
                    before.next = current
                else:
                    head_before = current
                before = current
                if after:
                    after.next = current.next
            else:
                if not after:
                    head_after = current
                after = current
            current = current.next
        if before and head_after:
            before.next = head_after
        return head_before
        
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
    assert(x.partition(head = get_liked_node([1,4,3,2,5,2]), x = 3) == [])
    assert(x.partition(head = get_liked_node([1,2,3,4,5]), k = 2) == [])
    assert(x.partition(head = get_liked_node([0,1,2,3,4,5]), k = 6) == [])
    # assert(x.merge([0], 1, [1], 1) == [1])
    assert(x.maxProfit([7,1,5,3,6,4]) == 7)

