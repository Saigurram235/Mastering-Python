#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    # if head == None:
    #     return Node(data, None)
    # else:
    #     if head.next == None:
    #         head.next = Node(data,None)
    #     else:
    #         insertNodeAtTail(head.next,data)
    #     return head
    sys.setrecursionlimit(1000000) #It the value of integer type that denotes the new limit of python interpreter stack.
    if head == None:
        return SinglyLinkedListNode(data)
    else:
        if head.next == None:
            head.next = SinglyLinkedListNode(data)
        else:
            insertNodeAtTail(head.next,data)
    return llist.head
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
