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
        self.tail = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    if llist is None:
        llist = SinglyLinkedListNode(data)
        llist.next = None
    elif llist.next is None:
        llist.next = SinglyLinkedListNode(llist.data)
        llist.data = data
    elif llist.next.next is None:
        llist.next.next = SinglyLinkedListNode(llist.next.data)
        llist.next.data = llist.data
        llist.data = data
    elif llist.next.next.next is None:
        llist.next.next.next = SinglyLinkedListNode(llist.next.next.data)
        llist.next.next.data = llist.next.data
        llist.next.data = llist.data
        llist.data = data
    else:
        llist.next = insertNodeAtHead(llist.next, llist.data)
        llist.data = data

    return llist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()


