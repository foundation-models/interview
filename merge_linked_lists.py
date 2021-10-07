from unittest import TestCase, main

from list_to_BST import list_to_linked_list
from utility import LinkedList

def merge_sorted_x(list1, list2):
    result = LinkedList()
    merged_head = merge_sorted(list1.head, list2.head)
    result.head = merged_head
    return result
    

def merge_sorted(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    tmp = None
    if head1.data <= head2.data:
        tmp = head1
        tmp.next = merge_sorted(head1.next, head2)
    else:
        tmp = head2
        tmp.next = merge_sorted(head1, head2.next)
    return tmp
    
    

def inject_l1_after_l2(l1, l2):
    l2_next = l2.head.next
    l2.head.next = l1
    l1.head = l2.head
    l1_next = l1.head.next
    if l1_next:
        l1_next.head = l1_next
    if l2_next:
        l1.head.next = l2_next
    return l1_next, l2.head.next

def inject_l1_before_l2(l1, l2):
    l1_next = l1.head.next
    l1.head.next = l2
    l2.head = l1
    if l1_next:
        l1_next.head = l1_next
    return l1_next, l2


def absorb(l1, result):
    print(l1)
    print(result)
    while l1 is not None and result is not None:
        if l1.head.data >= result.head.data and (result.head.next is None or l1.head.data <= result.head.next.head.data):
            l1, result = inject_l1_after_l2(l1, result)
            print(l1)
            print(result)
            print(result.head.data)
        elif l1.head.data < result.head.data:
            l1, result = inject_l1_before_l2(l1, result)
            print(l1)
            print(result)
        else:
            head = result.head
            result = result.head.next
            result.head = head
    return result
        


def matrix_to_linked_lists(lists):
    result = []
    for list in lists:
        result.append(list_to_linked_list(list)) 
    return result

def test_merge_k_lists(lists):
    tmp = lists[0]
    for n in range(1,len(lists)):
        tmp = merge_sorted_x(lists[n], tmp)
        print(tmp)
    return tmp

class TestSolution(TestCase):
    def test_merge_k_lists(self):
        expected = list_to_linked_list([1,1,2,3,4,4,5,6])
        print(expected)
        self.assertEqual(test_merge_k_lists( matrix_to_linked_lists([[1,4,5],[1,3,4],[2,6]]) ), expected)
        

if __name__ == "__main__":
    main()
