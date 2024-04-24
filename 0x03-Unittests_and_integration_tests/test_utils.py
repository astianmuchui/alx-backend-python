#!/usr/bin/env python3

"""
Unit testing
"""

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize

class TestAccessNestedMap(TestCase):
    """
    TestAccessNestedMap class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test_access_nested_map method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests for keyerror exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """
    TestGetJson class
    """

    @parameterized.expand([
        ("http://example.com", True),
        ("http://holberton.io", False),
    ])
    def test_get_json(self, url, expected):
        """
        test_get_json method
        We don’t want to make any actual external HTTP calls. Use
        unittest.mock.patch to patch requests.get. Make sure it
        returns a Mock object with a json method that returns test_payload
        """

        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = expected
            self.assertEqual(get_json(url), expected)


class TestMemoize(TestCase):
    """
    Unit tests for memoize function
    """

    def test_memoize(self):

        """
        Function to test memoize
        """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()


        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            my_object = TestClass()
            self.assertEqual(my_object.a_property, 42)
            self.assertEqual(my_object.a_property, 42)
            self.assertEqual(mock_method.call_count, 1)
