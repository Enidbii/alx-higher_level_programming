#!/usr/bin/python3
""" Node module """


class Node:
    """ declares and defines node attributes """
    def __init__(self, data, next_node=None) -> None:
        """
        initializes the attributes

        Args:
            data: data to the list
            next_node: the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ defines data to be retrieved """
        self.__data = data

    @data.setter
    def data(self, value):
        """
        sets data values

        Args:
            value: data value of the node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ defines next node to be retrieved """
        self.__next_node = next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets the next node value

        Args:
            value: next node value
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ defines a class of singly linked lists attributes """
    def __init__(self) -> None:
        """ Initializes attribute of the class """
        self.__head = None

    def __str__(self) -> str:
        """ returns string to be printed for SinglyLinkedList """
        output = list()
        future = self.__head

        while future is not None:
            output.append(str(future.data))
            future = future.next_node

        return "\n".join(output)

    def sorted_insert(self, value):
        """
        Sorts the node values
        Args:
            value: value of node
        """
        if self.__head is None:
            self.__head = Node(value)
            return

        if value < self.__head.data:
            self.__head = Node(value, self.__head)  # beginning of node
            return

        future, past = self.__head.next_node, self.__head
        while future is not None:
            if value < future.data:
                past.next_node = Node(value, future)    # middle of node
                return
            past = future
            future = future.next_node
        past.next_node = Node(value)    # end of node
