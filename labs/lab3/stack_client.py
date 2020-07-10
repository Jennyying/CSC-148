import unittest
from stack import Stack


def list_stack(st: Stack, lst: list) -> None:
    """
    Add each element of lst to Stack, then remove it from the top and print it
    """
    for element in lst:
        st.add(element)
    # for sth in st:
    #     if type(sth) == list:
    #         for e in sth:
    #             st.add(e)
    while not st.is_empty():
        # new =[]
        top = st.remove()
        st.add(top)
        if type(top) == list:
            st.remove()
            for item in top:
                st.add(item)
            # st.remove()
        print(st.remove())


if __name__ == "__main__":
    # s = Stack()
    # new = ''
    # while new != 'end':
    #     new = input('Type a string:')
    #     s.add(new)
    # while not s.is_empty():
    #     print(s.remove())
    s = Stack()
    s.add('a')
    l1 = [1, 3, 5]
    l2 = [1, [3, 5], 7]
    l3 = [1, [3, [5, 7], 9], 11]

    list_stack(s, l3)
