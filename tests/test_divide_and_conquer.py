import unittest

import numpy as np

from divide_and_conquer import FindMinMax


class TestFindMinMax(unittest.TestCase):
    """
    Test cases for the Find Min/Max class.
    """

    @classmethod
    def setUpClass(cls):

        # Define big and max numbers in arrays.
        cls.small_min_num = -5
        cls.small_max_num = 50

        cls.med_min_num = -10
        cls.med_max_num = 500

        cls.big_min_num = -20
        cls.big_max_num = 1000

        # Define 1D arrays with different sizes.
        cls.small_arr = [
            number for number in range(cls.small_min_num, cls.small_max_num)
        ]
        cls.medium_arr = [
            number for number in range(cls.med_min_num, cls.med_max_num)
        ]
        cls.big_arr = [
            number for number in range(cls.big_min_num, cls.big_max_num)
        ]

        return None

    def test_get_min_number_small_array(self):
        """
        Get the minimum number in a small array.
        """
        find_min_max = FindMinMax(self.small_arr)
        result = find_min_max.get_number("min")

        self.assertEqual(self.small_min_num, result)

        return None

    def test_get_max_number_small_array(self):
        """
        Get the maximum number in a small array.
        """
        find_min_max = FindMinMax(self.small_arr)
        result = find_min_max.get_number("max")

        self.assertEqual(self.small_max_num - 1, result)

        return None

    def test_get_min_number_medium_array(self):
        """
        Get the minimum number in a medium array.
        """
        find_min_max = FindMinMax(self.medium_arr)
        result = find_min_max.get_number("min")

        self.assertEqual(self.med_min_num, result)

        return None

    def test_get_max_number_medium_array(self):
        """
        Get the medium number in a medium array.
        """
        find_min_max = FindMinMax(self.medium_arr)
        result = find_min_max.get_number("max")

        self.assertEqual(self.med_max_num - 1, result)

        return None

    def test_get_min_number_big_array(self):
        """
        Get the minimum number in a big array.
        """
        find_min_max = FindMinMax(self.big_arr)
        result = find_min_max.get_number("min")

        self.assertEqual(self.big_min_num, result)

        return None

    def test_get_max_number_big_array(self):
        """
        Get the medium number in a big array.
        """
        find_min_max = FindMinMax(self.big_arr)
        result = find_min_max.get_number("max")

        self.assertEqual(self.big_max_num - 1, result)

        return None


if __name__ == '__main__':
    unittest.main()
