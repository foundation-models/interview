#!/bin/python3

import math
import os
import random
import re
import sys
from unittest import TestCase, main

def reverseShuffleMerge(st):
    candiate = st[:len(st)//2]
    print(candiate)
    




class TestSolution(TestCase):
    
    def test_jump_game(self):
        llist = DoublyLinkedList()
        arr = [1, 2, 3]
        for item in arr:
            llist_item = int(item)
            llist.insert_node(llist_item)
        self.assertEqual(print_doubly_linked_list(llist.head), "3, 2, 1,")

        




class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(str(node.data), end = ', ')
        node = node.next

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    # Write your code here
    head = llist
    while(llist is not None):
        next = llist.next
        llist.next = llist.prev
        llist.prev = next
        head = llist
        llist = next
    return head

if __name__ == "__main__":
    main()