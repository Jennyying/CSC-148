from typing import Union
import copy

class HelpQueueEntry:
    """
    Represent one entry in the help queue
    """
    def __init__(self, name, number, course='') -> None:
        self.name, self.number, self.course = name, number, course


class HelpQueue:
    """
    A class to represent a help queue
    """
    def __init__(self):
        self.helpqueue = []
        self.next_number = -1

    def process_swipe(self, name: str, course: str=''):
        for stu in self.helpqueue:
            if stu.name == name:
                return stu.number
        self.next_number += 1
        self.helpqueue.append(HelpQueueEntry(name, self.next_number, course))
        return self.next_number

    def get_next_student(self, course=''):
        if course != '':
            for stu in self.helpqueue:
                if stu.course == course:
                    # num = stu.number
                    self.helpqueue.remove(stu)
                    return stu
            else:
                return None
        else:
            if len(self.helpqueue) != 0:
                nxt = self.helpqueue[0]
                self.helpqueue.remove(nxt)
                return nxt


def width(list_, max_depth):
    """
    >>> list_ = [0,1]
    >>> width(list_, 1)
    2
    >>> list_ = [[0, 1], 2, [3, [[], 4]]]
    >>> width(list_, 4)
    4
    """
    new = []
    # num = count_at_depth(list_, 1)
    for i in range(1, max_depth + 1):
        new.append(count_at_depth(list_, i))
    #     if count_at_depth(list_, i) > num:
    #         num = count_at_depth(list_, 1)
    # return num
            # print(num)
    return max(new)


def count_at_depth(list_, depth) -> int:
    """
    >>>
    """
    if depth == 1:
        return len(list_)
    else:
        return sum([count_at_depth(sub, depth - 1) for sub in list_
                    if isinstance(sub, list)])

class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        # copy children if not None
        self.children = children[:] if children is not None else []


def prune(t, predicate):
    """
    >>> t1 = Tree(6, [Tree(8), Tree(9)])
    >>> t2 = Tree(4, [Tree(11), Tree(10)])
    >>> t3 = Tree(7, [Tree(3), Tree(12)])
    >>> t = Tree(5, [t1, t2, t3])
    >>> t3_pruned = Tree(7, [Tree(12)])
    >>> def predicate(v): return v > 4
    >>> prune(t, predicate)
    Tree(5, t1, t3_pruned])
    """
    if not predicate(t.value):
        return None
    else:
        return Tree(t.value, [prune(c, predicate) for c in t.children if prune(c, predicate) is not None])


if __name__ == '__main__':
    hq = HelpQueue()
    assert hq.process_swipe
    assert hq.process_swipe('Amy', 'CSC108') == 0
    assert hq.process_swipe('Bo') == 1
    assert hq.process_swipe('Chen', 'CSC148') == 2
    assert hq.process_swipe('Amy') == 0
    assert hq.get_next_student('CSC148').number == 2
    assert hq.get_next_student('CSC148') is None
    assert hq.get_next_student('CSC165') is None
    assert hq.get_next_student().number == 0
    assert hq.get_next_student().number == 1
    assert hq.get_next_student() is None

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
        if next_ is not None:
            self.skip = next_.next_
        else:
            self.skip = None

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
        5 ->|
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "Empty!"
        else:
            # use front.__str__() if this list isn't empty
            return str(self.front)

    def precursors(self, value):
        """
       >>> lnk = LinkedList()
       >>> lnk.precursors(3)
       (None, None)
       >>> a = LinkedListNode(3)
       >>> lnk.front, lnk.back, lnk.size = a, a, 1
       >>> lnk.precursors(1)
       (None, None)
       >>> b = LinkedListNode(1, a)
       >>> lnk.front, lnk.size = b, 2
       >>> lnk.precursors(5)
       (1, 3)
        """
        if not self.front and not self.back:
            return (None, None)
        new = []
        current = self.front
        while current:
            if current.value < value:
                new.append(current.value)
            current = current.next_
        # print(new)
        if len(new) > 0:
            a = max(new)
            new.remove(a)
            if len(new) > 0:
                return (max(new), a)
            else:
                return (None, a)
        else:
            return (None, None)
    def insert(self, value, prev, cur):
        """
        >>> lnk = LinkedList()
        >>> lnk.insert(3, lnk.precursors(3)[0], lnk.precursors(3)[1])
        >>> lnk.insert(0, lnk.precursors(0)[0], lnk.precursors(0)[1])
        >>> lnk.insert(2, lnk.precursors(2)[0], lnk.precursors(1)[1])
        >>> print(lnk.front)
        0 -> 1 -> 2 -> 3 ->|
        >>> print(lnk.back)
        3 ->|
        >>> lnk.size
        4
        >>> print(lnk.front.skip)
        2 -> 3 ->|
        >>> print(lnk.front.next_.skip)
        3 ->|
        """
        current = self.front
        while current is not None:
            if current == cur:
                ori_next = current.next_
                current.next_ = LinkedListNode(value, ori_next)
                break
            current = current.next_
            self.size += 1
        if current is None:
            ori = self.front
            self.front = LinkedListNode(value, ori)
            if self.back is None:
                self.back = LinkedListNode(value, ori)
        # else:
        #     ori_next = current.next_
        #     current.next_ = LinkedListNode(value, ori_next)

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


def merge(listl, list2):
    """
    >>> listl =LinkedList()
    >>> listl.append(1)
    >>> listl.append(3 )
    >>> listl.append(5 )
    >>> list2 = LinkedList()
    >>> list2.append(2)
    >>> list2.append(6)
    >>> merge(listl , list2 )
    >>> print(listl.front)
    1 -> 2 -> 3 -> 5 -> 6 ->|
    """
    current1 = listl.front
    current2 = list2.front
    while current2 is not None:
        while current1 is not None:
            if current1.value < current2.value:
                ori_n = current1.next_
                current1.next_ = current2
                current1.next_.next_ = ori_n
                if ori_n is None:
                    listl.back = current1. next_
                    listl.size += 1
            current1 = current1.next_
        current2 = current2.next_

def concatenate_flat(list_):
    """

    :param list_:
    :type list_:
    >>> concatenate_flat(['five', [['four', 'by'], 'three'], ['two']])
    'fourbytwo'
    """
    if all([isinstance(x, str) for x in list_]):
        # return sum([x for x in list_])
        s = ''
        for x in list_:
            # print(x)
            s += x
        return s
    else:
        # return sum([concatenate_flat(x) for x in list_ if isinstance(x, list)])
        st = ''
        for x in list_:
            if isinstance(x, list):
                st += concatenate_flat(x)
        return st
