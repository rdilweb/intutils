"""
Copyright 2019-present Reece Dunham.
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-----------

See https://docs.rdil.rocks/libraries/intutils for more information.
"""  # noqa


from .vendor import sorting


def divisible_by_no_decimals(number: int, divisor: int) -> bool:
    return (number % divisor) == 0


def is_even(number: int) -> bool:
    return divisible_by_no_decimals(number, 2)


def is_odd(number: int) -> bool:
    return not is_even(number)


def is_int(testable) -> bool:
    if type(testable) == int:
        return True
    elif type(testable) == str:
        try:
            int(testable)
            return True
        except ValueError:
            return False
    return False


def sort_greatest_to_least(mylist: list) -> list:
    return list(reversed(sorting.quick_sort(mylist, 0, len(mylist) - 1)))
