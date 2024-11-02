#!/usr/bin/env python3
"""
tests the client module
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    tests access GithubOrgClient
    """

    @parameterized.expand([
        ("google", ),
        ("abc", )
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json: MagicMock):
        """ test that GithubOrgClient.org returns the correct value. """
        my_client = GithubOrgClient(org)
        my_client.org()
        my_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")
