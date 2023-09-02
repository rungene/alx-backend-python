#!/usr/bin/env python3
"""
test_utils module. Unit test for utils.access_nested_map
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
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
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_key):
        """
        This method Use the assertRaises context manager to
        test that a KeyError is raised
        """
        with self.assertRaises(KeyError):
            result = access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test suite for get_json function"""
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test that utils.get_json returns the expected result."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test suite for test_memoize method."""
    def test_memoize(self):
        """
        Test that when calling a_property twice, the
        correct result is returned but a_method is only
        called once"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """Method to test, returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Returns memoize property"""
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as memo_mock:
            test_memo = TestClass()
            test_memo.a_property
            test_memo.a_property

            memo_mock.asset_called_once()
