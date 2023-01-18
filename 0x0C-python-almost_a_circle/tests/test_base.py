#!/usr/bin/python3
"""base class unittest module

"""
import unittest
import json

from models.base import Base
class TestBaseClass(unittest.TestCase):
    def test_BaseIntancewith_no_arg(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_BaseIntancewithInteger(self):
        base = Base(9)
        self.assertEqual(base.id, 9)

    def test_Baseinstancesecond(self):
        base = Base()
        self.assertEqual(base.id, 2)

    def test_BasewithListarg(self):
        base = Base([1, 2, 3])
        self.assertEqual(base.id, [1, 2, 3])

    def test_BasewithNone(self):
        base = Base(None)
        self.assertEqual(base.id, 3)

    def test_BasewithDict(self):
        base = Base({"1": 2})
        self.assertEqual(base.id, {"1": 2})

    def test_Basewithstring(self):
        base = Base("Dennis")
        self.assertEqual(base.id, "Dennis")

    def test_accessprivateproperty(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_accessprivateproperty_on_instance(self):
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_None(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_no_args(self):
        base = Base()
        with self.assertRaises(TypeError):
            base.to_json_string()

    def test_to_json_string_with_string(self):
        base = Base()
        self.assertEqual(base.to_json_string("string"), '"string"')

    def test_to_json_string_with_list(self):
        base = Base()
        self.assertEqual(base.to_json_string([{"1": 2}, {"2": 3}]), '[{"1": 2}, {"2": 3}]')

    def test_from_json_string_with_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_with_emptystring(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_with_dict_string(self):
        self.assertEqual(Base.from_json_string('{"1": 2}'), {"1": 2})

    def test_from_json_string_with_list_string(self):
        self.assertEqual(Base.from_json_string('[{"1": 2}, {"2": 3}]'), [{"1": 2}, {"2": 3}])

    def test_from_json_string_with_string(self):
        self.assertEqual(Base.from_json_string('"string"'), "string")

    def test_from_json_string_with_nonjson_string(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string("string")

    def test_from_json_string_with_empty_list_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])


if __name__ == "__main__":
    unittest.main()
