#!/usr/bin/env python3

"""
Unit testing
"""

from unittest import TestCase
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map


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

    @parameterized.expand(
        {
            ({}, ("a",),),
            ({"a": 1}, ("a", "b")),
        }
    )
    def test_acess_nested_map_exception(self, nested_map, path):
        """
        Tests for keyerror exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

