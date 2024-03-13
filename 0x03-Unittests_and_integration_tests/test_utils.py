#!/usr/bin/env python3
"""Test Utils Module"""
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """test class for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
            ,])
    def test_access_nested_map(self, nested_map: Dict, 
            path: Tuple[str], expected: Union[Dict, int]) -> None:
            """"acess_nested_map test"""
            self.assertEqual(access_nested_map(nested_map, path), expected)
