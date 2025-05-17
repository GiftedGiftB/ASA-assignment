import cube
import unittest


class Testcube(unittest.Testcase):
	def test_get_cube_function_exists(self):
		cube.get_cube(3)

	def test_that_cube_function_return_correct_answer(self):
		actual = cube.get_cube(5)
		expected = 125
		self.assertEquals(actual, expected)
		actual = cube.get_cube(10)
		expected = 1000
		self.assertEqual(actual, expected)

	def test_that_get_cube_function_work_for_number_between_1_to_10(self):