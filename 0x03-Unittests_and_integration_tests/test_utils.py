#!/usr/bin/env python3
"""
tests the utils module
"""
import unittest
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
import utils


class TestAccessNestedMap(TestCase):
    """
    tests access nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        this test is ran 3 times for different inputs
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        tries to access non existing keys and raises key error
        """
        self.assertRaises(KeyError, utils.access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    tests get_json
    """

    class Jsongetter:
        """
        class to mock return of requests.get
        """

        def __init__(self, json):
            """
            initialisation here
            """
            self.__json = json

        def json(self):
            """ requests.get().json() """
            return self.__json

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests):
        """tests get json"""
        mock_requests.return_value = self.Jsongetter(test_payload)

        self.assertEqual(utils.get_json(test_url), test_payload)
