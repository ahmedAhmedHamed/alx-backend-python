#!/usr/bin/env python3
"""
tests the utils module
"""
import unittest
from unittest import TestCase
from parameterized import parameterized
import utils


class TestAccessNestedMap(TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
