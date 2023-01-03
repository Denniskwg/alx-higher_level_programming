#!/usr/bin/python3
"""Unittest for max_integer([..])

"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class Testmaxinteger(unittest.TestCase):
    def setUp(self):
        self.l = [1, 2, 3, 4]
        self.t = (1, 3, 4, 9)

    def text_max_integer(self):
        self.assertEqual(max_integer(self.l), 4)
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    def test_no_input(self):
        self.assertEqual(max_integer(), None)
    def test_tuple(self):
        self.assertEqual(max_integer(self.t), 9)
    def test_integer_input(self):
        with self.assertRaises(TypeError):
            max_integer(1)
    def test_string_input(self):
        self.assertEqual(max_integer("Dennis"), 's')
    def test_digit_string(self):
        self.assertEqual(max_integer("9652"), '9')

if __name__ == "__main__":
    unittest.main()
