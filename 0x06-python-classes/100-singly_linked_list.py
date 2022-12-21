#!/usr/bin/python3
"""

This is the "Single Linked List" module.

Class Node takes in integer values as data within each node,
and a next attribute which points to the next node or to None.

Class SinglyLinkedList initializes a default head of None.
Method sorted_insert handles all nodes created and adds them to
the linked list sorted by the int value stored within.

"""


class Node:
    """A class that creates a single Node in a Linked List.
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        if not type(self.__data) is int:
            raise TypeError("data must be an integer")
        self.__next_node = next_node
        if not type(self.__next_node) is Node\
            and type(self.__next_node) is None:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not type(value) is int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not type(value) is Node and type(value) is None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A class that creates a Singly Linked List.
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        listd = []
        while current != None:
            listd.append(current.data)
            current = current.next_node
        result = '\n'.join(str(i) for i in listd)
        return result

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        elif value <= self.__head.data:
            node = self.__head
            self.__head = Node(value, node)
        else:
            current = self.__head
            while current.next_node != None:
                prev = current
                current = current.next_node
                if value <= current.data and prev.data < value:
                    node = current
                    current = Node(value, node)
                    prev.next_node = current
                    break
            if current.next_node is None:
                current.next_node = Node(value)
