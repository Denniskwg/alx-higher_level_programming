#!/usr/bin/python3

"""rectangle class unittest

"""

from models.rectangle import Rectangle
import unittest
from unittest import mock
from unittest.mock import patch
import io

class TestRectangle(unittest.TestCase):

    def test_rectangle_instantiation(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 12)

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
        self.assertEqual(rect.id, 14)

    def test_rectangle_instantiation_with_3_argument(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 13)

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
        self.assertEqual(str(rect), "[Rectangle] (15) 0/0 - 1/2")

    def test_display(self):
        rect = Rectangle(2, 3)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rect.display()

        assert fake_stdout.getvalue() == "##\n##\n##\n"

    def test_display_2(self):
        rect = Rectangle(2, 3, 1, 1)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rect.display()

        assert fake_stdout.getvalue() == "\n ##\n ##\n ##\n"

    def test_to_dictionary(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.to_dictionary(), {"id": 16,\
            "width": 1, "height": 2, "x": 0, "y": 0})

    def test_update(self):
        r = Rectangle(1, 2)
        r.update()
        self.assertEqual(r.id, 17)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_create(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_save_to_file_with_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(str(f.read()), '[]')

    def test_save_to_file_with_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(str(f.read()), '[]')
