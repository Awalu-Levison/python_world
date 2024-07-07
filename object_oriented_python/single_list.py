#!/usr/bin/python3
"""Node of singly-linked list"""


class Node:
    """structure of a node"""

    def __init__(self, data, next_node=None):
        """Initialise the class attributes
        args:
            data(int): Data of the new node
            next_node(mode): Next node of the new node
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Get data of the node"""
            return (self.__data)

        @data.setter
        def data(self, value):
            """Set new data of the node"""
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Access the next node"""
            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""


    def __init__(self):
        """Initialise new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node to the list
        node is inserted at ordered numerdical position
        Args:
            value(int): New node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new

    def __str__(self):
        """Define the print representation of the singly linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
