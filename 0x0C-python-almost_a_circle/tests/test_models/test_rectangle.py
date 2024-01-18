#!/usr/bin/python3
"""Defines unittests for rectangle.py"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def setUp(self):
        """Create a default rectangle for testing"""
        self.default_rectangle = Rectangle()

    def test_constructor_with_no_arguments(self):
        self.assertEqual(self.default_rectangle.width, 0)
        self.assertEqual(self.default_rectangle.height, 0)
        self.assertEqual(self.default_rectangle.x, 0)
        self.assertEqual(self.default_rectangle.y, 0)

    def test_constructor_with_args(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_constructor_with_keyword_arguments(self):
        rectangle = Rectangle(width=6, height=7, x=8, y=9)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 8)
        self.assertEqual(rectangle.y, 9)

    def test_constructor_with_mixed_args(self):
        rectangle = Rectangle(1, height=2, x=3, y=4)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_to_dictionary_method(self):
        rectangle_dict = self.default_rectangle.to_dictionary()
        self.assertIsInstance(rectangle_dict, dict)
        self.assertEqual(rectangle_dict, {'id': None, 'width': 0,
                                          'height': 0, 'x': 0, 'y': 0})

    def test_str_representation(self):
        str_representation = str(self.default_rectangle)
        self.assertIsInstance(str_representation, str)
        self.assertEqual(str_representation, "[Rectangle] (None) 0/0 - 0/0")

    def test_update_method_with_args(self):
        self.default_rectangle.update(1, 2, 3, 4, 5)
        self.assertEqual(self.default_rectangle.width, 2)
        self.assertEqual(self.default_rectangle.height, 3)
        self.assertEqual(self.default_rectangle.x, 4)
        self.assertEqual(self.default_rectangle.y, 5)

    def test_update_method_with_kwargs(self):
        self.default_rectangle.update(width=5, height=6, x=7, y=8)
        self.assertEqual(self.default_rectangle.width, 5)
        self.assertEqual(self.default_rectangle.height, 6)
        self.assertEqual(self.default_rectangle.x, 7)
        self.assertEqual(self.default_rectangle.y, 8)

    def test_constructor_with_negative_args(self):
        rectangle = Rectangle(-1, -2, -3, -4)
        self.assertEqual(rectangle.width, 0)
        self.assertEqual(rectangle.height, 0)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_constructor_with_float_args(self):
        rectangle = Rectangle(1.5, 2.5, 3.5, 4.5)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_constructor_with_invalid_argument_types(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", "arguments", "should", "raise", "TypeError")

    def test_constructor_with_id(self):
        rectangle_with_id = Rectangle(1, 2, 3, 4, id=42)
        self.assertEqual(rectangle_with_id.id, 42)

    def test_update_method_with_invalid_arguments(self):
        with self.assertRaises(TypeError):
            self.default_rectangle.update("invalid", "arguments",
                                          "should", "raise", "TypeError")

    def test_update_method_with_invalid_kwargs(self):
        with self.assertRaises(ValueError):
            self.default_rectangle.update(invalid_key=42)

    def test_to_dictionary_method_with_id(self):
        rectangle_with_id = Rectangle(1, 2, 3, 4, id=32)
        rectangle_dict = rectangle_with_id.to_dictionary()
        self.assertEqual(rectangle_dict['id'], 32)

    if __name__ == "__main__":
        unittest.main()
