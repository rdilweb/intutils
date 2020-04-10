"""intutils is a basic Python integer manipulation library."""

from typing import Any, List


__author__ = "Reece Dunham"
__license__ = "MIT"
__all__ = [
    "divisible_by_no_decimals", "is_even", "is_odd", "is_int",
    "sort_greatest_to_least"
]


def divisible_by_no_decimals(number: int, divisor: int) -> bool:
    """
    Checks if the `number` can be divided by the `divisor` without the
    resulting number having decimals in it.

    Arguments:
        number: The base number.
        divisor: The number to divide the `number` by.

    Returns:
        If it is possible.
    """
    return (number % divisor) == 0


def is_even(number: int) -> bool:
    """
    Returns if the `number` is even.

    Arguments:
        number: The number to check.

    Returns:
        If the number is even.
    """
    return divisible_by_no_decimals(number, 2)


def is_odd(number: int) -> bool:
    """
    Returns if the `number` is odd.

    Arguments:
        number: The number to check.

    Returns:
        If the number is odd.
    """
    return not is_even(number)


def is_int(testable: Any) -> bool:
    """
    Returns if the passed item is an integer.

    Arguments:
        number: The item to check.

    Returns:
        If the object is an integer or a string that can be an integer.
    """
    if type(testable) == int:
        return True
    elif type(testable) == str:
        try:
            int(testable)
            return True
        except ValueError:
            return False
    return False


def sort_greatest_to_least(mylist: List[int]) -> List[int]:
    """
    Sorts the passed list of integers from greatest to least.

    Arguments:
        mylist: The list to sort.

    Returns:
        The sorted list.
    """
    return list(
        reversed(
            _Sorting().quick_sort(mylist, 0, len(mylist) - 1)
        )
    )


def days_in_month(month_number: int, year_int=0) -> int:
    """
    Returns the number of days in the given month.

    Arguments:
        month_number: The month.
        year_int: The year to check (for leap years).

    Returns:
        The day count.
    """
    if month_number >= 13:
        raise ValueError("There isn't a month with a number bigger then 12!!")

    if is_even(month_number) and not month_number == 2:
        # even month, not Febrary
        return 30

    if is_odd(month_number):
        # odd month
        return 31

    if divisible_by_no_decimals(year_int, 4):
        # leap year
        return 29

    # typical year
    return 28


class _Sorting:
    """
    Sorting Algorithms

    This class includes some interfaces to easily to sort lists.

    Author: Florian Dahlitz
    GitHub: https://github.com/DahlitzFlorian/SortingAlgorithms
    """

    def _swap(self, thelist: List[int], a: int, b: int) -> None:
        """
        Swaps two values of a given lists. Needs a pointer
        to the lists and the two positions of the values to swap.

        Parameters:
            thelist: The list containing the items.
            a: The position item `a` is in.
            b: The position item `b` is in.
        """
        tmp = thelist[a]
        thelist[a] = thelist[b]
        thelist[b] = tmp

    def quick_sort(self, data: List[int], left: int, right: int) -> List[int]:
        """
        Quick Sort

        As the name mentions it's a very efficient and fast
        sorting algorithm.

        Parameters:
            data: The list to sort.
            left: The first index of the list.
            right: The last index of the list.

        Returns:
            The sorted list.
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
                self._swap(data, le, r)
                le += 1
                r -= 1

        if left < r:
            self.quick_sort(data, left, r)

        if le < right:
            self.quick_sort(data, le, right)

        return data
