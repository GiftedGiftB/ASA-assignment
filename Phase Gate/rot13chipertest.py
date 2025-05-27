import rot13chiper
from unittest import TestCase


class Testrot13chiper(TestCase):
	def test_get_encrypt_text_function_exists(self):
		rot13chiper.get_rot13chiper(3)
