"""
This file contains unit tests for the utility functions (particularly extract_domain).
It uses the built-in unittest framework in Python.
"""

import unittest
from scripts.utils import extract_domain

class TestUtils(unittest.TestCase):
    """
    A collection of test cases to ensure extract_domain behaves as expected.
    """

    def test_extract_domain_basic(self):
        self.assertEqual(extract_domain("http://example.com"), "example.com")
        self.assertEqual(extract_domain("https://example.com"), "example.com")
    
    def test_extract_domain_with_www(self):
        self.assertEqual(extract_domain("http://www.example.com"), "example.com")
    
    def test_extract_domain_subdomain(self):
        self.assertEqual(extract_domain("http://sub.example.com"), "example.com")
    
    def test_extract_domain_invalid(self):
        self.assertEqual(extract_domain(""), "")
        self.assertEqual(extract_domain(None), "")

if __name__ == '__main__':
    unittest.main()
