#!/usr/bin/python3

"""rectangle class unittest

"""

from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):

    def test_rectangle_instantiation(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 9)

    def test_rectangle_instantiation_without_args(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_rectangle_instantiation_with_wrong_type_width(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 0)

    def test_rectangle_instantiation_with_dict_argument(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, '1')

    def test_rectangle_instantiation_with_4_argument(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 11)

    def test_rectangle_instantiation_with_3_argument(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 10)

    def test_rectangle_instantiation_with_0_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)

    def test_rectangle_instantiation_with_0_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)

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

    def test_rectangle_instantiation_with_wrongtype_x(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "3")

    def test_rectangle_instantiation_with_wrongtype_y(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "4")

    def test_rectangle_instantiation_with_id_and_4_args(self):
        rect = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 89)

    def test_area(self):
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_str_(self):
        rect = Rectangle(1, 2)
        self.assertEqual(str(rect), "[Rectangle] (12) 0/0 - 1/2")
