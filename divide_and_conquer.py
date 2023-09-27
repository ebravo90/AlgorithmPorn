""" Divide and conquer algorithms module  """
import re
from typing import Dict, List, Optional

from utils.utils import ProfileUtils, MiscUtils


profiler = ProfileUtils()

class FindMinMax:
    """
    Find the minimum or maximum number in a list.
    """

    def __init__(self, number_list: List[int]):

        if not MiscUtils.validate_param_annotations(
            FindMinMax.__init__,
            (number_list)
        ):
            print("Incorrect parameter type.")
            return None

        self._number_list: List[int] = number_list
        self._method: str = None

    def _set_strategy(
            self,
            value_left: int,
            value_right: int
    ) -> Optional[int]:
        """
        Get the strategy to return the min or max value based on given
        method.

        :param value_left: Value from left side of the input list.
        :type value_left: int
        :param value_right: Value from right side of the input list.
        :type value_right: int
        :return: The value based on the given method, otherwise None.
        :rtype: Optional[int]
        """

        if re.match(r"[m|M][i|I][n|N]", self._method):
            return min(value_left, value_right)
        elif re.match(r"[m|M][a|A][x|X]", self._method):
            return max(value_left, value_right)
        else:
            print(f"Only allowed min or max, not '{self._method}'")
            return None

    def _find_min_max(
            self,
            left_side: int,
            right_side: int
    ) -> int:
        """
        Find the maximum value on a given list.

        :param left_side: Index of the beginning of the left side of the
                          list.
        :type left_side: int
        :param right_side: Index of the last element on the right side
                           of the
                           list.
        :type right_side: int
        :return: Integer depending of the given method to get from list
                 (min or max).
        :rtype: int
        """

        if left_side == right_side:
            return self._number_list[left_side]

        mid = (left_side + right_side) // 2

        value_left  = self._find_min_max(left_side, mid)
        value_right = self._find_min_max(mid + 1, right_side)

        return self._set_strategy(value_left, value_right)

    def get_number(self, method: str) -> Optional[int]:
        """
        Method that returns minimum or maximum value from a list.

        :return: Integer of the number found in the iterable according
                 to the method chosen.
        :rtype: int
        """

        if not MiscUtils.validate_param_annotations(
            FindMinMax.get_number,
            (method)
        ):
            print("Incorrect parameter type.")
            return None

        self._method = method

        left_side = 0
        right_side = len(self._number_list) - 1

        get_val = self._find_min_max(left_side, right_side)

        return get_val
