#!/usr/bin/env python3
"""Test Client Module"""
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from typing import Dict
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{val}")

    def test_public_repos_url(self) -> None:
        """test for mocking property"""
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock) as prop_mock:
            prop_mock.return_value = {
                    'repos_url': "https://api.github.com/users/example/repos",
                    }
            test = GithubOrgClient("example")
            val = test._public_repos_url
            self.assertEqual(prop_mock.return_value['repos_url'], val)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test method for public_repos"""
        mock_payload = [{"name": "string1"}, {"name": "string2"}]
        mock_get_json.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as prop_mock:

            prop_mock.return_value = "example"
            test = GithubOrgClient('test')
            val = test.public_repos()

            lis = [item["name"] for item in mock_payload]
            self.assertEqual(val, lis)

            prop_mock.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integeration test"""
    @classmethod
    def setUpClass(cls) -> None:
        """set up method for test"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect_mock(url):
            return {
                    'https://api.github.com/orgs/google': cls.org_payload,
                    'https://api.github.com/orgs/google/\
                            repos': cls.repos_payload,
                    }[url]
        cls.mock_get.side_effect = MagicMock(side_effect=side_effect_mock)

    def test_public_repos(self) -> None:
        """"test method for public_repos"""
        test = GithubOrgClient("google")
        repos = test.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """test method for public_repos with licence"""
        test = GithubOrgClient("google")
        repos = test.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """tear down method"""
        cls.get_patcher.stop()
