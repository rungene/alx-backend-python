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


class TestGetJson(unittest.TestCase):
    """Test suite for get_json function"""
    @patch('request.get')
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """test that utils.get_json returns the expected result."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        request_get_mock = Mock()
        request_get_mock.return_value = mock_response
        with patch('get_json.requests.get', request_get_mock):
            result = get_json(test_url)

            request_get_mock.assert_called_once_with(test_url)
            self.assertEqual(result.json(), test_payload)
