from typing import Union, Any

def divrem(a, b):
    """
    >>> divrem(16, 6)
    (2, 4)
    >>> divrem(12, 4)
    (3, 0)
    >>> divrem(3, 0)
    ZeroDivisionError


    """
    assert b != 0
    # if b == 0:
    #     raise ZeroDivisionError
    if a < b:
        return(0, a)
    elif a == b:
        return(1, 0)
    else:
        return (divrem(a-b, b)[0] + 1, a - (divrem(a-b, b)[0] + 1) * b)

class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
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
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s

class LinkedList:
    """
    Collection of LinkedListNodes

    === Attributes ==
    front - first node of this LinkedList
    back - last node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Create an empty linked list.
        """
        self.front, self.back, self.size = None, None, 0

    def __str__(self) -> str:
        """
        Return a human-friendly string representation of
        LinkedList self.

        >>> lnk = LinkedList()
        >>> print(lnk)
        Empty!
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->| Size: 1
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "Empty!"
        else:
            # use front.__str__() if this list isn't empty
            return str(self.front) + " Size: {}".format(self.size)

    def append(self, value: object) -> None:
        """
        Insert a new LinkedListNode with value after self.back.

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        # create the new node
        new_node = LinkedListNode(value)
        # if the list is empty, the new node is front and back
        if self.size == 0:
            assert self.back is None and self.front is None, "ooops"
            self.front = self.back = new_node
        # if the list isn't empty, front stays the same
        else:
            # change *old* self.back.next_ first!!!!
            self.back.next_ = new_node
            self.back = new_node
        # remember to increase the size
        self.size += 1

    def repeat_items(self) -> None:
        """
        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.append(9)
        >>> lnk.append(9)
        >>> lnk.repeat_items()
        >>> print(lnk)
        1 -> 1 -> 0 -> 0 -> 9 -> 9 -> 9 -> 9 ->|
        """
        self.size *= 2
        current = self.front
        while current:
            ori_next = current.next_
            current.next_ = LinkedListNode(current.value, ori_next)
            current = current.next_
            current.next_ = ori_next
            if current.next_ is None:
                self.back = current
            current = ori_next


class BTNode:
    """Binary Tree node.

    data - data this node represents
    left - left child
    right - right child
    """
    data: object
    left: Union["BTNode", None]
    right: Union["BTNode", None]

    def __init__(self, data: object,
                 left: Union["BTNode", None]=None,
                 right: Union["BTNode", None]=None) -> None:
        """
        Create BTNode (self) with data and children left and right.

        An empty BTNode is represented by None.

        """
        self.data, self.left, self.right = data, left, right

def make_full(root):
    """
    >>> make_full(BTNode(10, BTNode(30, BTNode(50, None, None), None), BTNode(40, None, None)))
    1
    """
    if (not root.left) and (not root.right):
        return 0
    else:
        if not root.left:
            return 1 + make_full(root.right)
        if not root.right:
            return 1 + make_full(root.left)
        else:
            return make_full(root.left) + make_full(root.right)






if __name__ == 'main':
    import doctest
    doctest.testmod()

