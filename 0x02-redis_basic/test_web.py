#!/usr/bin/env python3
""" Test module for web.py """
import unittest
from unittest.mock import patch
from web import get_page, redis_store


class TestWeb(unittest.TestCase):

    @patch("web.requests.get")
    def test_get_page(self, mock_get):
        mock_get.return_value.text = "Hello, World!"
        url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.google.com"

        # First time accessing the URL, it should call requests.get
        result = get_page(url)
        self.assertEqual(result, "Hello, World!")
        mock_get.assert_called_once_with(url)

        # Second time accessing the URL, it should use the cache
        result = get_page(url)
        self.assertEqual(result, "Hello, World!")
        # requests.get should still only have been called once
        mock_get.assert_called_once_with(url)

    # @patch("web.requests.get")
    # def test_get_page_different_url(self, mock_get):
    #     mock_get.return_value.text = "Hello, World!"
    #     url1 = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.google.com"
    #     url2 = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.bing.com"

    #     # Accessing two different URLs should call requests.get twice
    #     get_page(url1)
    #     get_page(url2)
    #     self.assertEqual(mock_get.call_count, 2)

    # @patch("web.requests.get")
    # def test_get_page_no_cache(self, mock_get):
    #     mock_get.return_value.text = "Hello, World!"
    #     url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.google.com"

    #     # If the cache expires, it should call requests.get again
    #     get_page(url)
    #     redis_store.delete(f"result:{url}")  # manually delete the cache
    #     get_page(url)
    #     self.assertEqual(mock_get.call_count, 2)


if __name__ == "__main__":
    unittest.main()
