import unittest
from models.base import base


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        """Test when list_dictionaries is empty"""
        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), "[]")

        """Test when list_dictionaries contains dictionaries"""
        list_dicts = [{"key1": "value1"}, {"key2": "value2"}]
        expected_json = '[{"key1": "value1"}, {"key2": "value2"}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_save_to_file(self):
        """Test saving an empty list to a JSON file"""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        """Test saving a list of dictionaries to a JSON file"""
        list_dicts = [{"key1": "value1"}, {"key2": "value2"}]
        Base.save_to_file(list_dicts)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[{"key1": "value1"}, {"key2": "value2"}]')

    def test_from_json_string(self):
        """Test when json_string is None"""
        self.assertEqual(Base.from_json_string(None), [])

        """Test when json_string is an empty list representation"""
        self.assertEqual(Base.from_json_string("[]"), [])

        """Test when json_string contains a list of dictionaries"""
        json_string = '[{"key1": "value1"}, {"key2": "value2"}]'
        expected_list = [{"key1": "value1"}, {"key2": "value2"}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

    def test_create(self):
        """Test creating an instance of Rectangle"""
        rectangle_dict = {"id": 1, "width": 2, "height": 3}
        rectangle_instance = Base.create(**rectangle_dict)
        self.assertEqual(rectangle_instance.id, 1)
        self.assertEqual(rectangle_instance.width, 2)
        self.assertEqual(rectangle_instance.height, 3)

        """Test creating an instance of Square"""
        square_dict = {"id": 2, "size": 4}
        square_instance = Base.create(**square_dict)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 4)

if __name__ == "__main__":
    unittest.main()
