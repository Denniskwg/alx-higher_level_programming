#!/usr/bin/python3
"""base class unittest module

"""
import unittest

from models.base import Base
class TestBaseClass(unittest.TestCase):
    def testBaseIntancewith_no_arg(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def testBaseIntancewithInteger(self):
        base = Base(9)
        self.assertEqual(base.id, 9)

    def testBaseinstancesecond(self):
        base = Base()
        self.assertEqual(base.id, 2)

    def testBasewithListarg(self):
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])

    def testBasewithNone(self):
        base = Base(None)
        self.assertEqual(base.id, 3)

    def testBasewithDict(self):
        base = Base({"1": 2})
        self.assertEqual(base.id, {"1": 2})

    def testBasewithstring(self):
        base = Base("Dennis")
        self.assertEqual(base.id, "Dennis")

    def testaccessprivateproperty(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def testaccessprivateproperty_on_instance(self):
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects

    def test_to_json_string(self):
        base = Base()
        self.assertEqual(base.to_json_string([]), "[]")

    def test_to_json_string_with_None(self):
        base = Base()
        self.assertEqual(base.to_json_string(None), "[]")

    def test_to_json_string_with_no_args(self):
        base = Base()
        with self.assertRaises(TypeError):
            base.to_json_string()

    def test_to_json_string_with_string(self):
        base = Base()
        self.assertEqual(base.to_json_string("string"), '"string"')

    def test_to_json_string_with_dict(self):
        base = Base()
        self.assertEqual(base.to_json_string({"1": 2}), '{"1": 2}')

    def test_to_json_string_with_list(self):
        base = Base()
        self.assertEqual(base.to_json_string([{"1": 2}, {"2": 3}]), '[{"1": 2}, {"2": 3}]')

if __name__ == "__main__":
    unittest.main()
