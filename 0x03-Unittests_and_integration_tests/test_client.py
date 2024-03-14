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
        ("google"),
        ("abc")
        ])
    @patch('client.get_json')
    def test_org(
            self,
            val: str,
            mock_get_json):
        """test for org method"""
        github_client = GithubOrgClient(val)
        github_client.org()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{val}")
