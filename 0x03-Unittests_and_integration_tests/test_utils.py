#!/usr/bin/env python3
"""
test_utils module. Unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Assert This method test that the method return value
        is the expected result
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_key):
        """
        This method Use the assertRaises context manager to
        test that a KeyError is raised
        """
        with self.assertRaises(KeyError):
            result = access_nested_map(nested_map, path)
