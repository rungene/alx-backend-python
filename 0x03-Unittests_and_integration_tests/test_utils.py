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
        (nested_map={"a": 1}, path=("a",), 1),
        (nested_map={"a": {"b": 2}}, path=("a",), {"b": 2}),
        (nested_map={"a": {"b": 2}}, path=("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        This method test that the method return value
        is the expected result"""
        result = access_nested_map(nested_map, path)

        self.assertEqual(result, expected)
