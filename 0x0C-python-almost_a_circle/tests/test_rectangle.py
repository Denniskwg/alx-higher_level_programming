#!/usr/bin/python3

"""rectangle class unittest

"""
from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    def test_rectangle_instantiation(self):
        rect = Rectangle(1, 1)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 8)

    def test_rectangle_instantiation_without_args(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_rectangle_instantiation_with_wrong_type_width(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 0)

    def test_rectangle_instantiation_with_dict_argument(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, '1')

    def test_rectangle_instantiation_with_list_argument(self):
        rect = Rectangle(1, 1, 1, 1)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.id, 9)

    def test_rectangle_instantiation_with_0_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)

    def test_rectangle_instantiation_with_0_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)

    def test_rectangle_instantiation_with_negative_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 1)

    def test_rectangle_instantiation_with_negative_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, -1)

    def test_rectangle_instantiation_with_negative_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 1, -1, 0)

    def test_rectangle_instantiation_with_negative_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 1, 1, -1)

    def test_rectangle_instantiation_with_id(self):
        rect = Rectangle(1, 1, 1, 1, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)
        self.assertEqual(rect.id, 89)
