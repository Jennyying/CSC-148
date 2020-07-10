# === Quicksort 2 === #
def _partition_2(list_: list, i: int, j: int) -> int:
    """Rearrange list_[i:j] so that items < list_[i] are at
    the beginning and items >= list_[i] are at the end,
    and return the new index for list_[i].

    >>> _partition_2([1, 5, 2, 4, 3], 1, 4)
    3
    """
    v = list_[i]
    k = i + 1
    j -= 1
    while k <= j:
        if list_[k] < v:
            k += 1
        else:
            list_[k], list_[j] = list_[j], list_[k]
            j -= 1
    list_[i], list_[j] = list_[j], list_[i]
    return j


def _quicksort_2(list_: list, i: int, j: int) -> None:
    """
    Sort list_[i:j] by partitioning it around the first item,
    then recursing.
    """
    if i < j:
        pivot = _partition_2(list_, i, j)
        _quicksort_2(list_, i, pivot)
        _quicksort_2(list_, pivot + 1, j)


def quicksort_2(list_: list) -> None:
    """
    Sort list list_ in non-decreasing order.
    """
    _quicksort_2(list_, 0, len(list_))

# === Mergesort 2 === #
def _merge_2(list_: list, i: int, mid: int, j: int) -> list:
    """
    Merge the two sorted halves list_[i:mid + 1] and
    list_[mid + 1:j + 1] and return them in a new list.
    Notice that list_[mid] belongs in the left half and list_[j]
    belongs in the right half -- the indices are inclusive.

    >>> _merge_2([1, 3, 5, 2, 4, 6], 0, 2, 5)
    [1, 2, 3, 4, 5, 6]
    """
    result = []
    left = i
    right = mid + 1
    # Done when left > mid or when right > j; i.e.,
    # when we've finished one of the halves.
    while left <= mid and right <= j:
        if list_[left] < list_[right]:
            result.append(list_[left])
            left += 1
        else:
            result.append(list_[right])
            right += 1
    # Items left: list_[left:mid + 1]
    #             list_[right:j + 1]
    return result + list_[left:mid + 1] + list_[right:j + 1]


def _mergesort_2(list_: list, i: int, j: int) -> None:
    """
    Sort the items in list_[i] through list_[j] in
    non-decreasing order.
    """
    if i < j:
        mid = (i + j) // 2
        _mergesort_2(list_, i, mid)
        _mergesort_2(list_, mid + 1, j)
        list_[i:j + 1] = _merge_2(list_, i, mid, j)


def mergesort_2(list_: list) -> None:
    """
    Sort list list_ in non-decreasing order.

    """
    _mergesort_2(list_, 0, len(list_) - 1)


# === Bubblesort 2 === #
def bubblesort_2(list_: list) -> None:
    """
    Sort the items in list_ in non-decreasing order.

    """
    j = len(list_) - 1
    swapped = True
    # Stop when no elements are swapped.
    while swapped and j != 0:
        swapped = False
        # Swap every item that is out of order.
        for i in range(j):
            if list_[i] > list_[i + 1]:
                swapped = True
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
        j -= 1

