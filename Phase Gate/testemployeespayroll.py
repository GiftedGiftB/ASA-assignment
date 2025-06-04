import employeespayroll
from unittest import TestCase


class Testcube(TestCase):
	def test_get_employeespayroll_function_exists(self):
		employeespayroll.get_employeespayroll(3)
