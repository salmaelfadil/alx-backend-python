#!/usr/bin/env python3
"""Test Client Module"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """class fort testing client function"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})])
    @patch('client.get_json')
    def test_org(
            self,
            val: str,
            expected: Dict[str, str],
            mock_get_json) -> None:
        """test for org method"""
        mock_get_json.return_value = expected
        github_client = GithubOrgClient(val)
        return_val = github_client.org()
        mock_org.assert_called_once_with(f"https://api.github.com/orgs/{val}")
        self.assertEqual(return_val, expected)
