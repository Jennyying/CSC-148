""" practice on linked lists
"""
from typing import Union, Any


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

    def __eq__(self, other):
        """
        Return whether LinkedListNode self is equivalent to other.

        @param LinkedListNode self: this LinkedListNode
        @param LinkedListNode|object other: object to compare to self.
        @rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        if type(self) != type(other):
            return False
        current_node = self.next_
        current_node2 = other.next_
        while current_node is not None or current_node2 is not None:
            if not (current_node is not None and current_node2 is not None):
                return False
            if current_node != current_node2:
                return False
            current_node = current_node.next_
            current_node2 = current_node2.next_
        return True


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

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedList self is equivalent to
        other.

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        """
        if type(self) != type(other):
            return False
        return self.size == other.size and self.front == other.front and self.back == other.back

    def delete_after(self, value: object) -> None:
        """
        Remove the node following the first occurrence of value, if
        possible, otherwise leave self unchanged.
        """
        count = 0
        current = self.front
        while current is not None:
            if current.value == value and current != self.back:
                if self.front[count + 1] == self.back:
                    self.back = current
                else:
                    current.next_ = self.front[count + 2]
                self.size -= 1
            current = current.next_
            count -= 1

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

    def prepend(self, value: object) -> None:
        """
        Insert value before LinkedList self.front.

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk[0] = 7
        >>> print(lnk)
        7 ->| Size: 1
        """
        # Create new node with next_ referring to front
        new_node = LinkedListNode(value, self.front)
        # change front
        self.front = new_node
        # if the list was empty, change back
        if self.size == 0:
            self.back = new_node
        # update size
        self.size += 1

    def delete_front(self) -> None:
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """
        assert self.front is not None, "unexpected None!"
        # if back == front, set it to None
        if self.front == self.back:
            self.back = None
        # set front to its successor
        self.front = self.front.next_
        # decrease size
        self.size -= 1

    def __setitem__(self, index: int, value: object) -> None:
        """
        Set the value of list at position index to value. Raise IndexError
        if index >= self.size or index < -self.size

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.__setitem__(1, 1)
        >>> lnk[-1]
        1
        """
        if (-self.size > index
                or index > self.size):
            raise IndexError("out of range!!!")
        elif index < 0:
            index += self.size
        current_node = self.front
        # walk index steps along from 0 to retrieve element
        for _ in range(index):
            assert current_node is not None, "unexpected None!!!!!"
            current_node = current_node.next_
        # return the value at position index
        current_node.value = value

    def __add__(self, other: "LinkedList") -> "LinkedList":
        """
        Return a new list by concatenating self to other.  Leave
        both self and other unchanged.

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> print(lnk1 + lnk2)
        5 -> 7 ->| Size: 2
        """
        new = LinkedList()
        current_node = self.front
        while current_node is not None:
            new.append(current_node.value)
            current_node = current_node.next_
        c_node = other.front
        while c_node is not None:
            new.append(c_node.value)
            c_node = c_node.next_
        return new

    def insert_before(self, value1: object, value2: object) -> None:
        """
        Insert value1 into LinkedList self before the first occurrence
        of value2, if it exists.  Otherwise leave self unchanged.
        """
        current_node = self.front
        count = 0
        # "walk" the linked list
        while current_node is not None:
            if current_node.value == value2:
                self.size += 1
                if count == 0:
                    self.front = LinkedListNode(value1, current_node)
                else:
                    self.front[count - 1].append(LinkedListNode(value1, current_node))
            current_node = current_node.next_
            count += 1

    def copy(self) -> "LinkedList":
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(7)
        >>> print(lnk.copy())
        7 -> 5 ->|
        """

        new = LinkedList()
        current = self.front
        while current is not None:
            new.append(current.value)
            current = current.next_
        return new

    def __len__(self) -> int:
        """
        Return the number of nodes in LinkedList self.
        """
        count = 0
        current = self.front
        while current is not None:
            current = current.next_
            count += 1
        return count

    def __getitem__(self, index: int) -> object:
        """
        Return the value at LinkedList self's position index.

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.__getitem__(1)
        0
        >>> lnk[-1]
        0
        """
        # deal with a negative index by adding self.size
        if (-self.size > index
                or index > self.size):
            raise IndexError("out of range!!!")
        elif index < 0:
            index += self.size
        current_node = self.front
        # walk index steps along from 0 to retrieve element
        for _ in range(index):
            assert current_node is not None, "unexpected None!!!!!"
            current_node = current_node.next_
        # return the value at position index
        return current_node.value

    def __contains__(self, value: object) -> bool:
        """
        Return whether LinkedList self contains value.

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> 2 in lnk
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        # "walk" the linked list
        while current_node is not None:
            # if any node has a value == value, return True
            if current_node.value == value:
                return True
            current_node = current_node.next_
        # if you get to the end without finding value,
        # return False
        return False

    def concat(self, other: 'LinkedList'):
        """
        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(2)
        >>> lnk1.prepend(1)
        >>> lnk1.prepend(0)
        >>> lnk2 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk1.prepend(4)
        >>> lnk1.prepend(3)
        >>> lnk1.concat(lnk2)
        >>> print(lnk1.front)
        0 -> 1 -> 2 -> 3 -> 4 -> 5
        >>> print(lnk2.front)
        None
        """
        if other.size == 0:
            raise Exception
        current = other.front
        while current is not None:
            self.back = (current, current.next_)
            self.back = current.next_
        other.front = None
        other.back = None



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="pylint.txt")
