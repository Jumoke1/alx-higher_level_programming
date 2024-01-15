#!/usr/bin/python3
"""Defines unittests for base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """unitest for testing instance of a base class"""

    def test_create_instance(self):
        obj = Base()
        self.assertIsInstance(obj, Base)
        self.assertIsNotNone(obj.id)

    def test_create_instance_with_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_nonempty_list(self):
        obj_list = [Base(1), Base(2)]
        json_str = Base.to_json_string([obj.to_dictionary()
                                        for obj in obj_list])
        expected_json = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(json_str, expected_json)

    def test_save_to_file_empty_list(self):
        filename = "Base.json"
        Base.save_to_file([])
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")

        os.remove(filename)

    def test_save_to_file_nonempty_list(self):
        filename = "Base.json"
        obj_list = [Base(1), Base(2)]

        try:
            Base.save_to_file(obj_list)
            self.assertTrue(os.path.exists(filename))

            with open(filename, 'r') as file:
                content = file.read()
                expected_content = '[{"id": 1}, {"id": 2}]'
                self.assertEqual(content, expected_content)
        finally:
            os.remove(filename)

    def test_load_from_file_empty_file(self):
        filename = "Base.json"
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs, [])

        self.assertFalse(os.path.exists(filename))

    def test_load_from_file_nonempty_file(self):
        filename = "Base.json"
        obj_list = [Base(1), Base(2)]
        Base.save_to_file(obj_list)

        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertIsInstance(loaded_objs[0], Base)
        self.assertIsInstance(loaded_objs[1], Base)

        os.remove(filename)

    def test_create_instance_with_dictionary(self):
        obj_dict = {'id': 1, 'width': 10, 'height': 20}
        obj = Base.create(**obj_dict)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)

    def test_from_json_string_empty_input(self):
        empty_json_str = "[]"
        result = Base.from_json_string(empty_json_str)
        self.assertEqual(result, [])

    def test_from_json_string_nonempty_input(self):
        nonempty_json_str = '[{"id": 1}, {"id": 2}]'
        result = Base.from_json_string(nonempty_json_str)
        self.assertEqual(result, [{'id': 1}, {'id': 2}])

    def test_save_to_file_csv_empty_list(self):
        filename = "Base.csv"
        Base.save_to_file_csv([])
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as csvfile:
            content = csvfile.read()
            self.assertEqual(content, "[]")

        os.remove(filename)

    def test_save_to_file_csv_nonempty_list(self):
        filename = "Base.csv"
        obj_list = [Base(1), Base(2)]

        try:
            Base.save_to_file_csv(obj_list)
            self.assertTrue(os.path.exists(filename))

            with open(filename, 'r') as csvfile:
                content = csvfile.read()
                expected_content = 'id\n1\n2\n'
                self.assertEqual(content, expected_content)
        finally:
            os.remove(filename)

    def test_load_from_file_csv_empty_file(self):
        filename = "Base.csv"
        loaded_objs = Base.load_from_file_csv()
        self.assertEqual(loaded_objs, [])

        self.assertFalse(os.path.exists(filename))

    def test_load_from_file_csv_nonempty_file(self):
        filename = "Base.csv"
        obj_list = [Base(1), Base(2)]
        Base.save_to_file_csv(obj_list)

        loaded_objs = Base.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 2)
        self.assertIsInstance(loaded_objs[0], Base)
        self.assertIsInstance(loaded_objs[1], Base)

        os.remove(filename)

    def test_draw(self):
        pass


if __name__ == '__main__':
    unittest.main()
