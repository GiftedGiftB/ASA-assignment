from randomnumber import get_length, get_even_positions, get_odd_positions, get_element_at_every_third_position, get_average

import unittest


class MyTestCase(unittest.TestCase):
    def test_that_length_function_works_well(self):
        list = [10,15,2,12,13,38,34,8,3,7]
        self.assertEqual(get_length(list), 10)

    def test_that_even_positions_works_well(self):
        list = [10,15,2,12,13,38,34,8,3,7]
        self.assertEqual(get_even_positions(list), 62)

    def test_that_odd_positions_works_well(self):
        list = [10,15,2,12,13,38,34,8,3,7]
        self.assertEqual(get_odd_positions(list), 80)

    def test_that_element_at_every_third_position_works_well(self):
        list = [10,15,2,12,13,38,34,8,3,7]
        self.assertEqual(get_element_at_every_third_position(list), 228)

    def test_that_average_function_works_well(self):
        list = [10,15,2,12,13,38,34,8,3,7]
        self.assertEqual(get_average(list), 14.2)

    def test_that_last_element_at_third_position_is_not_equal_zero(self):
        list = [10,15,2,12,13,38,34,8,3,7]
        self.assertEqual(get_element_at_every_third_position(list), 228)


