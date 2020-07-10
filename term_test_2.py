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

def contains_satisfier(list_, predicate):
    """
    Return whether possibly-nested list_ contains a non-list element
    that satisfies (returns True for) predicate.
    @param list list_: list to check for predicate satisfiers
    @param (object)->bool predicate: boolean function
    @rtype: bool
    >>> list_ = [5, [6, [7, 8]], 3]
    >>> def p(n): return n > 7
    >>> contains_satisfier(list_, p)
    True
    >>> def p(n): return n > 10
    >>> contains_satisfier(list_, p)
    False
    """
    for ele in list_:
        if not isinstance(ele, list):
            if predicate(ele):
                return True
        else:
            return any([contains_satisfier(ele, predicate)])

    def count_odd_above(t, n):
        """
        Return the number of nodes with depth less than n that have odd values.
        Assume t’s nodes have integer values.
        @param Tree t: tree to list values from
        @param int n: depth above which to list values
        @rtype: int
        >>> t1 = Tree(4)
        >>> t2 = Tree(3)
        >>> t3 = Tree(5, [t1, t2])
        >>> count_odd_above(t3, 1)
        1
        """
        depth = 0
        if t.children == []:
            if t.value % 2 == 0:
                return 1
            else:
                return 0
            depth += 1
        else:
            return sum([count_odd_above(c, n)
                        for c in t.children
                        if depth <= n])




if __name__ == "__main__":
    import doctest
    doctest.testmod()
