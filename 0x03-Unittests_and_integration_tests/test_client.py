#!/usr/bin/env python3
"""
tests the client module
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    tests access GithubOrgClient
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json: MagicMock):
        """ test that GithubOrgClient.org returns the correct value. """
        my_client = GithubOrgClient(org)
        my_client.org()
        my_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """ test_public_repos_url """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            payload = "returned payload"
            mock_org.return_value = {"repos_url": "returned payload"}
            my_client = GithubOrgClient("test")
            self.assertEqual(my_client._public_repos_url, payload)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock):
        """
        tests public repos property, mocking everything
        """
        payload = {"repos_url": "test"}
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_org:
            payload = "test"
            mock_org.return_value = payload
            my_client = GithubOrgClient("test")
            self.assertEqual(my_client._public_repos_url, payload)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: dict, license_key: str, expected: bool):
        """ to unit-test GithubOrgClient.has_license """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)
