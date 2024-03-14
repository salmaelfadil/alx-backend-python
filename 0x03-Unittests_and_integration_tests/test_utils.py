#!/usr/bin/env python3
"""Test Utils Module"""
from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """test class for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]) -> None:
        """"acess_nested_map test"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception) -> None:
        """test exception"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test class for get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
            ])
    @patch('utils.requests.get')
    def test_get_json(self, url: str, ex_payload: Dict, mock_get) -> None:
        """test method for get_json"""
        mock_response = Mock()
        mock_response.json.return_value = ex_payload
        mock_get.return_value = mock_response
        return_val = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(return_val, ex_payload)


class TestMemoize(unittest.TestCase):
    """test class for memoize function"""
    def test_memoize(self) -> None:
        """test memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as obj:
            test = TestClass()
            res1 = test.a_property()
            res2 = test.a_property()
            obj.assert_called_once()
