"""Sorting Algorithms

    This file includes all sorting algorithms existing in
    this project. It provides an interface to use them
    easily to sort lists.

    @author Florian Dahlitz
"""


def _swap(thelist: list, a, b):
    """swap

        Swaps two values of a given lists. Needs a pointer
        to the lists and the two positions of the
        values to swap.
    """
    tmp = thelist[a]
    thelist[a] = thelist[b]
    thelist[b] = tmp


def quick_sort(data: list, left: int, right: int) -> list:
    """
    Quick Sort

    As the name mentions it's a very efficient and fast
    sorting algorithm.

    The second argument (left) is the first index of the list.
    The third argument (right) is the last index of the list.
    """
    le = left
    r = right
    comparison = data[int((le + r) / 2)]

    while le <= r:
        while data[le] < comparison:
            le += 1

        while data[r] > comparison:
            r -= 1

        if le <= r:
            _swap(data, le, r)
            le += 1
            r -= 1

    if left < r:
        quick_sort(data, left, r)

    if le < right:
        quick_sort(data, le, right)

    return data
