#!/usr/bin/env python3
"""
Unit tests for access_nested_map function in utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Tuple, Any
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Mapping[str, Any], path: Tuple[str, ...],
            expected: Any
    ) -> None:
        """
        Test access_nested_map returns expected value for given nested_map
        and path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping[str, Any], path: Tuple[str, ...]
    ) -> None:
        """
        Test access_nested_map raises KeyError with expected message
        for invalid path.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator function."""
    def test_memoize(self):
        """Tests that memoize caches the result after the first call."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()

        with patch.object(
                instance, 'a_method', return_value=42
        ) as mock_method:
            result_first_call = instance.a_property
            result_second_call = instance.a_property

            self.assertEqual(result_first_call, result_second_call)
            mock_method.assert_called_once()


class TestGetJson(unittest.TestCase):
    """Test cass for utils.get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: Mock):
        """test that get_json returns expected result with mock"""
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
