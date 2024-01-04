#!/usr/bin/env python3
""" Module for testing utils """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key not found: 'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "Key not found: 'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception, expected_message):
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        # Mocking the requests.get method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        # Call the function with the mocked requests.get
        result = get_json(test_url)

        # Assert that the mocked requests.get was called exactly once with the test_url
        mock_requests_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to the test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Call a_property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Assert that a_method was called only once
        mock_a_method.assert_called_once()

        # Assert that the results are correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
