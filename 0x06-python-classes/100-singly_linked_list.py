#!/usr/bin/python3
""" defining a node class """


class Node:
    """ This class represent a node class

    Attributes:
        data (int): data ofthe node to be sorted and inserted
        next_node (node): nodes to be inserted and sorted

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__nextnode

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__nextnode = value


class SinglyLinkedList:
    """ This class sort lists and the node in the right position

    Atrributes:
        head (node): pointer to the head

    methods:
        sorted_insert(): To sort and insert new node
        __str__: to print new node
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):

        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head

            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node

            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        nodes = []
        temp = self.__head

        while temp:
            nodes.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(nodes))
