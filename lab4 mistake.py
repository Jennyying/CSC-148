"""
Read over the very-abbreviated LinkedListNode and LinkedList class declarations
below.  Then implement the body of copy (look for the TODO),
which must run with only the code below.

If you are writing this on paper, please provide your:

Name:

utorid:
"""
from typing import Union


class LinkedListNode:
    """
    Node to be used in linked list

    next_ - successor to this LinkedListNode
    value - data this LinkedListNode represents
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
        next_: Union["LinkedListNode", None]=None) -> None:
        """
        Create LinkedListNode self with data value and successor next_.
        """
        self.value, self.next_ = value, next_

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        s = "{} ->".format(self.value)
        current_node = self.next_
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        return s + "|"


class LinkedList:
    """
    Collection of LinkedListNodes

    front - first node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Create an empty linked list.
        """
        self.front, self.size = None, 0

    def copy(self) -> "LinkedList":
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        >>> lnk = LinkedList()
        >>> lnk.front = LinkedListNode(3, None) # Insert in reverse
        >>> lnk.front = LinkedListNode(2, lnk.front)
        >>> lnk.front = LinkedListNode(1, lnk.front) # lnk.front has value 1 now
        >>> print(lnk.copy())
        1 -> 2 -> 3 ->|
        >>> lnk.copy() is lnk # you must create a COPY and not return 'self'
        False
        >>> lnk.copy().front is lnk.front # all nodes are copied as well.
        False
        """
        # TODO: implement the body of this method.
        # You need not touch any other code than the body of this method
        # You need not add comments or docstrings.
        # You need not add any assertions or preconditions.
        new = LinkedList()
        current = self.front
        while current != None:
            new.front = LinkedListNode(current.value, current.next_)
            current = current.next_
            new.size += 1
        return new
